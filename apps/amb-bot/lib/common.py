"""Shared helpers for the serverless AMB bot (front door + worker).

Reuses the existing dispatcher (apps/slack-bot/amb.py) vendored into _vendor/ by
scripts/vendor.sh. The tools run as subprocesses under this function's Python
(amb._venv_py falls back to sys.executable when no per-tool venv exists), with the
data dir pointed at /tmp (Vercel's only writable path).
"""
from __future__ import annotations
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
VENDOR = os.path.join(HERE, "_vendor")

# Make the vendored dispatcher importable and point it at vendored tools + /tmp.
os.environ.setdefault("AMB_TOOLS_DIR", os.path.join(VENDOR, "tools"))
os.environ.setdefault("AMB_DATA_DIR", "/tmp/amb-brands")
sys.path.insert(0, os.path.join(VENDOR, "slack-bot"))

SB_URL = os.environ.get("NEXT_PUBLIC_SUPABASE_URL") or os.environ.get("SUPABASE_URL")
SB_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET", "")


# ── Slack request signature (https://api.slack.com/authentication/verifying-requests-from-slack) ──
def verify_slack(headers: dict, raw_body: bytes) -> bool:
    ts = headers.get("x-slack-request-timestamp", "")
    sig = headers.get("x-slack-signature", "")
    if not ts or not sig or not SIGNING_SECRET:
        return False
    if abs(time.time() - int(ts)) > 60 * 5:          # replay window
        return False
    base = b"v0:" + ts.encode() + b":" + raw_body
    mine = "v0=" + hmac.new(SIGNING_SECRET.encode(), base, hashlib.sha256).hexdigest()
    return hmac.compare_digest(mine, sig)


# ── Supabase REST (service role) ──
def _sb(method: str, path: str, body=None, prefer: str = "return=representation"):
    req = urllib.request.Request(
        f"{SB_URL}/rest/v1/{path}",
        data=json.dumps(body).encode() if body is not None else None,
        method=method,
        headers={"apikey": SB_KEY, "Authorization": f"Bearer {SB_KEY}",
                 "Content-Type": "application/json", "Prefer": prefer})
    try:
        r = urllib.request.urlopen(req)
        txt = r.read()
        return json.loads(txt) if txt else []
    except Exception:
        return []


def enqueue_job(**fields) -> list:
    """Insert a job; dedup on slack_event_id. Returns inserted rows (empty if dup)."""
    return _sb("POST", "amb_job?on_conflict=slack_event_id", [fields],
               prefer="resolution=ignore-duplicates,return=representation")


def claim_next_job():
    rows = _sb("GET", "amb_job?status=eq.queued&order=created_at.asc&limit=1")
    if not rows:
        return None
    job = rows[0]
    upd = _sb("PATCH", f"amb_job?id=eq.{job['id']}&status=eq.queued",
              {"status": "running", "started_at": "now()", "attempts": job.get("attempts", 0) + 1})
    return upd[0] if upd else None          # empty = another worker claimed it


def finish_job(job_id, status, result="", error=""):
    _sb("PATCH", f"amb_job?id=eq.{job_id}",
        {"status": status, "result": result[:2000], "error": error[:2000], "completed_at": "now()"},
        prefer="return=minimal")


# ── Slack ──
def slack():
    from slack_sdk import WebClient
    return WebClient(token=SLACK_BOT_TOKEN)


def say(channel, thread_ts, text):
    try:
        slack().chat_postMessage(channel=channel, thread_ts=thread_ts, text=text)
    except Exception:
        pass


# ── Build (reuses amb.py) ──
def run_job(job: dict) -> dict:
    """Download the job's files, run the build, upload artifacts to the thread."""
    import amb
    brand = job["brand"]
    channel, thread = job.get("channel"), job.get("thread_ts")
    action = job.get("action") or "build"
    note = job.get("note") or ""
    d = amb._brand_dir(brand)

    pdfs, imgs = [], []
    for f in (job.get("files") or []):
        name = f.get("name", "file")
        dest = d / "inputs" / name
        try:
            amb.download(f["url"], str(dest), SLACK_BOT_TOKEN)
            (pdfs if name.lower().endswith(".pdf") else imgs).append(str(dest))
        except Exception:
            pass

    if action == "build" or (action == "storyboard" and pdfs and not (d / "output/storyboard_model.json").exists()):
        res = amb.run_from_sources(brand, pdfs, note=note)
    else:
        res = amb.apply_followup(brand, action, note=note, pdf_paths=pdfs,
                                 image_paths=imgs, entry_key=amb.entry_key(note))

    client = slack()
    for it in res.get("artifacts", []):
        try:
            up = client.files_upload_v2(channel=channel, thread_ts=thread,
                                        file=it["path"], title=it["label"])
            fo = up.get("file") or (up.get("files") or [{}])[0]
            if fo.get("permalink"):
                amb.set_artifact_link(brand, it["label"], fo["permalink"])
        except Exception:
            pass
    say(channel, thread, res.get("text", f"*{brand}* — done."))
    return res
