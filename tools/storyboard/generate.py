"""
Storyboard synthesis — brand review → slide model (Juno/Linq format).

Takes Tool 1's scope.json + doc_model.json (the brand review: use cases + the
Apple features selected for each) and produces a storyboard_model.json laid out as
the submission deck: Cover → Entry points → Signing up & welcome → one slide per
use case → Escalation (HELP) + CSAT → Opt-out. Each step carries a mode
(USER DOES / PAGE DISPLAYS), an optional tag (Apple feature / Requirement / Entry
point — the purple tags), a one-line description, and an iMessage screen. The model
is constrained to the storyboard rules (automated disclosure in the welcome,
framing before rich elements, confirmation after taps, a route to a person,
anything-else before close, out-of-hours). render.py draws it; validate.py checks it.
"""
from __future__ import annotations
import json
import os
import re
from pathlib import Path

MODEL = os.environ.get("AMB_LLM_MODEL", "claude-opus-4-8")

SCREEN_HINT = {
    "nav": "brand name shown in the chat header",
    "bubbles": [{"side": "bot|user", "text": "message copy"}],
    "chips": ["quick reply option", "..."],
    "element": "none|quick_reply|list_picker|time_picker|rich_link|apple_pay|auth",
}
STEP_HINT = {
    "mode": "USER DOES|PAGE DISPLAYS",
    "tag": {"type": "Apple feature|Requirement|Entry point|", "text": "e.g. Quick Reply, Privacy Policy & Terms, Website Messages button"},
    "description": "one sentence: what the user does / what the page displays",
    "screen": SCREEN_HINT,
}


def run(review_dir: str, out_dir: str) -> dict:
    import anthropic
    rev = Path(review_dir)
    scope = json.loads((rev / "scope.json").read_text())
    doc = json.loads((rev / "doc_model.json").read_text()) if (rev / "doc_model.json").exists() else {}
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)

    brand = (scope.get("brand", {}) or {}).get("name") or doc.get("brand", {}).get("name") or "Brand"
    system = (
        "You produce an Apple Messages for Business UX storyboard for Linq's submission, in this "
        "exact deck format (one section per slide): "
        "(1) Entry points, (2) Signing up & starting the chat, (3..N) one slide PER USE CASE from "
        "the brand review, (N+1) Escalation to a human (HELP) + CSAT survey, (N+2) Opt-out (STOP). "
        "Each slide has ordered STEPS. Every step has: mode ('USER DOES' or 'PAGE DISPLAYS'), an "
        "optional tag {type: 'Apple feature'|'Requirement'|'Entry point', text}, a one-sentence "
        "description, and an iMessage screen {nav, bubbles:[{side:'bot'|'user',text}], chips:[], "
        "element}. Tag every step that shows a rich element with the matching Apple feature. "
        "Honor the rules: the welcome message must self-identify as automated and explain HELP + "
        "STOP; put a framing bubble before every rich element; confirm after every tap; include a "
        "route to a person on menus; ask 'anything else' before closing; show an out-of-hours path. "
        "Use ONLY the use cases + features in the brand review; don't invent features or use "
        '"iMessage"/"AMB"/"Apple Chat". Return STRICT JSON: '
        + json.dumps({"brand": brand, "cover": {"summary": "", "use_cases": [{"title": "", "features": []}]},
                      "sections": [{"id": "", "title": "", "description": "", "steps": [STEP_HINT]}]}))
    user = ("BRAND REVIEW — scope.json:\n" + json.dumps(scope, indent=2)
            + "\n\nBRAND REVIEW — doc_model.json (use cases, narrative, features):\n"
            + json.dumps({k: doc.get(k) for k in ("use_cases", "narrative", "entry_points", "flags")}, indent=2)
            + "\n\nProduce the storyboard slide model as strict JSON.")

    client = anthropic.Anthropic()
    resp = client.messages.create(model=MODEL, max_tokens=16000, system=system,
                                  messages=[{"role": "user", "content": user}])
    m = re.search(r"\{.*\}", resp.content[0].text, re.S)
    model = json.loads(m.group(0)) if m else {"brand": brand, "sections": []}
    model.setdefault("brand", brand)
    (out / "storyboard_model.json").write_text(json.dumps(model, indent=2))
    return {"model": MODEL, "brand": brand, "sections": len(model.get("sections", [])),
            "steps": sum(len(s.get("steps", [])) for s in model.get("sections", []))}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("review_dir"); ap.add_argument("out_dir")
    a = ap.parse_args()
    s = run(a.review_dir, a.out_dir)
    print(f"storyboard_model.json ({s['model']}) · {s['sections']} sections · {s['steps']} steps")
