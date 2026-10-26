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
import re
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
    if "readiness" in f: return "readiness_note" if f.endswith(".md") else "readiness_form"
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
    # Internal JSON (scope/shotlist/model) stays on disk for the tools — never shared.
    rows = [{"brand": brand, "stage": stage, "kind": _kind(a), "label": a, "link": None}
            for a in artifacts if not a.lower().endswith(".json")]
    if rows:
        _sb("amb_artifact", rows)

def set_artifact_link(brand: str, label: str, link: str):
    """Fill in the Slack permalink on the artifact row the bot just uploaded."""
    url, key = _sb_cfg()
    if not url:
        return
    import urllib.parse
    q = f"?brand=eq.{urllib.parse.quote(brand)}&label=eq.{urllib.parse.quote(label)}&link=is.null"
    req = urllib.request.Request(
        f"{url}/rest/v1/amb_artifact{q}", data=json.dumps({"link": link}).encode(), method="PATCH",
        headers={"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json", "Prefer": "return=minimal"})
    try:
        urllib.request.urlopen(req)
    except Exception:
        pass

def _artifact_items(d: Path, names: list[str], stage: str) -> list[dict]:
    # Don't upload internal JSON to Slack — only the human-facing artifacts.
    return [{"path": str(d / "output" / n), "label": n, "kind": _kind(n), "stage": stage}
            for n in names if not n.lower().endswith(".json")]


def _venv_py(tool: str) -> str:
    p = TOOLS / tool / ".venv/bin/python"
    return str(p) if p.exists() else sys.executable


def _brand_dir(brand: str) -> Path:
    d = BRANDS / brand.lower().replace(" ", "-")
    (d / "inputs").mkdir(parents=True, exist_ok=True)
    (d / "output").mkdir(parents=True, exist_ok=True)
    return d


# ── Thread ↔ project memory (so a thread stays persistent: a follow-up mention in
#    the same thread resolves the brand without re-naming it). Bot-local JSON. ──
_THREADS = BRANDS / ".threads.json"

def _load_threads() -> dict:
    try:
        return json.loads(_THREADS.read_text())
    except Exception:
        return {}

def thread_brand(channel: str, thread_ts: str) -> str | None:
    return _load_threads().get(f"{channel}:{thread_ts}")

def link_thread(channel: str, thread_ts: str, brand: str):
    m = _load_threads()
    k = f"{channel}:{thread_ts}"
    if m.get(k) != brand:
        m[k] = brand
        BRANDS.mkdir(parents=True, exist_ok=True)
        _THREADS.write_text(json.dumps(m, indent=2))


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
    files = ([p.name for p in (d / "output").glob("brand-approval-*.html")]
             + [p.name for p in (d / "output").glob("*-usecases.pdf")]
             + [p.name for p in (d / "output").glob("*-readiness.pdf")]
             + [p.name for p in (d / "output").glob("readiness-*.md")])
    if ok:
        st = _state(d); st["stage"] = "brand_approval"; _save_state(d, st)
        _log(d, "brand_doc", "generated")
        _record(brand, "brand_approval", "brand_doc", files)
    return {"text": f"*Brand Approval doc — {brand}*\n```{out.strip()[-800:]}```",
            "artifacts": _artifact_items(d, files, "brand_approval"), "ok": ok}


def cmd_storyboard(brand: str, render_only: bool = False) -> dict:
    d = _brand_dir(brand)
    scope = d / "output/scope.json"
    doc = d / "output/doc_model.json"
    flow = d / "inputs/flow.json"
    model = d / "output/storyboard_model.json"
    # Preferred: generate the Juno-format deck from the brand review (Tool 1 output).
    if scope.exists() and doc.exists():
        args = [_venv_py("storyboard"), str(TOOLS / "storyboard/storyboard.py"),
                "--from-review", str(d / "output"), str(d / "output")]
        if render_only and model.exists():
            args.append("--render-only")   # re-render current content (no LLM), visual tweaks only
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
        return {"text": f"*Storyboard — {brand}*\n```{out.strip()[-800:]}```",
                "artifacts": _artifact_items(d, arts, "ux_approval"), "ok": ok}
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
        return {"text": f"*Experience Review — {brand}*\n```{out.strip()[-1000:]}```",
                "artifacts": _artifact_items(d, arts, "experience_review"), "ok": ok}
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


def parse_request(text: str, filenames: list[str]) -> dict:
    """Heuristically pull {brand, action} from a natural-language @mention."""
    t = re.sub(r"<@[^>]+>", "", text or "").strip()  # drop the bot mention
    low = t.lower()
    action = ("review" if "review" in low or "recording" in low else
              "storyboard" if "storyboard" in low or "story board" in low else
              "brand-doc")
    brand = None
    m = re.search(r"\bfor\s+([A-Za-z0-9][\w.\-&' ]{1,40}?)(?:\.|,|\s+(?:use|using|from|with|and)\b|$)", t)
    if m:
        brand = m.group(1).strip()
    if not brand and filenames:
        # e.g. "Superpower- Apple Messages for Business Brand Nomination.pdf" → "Superpower"
        base = re.split(r"[-–—]|messages|apple|brand|use", filenames[0], flags=re.I)[0]
        brand = re.sub(r"\.pdf$", "", base, flags=re.I).strip() or None
    return {"brand": (brand or "unknown").strip(), "action": action}


def download(url: str, dest: str, token: str):
    import urllib.request
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as r, open(dest, "wb") as f:
        f.write(r.read())


def run_from_sources(brand: str, pdf_paths: list[str], note: str = "") -> dict:
    """Mention flow: PDFs → intake → brand-doc → storyboard. Returns combined text + artifacts."""
    d = _brand_dir(brand)
    intake = d / "inputs/intake.json"
    ok, out = _run([_venv_py("brand-doc"), str(TOOLS / "brand-doc/intake_from_sources.py"),
                    brand, str(intake), *pdf_paths, "--note", note], TOOLS / "brand-doc")
    if not ok or not intake.exists():
        return {"text": f"Couldn't read the attachments for *{brand}*.\n```{out[-500:]}```", "artifacts": []}
    r1 = cmd_brand_doc(brand)
    r2 = cmd_storyboard(brand)
    arts = (r1.get("artifacts") or []) + (r2.get("artifacts") or [])
    return {"text": f"*{brand}* — brand doc + storyboard built from the attachments.\n"
                    f"{r2.get('text','')}", "artifacts": arts}


_ENTRY_ALIASES = {"web": "website", "site": "website", "ios": "app", "iphone": "app",
                  "spotlight": "search", "siri": "search", "safari": "search", "suggest": "search",
                  "text message": "sms", "deflect": "ivr", "phone call": "ivr", "invite": "invitation",
                  "apple maps": "maps"}
_ENTRY_KEYS = ["website", "app", "maps", "search", "social", "email", "sms", "qr", "ivr", "invitation"]

def entry_key(text: str) -> str | None:
    """Pull an entry-point type ('iOS app', 'Apple Maps', 'Spotlight') from free text."""
    low = (text or "").lower()
    for phrase, k in _ENTRY_ALIASES.items():
        if phrase in low:
            return k
    for k in _ENTRY_KEYS:
        if k in low:
            return k
    return None


def followup_action(text: str) -> str:
    """Keyword fallback: map an in-thread follow-up to an action (typo-tolerant)."""
    low = re.sub(r"<@[^>]+>", "", text or "").lower()
    if re.search(r"story\s*-?\s*board|scoreboard|storyboard|slide|deck|ux\s*flow|entry\s*point|"
                 r"in\s*place\s*of\s*the\s*phone|mock\s*up|\bimage\b|\bmockup\b|render", low):
        return "storyboard"
    if re.search(r"brand[-\s]?doc|nomination|brand\s*approval", low):
        return "brand-doc"
    if re.search(r"\breview\b|recording|the\s+video|experience\s*review", low):
        return "review"
    if re.search(r"feedback|apple\s+(said|replied|responded|rejected|sent)|rejection", low):
        return "feedback"
    if re.search(r"\bstatus\b|where\s+are\s+we|progress|what'?s\s+(left|next)", low):
        return "status"
    return "unknown"


def interpret_followup(brand: str, text: str, stage: str = "", has_images: bool = False) -> dict:
    """Interpret a free-form in-thread request → {action, entry_key, reply}. Uses the LLM
    for real conversational routing; falls back to keywords with no ANTHROPIC_API_KEY."""
    clean = re.sub(r"<@[^>]+>", "", text or "").strip()
    fallback = {"action": followup_action(clean), "entry_key": entry_key(clean), "reply": ""}
    if fallback["action"] == "unknown" and (fallback["entry_key"] or has_images):
        fallback["action"] = "storyboard"
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return fallback
    try:
        import anthropic
        sysmsg = (
            "You route a teammate's in-thread request about an Apple Messages for Business "
            "storyboard project to ONE action. Actions:\n"
            "- storyboard: (re)generate or re-render the UX storyboard deck. Use for ANYTHING "
            "visual: entry points, phone screens, mockups, images, bubbles, colors, a specific "
            "section/step, 'mock up', 'redo', 'use X in place of the phone'.\n"
            "- brand-doc: regenerate the brand nomination doc / use cases / readiness.\n"
            "- review: run the experience video review.\n"
            "- status: report pipeline status.\n"
            "- feedback: the user is relaying Apple's feedback to log against the rules.\n"
            "- note: just record a comment; no tool run.\n"
            "If the request names an entry-point type, set entry_key to one of "
            "[website, app, maps, search, social, email, sms, qr, ivr, invitation], else null. "
            "reply = one short sentence confirming what you will do, in the first person. "
            'Return STRICT JSON {"action","entry_key","reply"}.')
        usr = f"PROJECT: {brand} (stage: {stage or 'unknown'}). has_images={has_images}.\nMESSAGE: {clean}"
        client = anthropic.Anthropic()
        r = client.messages.create(model=os.environ.get("AMB_LLM_MODEL", "claude-opus-4-8"),
                                   max_tokens=400, system=sysmsg,
                                   messages=[{"role": "user", "content": usr}])
        m = re.search(r"\{.*\}", r.content[0].text, re.S)
        out = json.loads(m.group(0)) if m else {}
        action = out.get("action") if out.get("action") in DISPATCH or out.get("action") in ("feedback", "note") else fallback["action"]
        return {"action": action, "entry_key": out.get("entry_key") or fallback["entry_key"],
                "reply": (out.get("reply") or "").strip()}
    except Exception:
        return fallback


def _refresh_intake(brand: str, pdf_paths: list[str], note: str) -> bool:
    """Rebuild the brand's intake.json from new PDFs; returns True if it succeeded."""
    if not pdf_paths:
        return False
    d = _brand_dir(brand)
    intake = d / "inputs/intake.json"
    ok, _ = _run([_venv_py("brand-doc"), str(TOOLS / "brand-doc/intake_from_sources.py"),
                  brand, str(intake), *pdf_paths, "--note", note], TOOLS / "brand-doc")
    return ok and intake.exists()


def _save_entry_image(brand: str, key: str, image_paths: list[str]) -> bool:
    """Drop the first attached image in as the entry-point override (inputs/entry-<key>.png)."""
    if not (key and image_paths):
        return False
    import shutil
    d = _brand_dir(brand)
    ext = os.path.splitext(image_paths[0])[1].lower() or ".png"
    try:
        shutil.copy(image_paths[0], d / "inputs" / f"entry-{key}{ext}")
        return True
    except Exception:
        return False


def apply_followup(brand: str, action: str, note: str = "", pdf_paths: list[str] | None = None,
                   image_paths: list[str] | None = None, entry_key: str | None = None) -> dict:
    """Run an in-thread follow-up for a known brand. New PDFs refresh the brand review;
    an attached image + an entry type is dropped in as that entry-point's screen; a bare
    visual request re-renders the current deck (no LLM) so approved content is preserved."""
    pdf_paths = pdf_paths or []
    image_paths = image_paths or []
    d = _brand_dir(brand)
    if action == "review":
        return cmd_review(brand)
    if action == "feedback":
        return cmd_feedback(brand, note)
    if action == "status":
        return cmd_status(brand)
    if action == "brand-doc":
        _refresh_intake(brand, pdf_paths, note)
        return cmd_brand_doc(brand)
    if action == "storyboard":
        used_image = _save_entry_image(brand, entry_key, image_paths)
        arts = []
        refreshed = _refresh_intake(brand, pdf_paths, note)
        if refreshed:
            arts += cmd_brand_doc(brand).get("artifacts", [])     # new content → refresh scope/doc_model
        # Visual-only change (dropped image / entry / bubble tweak, no new PDFs) → cheap re-render.
        render_only = not refreshed and (d / "output/storyboard_model.json").exists()
        rs = cmd_storyboard(brand, render_only=render_only)
        note_bits = []
        if used_image:
            note_bits.append(f"used your image for the *{entry_key}* entry point")
        elif entry_key:
            note_bits.append(f"the *{entry_key}* entry point now shows the real AMB entry screen")
        extra = (" — " + "; ".join(note_bits)) if note_bits else ""
        return {"text": rs.get("text", "") + extra, "artifacts": arts + rs.get("artifacts", []), "ok": rs.get("ok")}
    # unknown intent: new PDFs → full rebuild; otherwise log the note as feedback on the project.
    if pdf_paths:
        return run_from_sources(brand, pdf_paths, note)
    _log(d, "note", note[:200])
    try:
        _record(brand, (_state(d).get("stage") or "brand_approval"), "note", [])
    except Exception:
        pass
    return {"text": f"Noted on *{brand}*. I can `re-do the storyboard`, `update the brand doc`, or "
                    f"`run the review` for this project — just say which (right here in the thread)."}


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
