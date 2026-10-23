#!/usr/bin/env python3
"""
AMB command dispatcher — the logic behind the Slack bot, callable from the CLI too.

    python amb.py <brand-doc|storyboard|review|feedback|status> <brand> [args]

Each brand has a folder: brands/<brand>/{inputs,output}/ + state.json. The three
run-commands shell out to each tool's own venv/orchestrator and write artifacts to
the brand's output folder (which the pipeline board also reads). status reports the
pipeline position; feedback splits an Apple reply into rule-matched items (the
rule-set feedback loop). Slack wiring is in bot.py; this module has no Slack deps.
"""
from __future__ import annotations
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
BRANDS = REPO / "brands"
TOOLS = REPO / "tools"

STAGES = ["brand_approval", "ux_approval", "experience_review", "launch"]

# ── Supabase (shared pipeline state the board reads). Best-effort: no env = skip. ──
import urllib.request  # noqa: E402

def _sb_cfg():
    url = os.environ.get("NEXT_PUBLIC_SUPABASE_URL") or os.environ.get("SUPABASE_URL")
    return (url, os.environ.get("SUPABASE_SERVICE_ROLE_KEY")) if (url and os.environ.get("SUPABASE_SERVICE_ROLE_KEY")) else (None, None)

def _sb(path: str, rows, params: str = ""):
    url, key = _sb_cfg()
    if not url:
        return
    req = urllib.request.Request(
        f"{url}/rest/v1/{path}{params}", data=json.dumps(rows).encode(), method="POST",
        headers={"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json",
                 "Prefer": "resolution=merge-duplicates,return=minimal"})
    try:
        urllib.request.urlopen(req)
    except Exception:
        pass  # board state is best-effort; local run still succeeds

def _kind(fname: str) -> str:
    f = fname.lower()
    if "usecases" in f: return "usecases_form"
    if "readiness-" in f or f.startswith("readiness"): return "readiness_note" if f.endswith(".md") else "readiness_form"
    if "brand-approval" in f: return "doc"
    if "storyboard" in f: return "storyboard"
    if "shotlist" in f: return "shotlist"
    if "timestamp-index" in f: return "timestamp_index"
    if "review-" in f or f == "review.json": return "review"
    if f == "scope.json": return "scope"
    return "artifact"

def _record(brand: str, stage: str, action: str, artifacts: list[str]):
    now = datetime.now(timezone.utc).isoformat()
    _sb("amb_brand", [{"name": brand, "stage": stage, "stage_entered_at": now, "updated_at": now}], "?on_conflict=name")
    _sb("amb_event", [{"brand": brand, "action": action}])
    rows = [{"brand": brand, "stage": stage, "kind": _kind(a), "label": a, "link": None} for a in artifacts]
    if rows:
        _sb("amb_artifact", rows)


def _venv_py(tool: str) -> str:
    p = TOOLS / tool / ".venv/bin/python"
    return str(p) if p.exists() else sys.executable


def _brand_dir(brand: str) -> Path:
    d = BRANDS / brand.lower().replace(" ", "-")
    (d / "inputs").mkdir(parents=True, exist_ok=True)
    (d / "output").mkdir(parents=True, exist_ok=True)
    return d


def _state(d: Path) -> dict:
    f = d / "state.json"
    return json.loads(f.read_text()) if f.exists() else {"stage": None, "events": []}


def _save_state(d: Path, st: dict):
    (d / "state.json").write_text(json.dumps(st, indent=2))


def _log(d: Path, action: str, detail: str = ""):
    st = _state(d)
    st["events"].append({"at": datetime.now(timezone.utc).isoformat(), "action": action, "detail": detail})
    _save_state(d, st)


def _run(cmd: list[str], cwd: Path) -> tuple[bool, str]:
    r = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr)[-3000:]


def cmd_brand_doc(brand: str) -> dict:
    d = _brand_dir(brand)
    intake = d / "inputs/intake.json"
    if not intake.exists():
        return {"text": f"No intake for *{brand}*. Drop `intake.json` in the thread (brand facts + 4 use cases) and re-run."}
    ok, out = _run([_venv_py("brand-doc"), str(TOOLS / "brand-doc/brand_doc.py"), str(intake), str(d / "output")],
                   TOOLS / "brand-doc")
    files = [p.name for p in (d / "output").glob("*.html")] + [p.name for p in (d / "output").glob("*.pdf")]
    if ok:
        st = _state(d); st["stage"] = "brand_approval"; _save_state(d, st)
        _log(d, "brand_doc", "generated")
        _record(brand, "brand_approval", "brand_doc", files)
    return {"text": f"*Brand Approval doc — {brand}*\n```{out.strip()[-800:]}```", "files": files, "ok": ok}


def cmd_storyboard(brand: str) -> dict:
    d = _brand_dir(brand)
    scope = d / "output/scope.json"
    doc = d / "output/doc_model.json"
    flow = d / "inputs/flow.json"
    # Preferred: generate the Juno-format deck from the brand review (Tool 1 output).
    if scope.exists() and doc.exists():
        args = [_venv_py("storyboard"), str(TOOLS / "storyboard/storyboard.py"),
                "--from-review", str(d / "output"), str(d / "output")]
    elif flow.exists():
        args = [_venv_py("storyboard"), str(TOOLS / "storyboard/storyboard.py"), str(flow), str(d / "output")]
        if scope.exists():
            args += ["--scope", str(scope)]
    else:
        return {"text": f"No brand review or flow for *{brand}*. Run `/amb brand-doc {brand}` first "
                        f"(the storyboard is generated from the use cases), or attach a `flow.json`."}
    ok, out = _run(args, TOOLS / "storyboard")
    if ok:
        st = _state(d); st["stage"] = "ux_approval"; _save_state(d, st); _log(d, "storyboard", "generated")
        arts = [p.name for p in (d / "output").glob("storyboard-*.html")] + [p.name for p in (d / "output").glob("shotlist-*.json")]
        _record(brand, "ux_approval", "storyboard", arts)
    return {"text": f"*Storyboard — {brand}*\n```{out.strip()[-800:]}```", "ok": ok}


def cmd_review(brand: str) -> dict:
    d = _brand_dir(brand)
    rec = next((p for p in (d / "inputs").glob("*.mp4")), None) or next((p for p in (d / "inputs").glob("*.mov")), None)
    if not rec:
        return {"text": f"No recording for *{brand}*. Upload the .mp4/.mov to the thread and re-run."}
    args = [_venv_py("video-review"), str(TOOLS / "video-review/review.py"), str(rec), str(d / "output" / "review")]
    ok, out = _run(args, TOOLS / "video-review")
    if ok:
        st = _state(d); st["stage"] = "experience_review"; _save_state(d, st); _log(d, "review", rec.name)
        rv = d / "output" / "review"
        arts = [f"review/{p.name}" for p in rv.glob("review-*")] + [f"review/{p.name}" for p in rv.glob("timestamp-index-*")]
        _record(brand, "experience_review", "review", arts or ["review.json"])
    return {"text": f"*Experience Review — {brand}*\n```{out.strip()[-1000:]}```", "ok": ok}


def cmd_status(brand: str) -> dict:
    d = _brand_dir(brand)
    st = _state(d)
    outs = sorted(p.name for p in (d / "output").rglob("*") if p.is_file())
    stage = st.get("stage") or "not started"
    last = st["events"][-1] if st.get("events") else None
    lines = [f"*{brand}* — stage: `{stage}`"]
    if last:
        lines.append(f"last: {last['action']} ({last['at'][:16]})")
    lines.append(f"artifacts: {', '.join(outs) if outs else 'none'}")
    nxt = {None: "run `/amb brand-doc`", "brand_approval": "send to Apple, then `/amb storyboard`",
           "ux_approval": "record the experience, then `/amb review`",
           "experience_review": "fix Fails, resubmit; then Launch SOP"}.get(st.get("stage"), "—")
    lines.append(f"next: {nxt}")
    return {"text": "\n".join(lines)}


def cmd_feedback(brand: str, text: str) -> dict:
    """Split an Apple reply into items + propose rule matches (AE confirms in Slack)."""
    if not text.strip():
        return {"text": "Paste Apple's feedback after the command."}
    d = _brand_dir(brand)
    try:
        import anthropic  # noqa
        from pathlib import Path as _P
        rules = json.loads((REPO / "packages/rules/rules.json").read_text())["rules"]
        catalog = "\n".join(f'{r["id"]} [{(r.get("letter_ids") or [""])[0]}]: {r["name"]}' for r in rules)
        client = anthropic.Anthropic()
        sysmsg = ("Split this Apple feedback into discrete items. For each, propose the single best "
                  "matching rule id from the catalog (or null if none — a candidate new rule). "
                  'Return STRICT JSON {"items":[{"apple_text","proposed_rule_id","timestamp_or_null"}]}.')
        resp = client.messages.create(model=os.environ.get("AMB_LLM_MODEL", "claude-opus-4-8"),
                                      max_tokens=2000, system=sysmsg,
                                      messages=[{"role": "user", "content": f"CATALOG:\n{catalog}\n\nFEEDBACK:\n{text}"}])
        import re
        m = re.search(r"\{.*\}", resp.content[0].text, re.S)
        items = json.loads(m.group(0))["items"] if m else []
        (d / "output/feedback-proposed.json").write_text(json.dumps(items, indent=2))
        _log(d, "feedback", f"{len(items)} items")
        body = "\n".join(f"• {it['apple_text'][:80]} → `{it.get('proposed_rule_id') or 'NEW'}`" for it in items)
        return {"text": f"*Apple feedback — {brand}* ({len(items)} items; react ✅ to confirm each)\n{body}"}
    except Exception as e:
        return {"text": f"feedback parse unavailable ({e}). Needs ANTHROPIC_API_KEY."}


DISPATCH = {"brand-doc": cmd_brand_doc, "storyboard": cmd_storyboard, "review": cmd_review, "status": cmd_status}


def dispatch(sub: str, brand: str, extra: str = "") -> dict:
    if sub == "feedback":
        return cmd_feedback(brand, extra)
    fn = DISPATCH.get(sub)
    if not fn:
        return {"text": f"Unknown command `{sub}`. Use: brand-doc | storyboard | review | feedback | status"}
    return fn(brand)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: amb.py <brand-doc|storyboard|review|feedback|status> <brand> [text]")
        sys.exit(1)
    res = dispatch(sys.argv[1], sys.argv[2], " ".join(sys.argv[3:]))
    print(res["text"])
    if res.get("files"):
        print("files:", res["files"])
