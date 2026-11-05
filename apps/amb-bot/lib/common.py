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
import re
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


ATTACH_EXT = (".pdf", ".png", ".jpg", ".jpeg")


def fetch_thread(channel, thread_ts):
    """Read the ENTIRE thread: every message's text + every PDF/image attachment,
    not just the triggering message. Needs channels:history / groups:history on the
    bot token; degrades to ([], "") if the scope is missing."""
    if not (channel and thread_ts):
        return [], ""
    try:
        msgs = slack().conversations_replies(channel=channel, ts=thread_ts, limit=200).get("messages", [])
    except Exception:
        return [], ""
    files, texts, seen = [], [], set()
    for m in msgs:
        t = re.sub(r"<@[^>]+>", "", m.get("text", "")).strip()
        if t:
            texts.append(t)
        for f in (m.get("files") or []):
            fid = f.get("id") or f.get("url_private")
            name = f.get("name", "")
            if fid not in seen and name.lower().endswith(ATTACH_EXT):
                seen.add(fid)
                files.append({"name": name, "url": f.get("url_private_download") or f.get("url_private")})
    return files, "\n".join(texts)


def _dedup_files(files):
    out, seen = [], set()
    for f in files:
        key = f.get("name") or f.get("url")
        if key and key not in seen:
            seen.add(key)
            out.append(f)
    return out


# ── Build (reuses amb.py), thread-aware + conversational ──
def run_job(job: dict) -> dict:
    import amb
    channel, thread = job.get("channel"), job.get("thread_ts")
    note = job.get("note") or ""

    # 1. Pull context from the whole thread (attachments posted in earlier messages too).
    tfiles, thread_text = fetch_thread(channel, thread)
    allfiles = _dedup_files((job.get("files") or []) + tfiles)
    pdf_names = [f["name"] for f in allfiles if f["name"].lower().endswith(".pdf")]
    has_pdfs = bool(pdf_names)
    has_images = any(f["name"].lower().endswith((".png", ".jpg", ".jpeg")) for f in allfiles)

    # 2. Resolve the brand: the thread's remembered project, else the explicit "for X".
    brand = (job.get("brand") or "").strip()
    if brand in ("", "unknown"):
        brand = amb.thread_brand(channel, thread) or amb.parse_request(note, pdf_names)["brand"]

    # 3. Interpret the request against the WHOLE thread.
    stage = ""
    if brand not in ("", "unknown"):
        try:
            stage = (amb._state(amb._brand_dir(brand)) or {}).get("stage") or ""
        except Exception:
            pass
    decision = amb.interpret_followup(brand, note, stage=stage, has_images=has_images,
                                      has_pdfs=has_pdfs, thread_text=thread_text)
    action, ekey, reply = decision["action"], decision.get("entry_key"), decision.get("reply")

    # 4. If we still can't tell the brand, or the model wants to ask — converse, don't fail.
    if brand == "unknown" or action == "ask":
        say(channel, thread, reply or "Which brand is this? And can you attach the brand PDFs "
            "(nomination / use cases) here in the thread so I can build it?")
        return {"text": reply or "asked for clarification"}

    amb.link_thread(channel, thread, brand)

    # 5. Download every gathered file into the brand's inputs.
    d = amb._brand_dir(brand)
    pdfs, imgs = [], []
    for f in allfiles:
        dest = d / "inputs" / f["name"]
        try:
            amb.download(f["url"], str(dest), SLACK_BOT_TOKEN)
            (pdfs if f["name"].lower().endswith(".pdf") else imgs).append(str(dest))
        except Exception:
            pass

    # 6. Route. PDFs + no existing review → full build (doc + storyboard) from the PDFs.
    has_review = (d / "output/scope.json").exists() and (d / "output/doc_model.json").exists()
    if action == "build" or (action in ("storyboard", "brand-doc") and pdfs and not has_review):
        if pdfs:
            res = amb.run_from_sources(brand, pdfs, note=note)
        elif has_review:
            res = amb.apply_followup(brand, "storyboard", note=note)
        else:
            res = {"text": f"I'd love to build *{brand}*, but I don't see any brand PDFs in this "
                           f"thread yet — drop in the nomination / use-case PDFs and I'll take it from there.",
                   "artifacts": []}
    else:
        res = amb.apply_followup(brand, action, note=note, pdf_paths=pdfs, image_paths=imgs, entry_key=ekey)

    # 7. Upload artifacts + reply in the thread.
    client = slack()
    for it in res.get("artifacts", []):
        try:
            up = client.files_upload_v2(channel=channel, thread_ts=thread, file=it["path"], title=it["label"])
            fo = up.get("file") or (up.get("files") or [{}])[0]
            if fo.get("permalink"):
                amb.set_artifact_link(brand, it["label"], fo["permalink"])
        except Exception:
            pass
    say(channel, thread, res.get("text") or reply or f"*{brand}* — done.")
    return res
