#!/usr/bin/env python3
"""
Tool 2 (UX Storyboard) — orchestrator.

    python storyboard.py <flow.json> <out_dir> [--scope scope.json]

Validates the authored flow against the storyboard rules, renders the iPhone-frame
storyboard (HTML; browser print-to-PDF), runs the Standards 2.18 self-check
(coverage of the scope's enhanced features), and emits shotlist.json (ordered steps
+ the checklist Refs each should evidence) which Tool 3 reads to know what the
video must show. The Slack `/amb storyboard` calls this.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

import render
import validate

FEATURE_KIND = {"quick_reply": "quick_reply", "list_picker": "list_picker",
                "time_picker": "time_picker", "rich_link": "rich_link",
                "apple_pay": "apple_pay", "authentication": "auth"}


def self_check(flow_data: dict, scope: dict) -> list[str]:
    kinds_present = {s["kind"] for steps in flow_data.get("flows", {}).values() for s in steps}
    out = []
    for feat, in_scope in (scope.get("enhanced_features") or {}).items():
        if not in_scope:
            continue
        kind = FEATURE_KIND.get(feat)
        if kind and kind in kinds_present:
            out.append(f"✓ {feat}: shown in the storyboard")
        elif kind:
            out.append(f"✗ {feat}: in scope but NOT in the storyboard — add a step or drop from scope")
        else:
            out.append(f"• {feat}: no dedicated frame kind (verify in the build)")
    return out or ["(no scope provided — coverage not checked)"]


def shotlist(flow_data: dict) -> list[dict]:
    rows = []
    for fkey, steps in flow_data.get("flows", {}).items():
        for i, s in enumerate(steps, 1):
            rows.append({"flow": fkey, "step": i, "actor": s.get("actor"), "kind": s["kind"],
                         "copy": s.get("copy", "")[:80], "evidence_refs": render.refs_for(s)})
    return rows


def model_shotlist(model: dict) -> list[dict]:
    rows = []
    for s in model.get("sections", []):
        for i, st in enumerate(s.get("steps", []), 1):
            tag = st.get("tag") or {}
            rows.append({"section": s.get("id") or s.get("title"), "step": i,
                         "mode": st.get("mode"), "tag": tag.get("text"),
                         "element": (st.get("screen") or {}).get("element"),
                         "copy": " ".join(b.get("text", "") for b in (st.get("screen") or {}).get("bubbles", []) or [])[:80]})
    return rows


def run_from_review(review_dir: str, out_dir: str):
    """Review-driven path: brand review (scope + doc_model) -> Juno-format deck."""
    import json as _json
    import generate, render_deck, validate as _v
    g = generate.run(review_dir, out_dir)
    out = Path(out_dir)
    model = _json.loads((out / "storyboard_model.json").read_text())
    brand = (model.get("brand", "brand")).lower().replace(" ", "-")
    (out / f"storyboard-{brand}.html").write_text(render_deck.render_html(model))
    (out / f"shotlist-{brand}.json").write_text(_json.dumps({"brand": brand, "steps": model_shotlist(model)}, indent=2))
    issues = _v.validate_model(model)
    print(f"storyboard-{brand}.html · {g['sections']} slides · {g['steps']} steps ({g['model']})")
    print(f"validation: {sum(i['severity']=='blocker' for i in issues)} blocker(s), {sum(i['severity']=='warn' for i in issues)} warning(s)")
    for i in issues:
        print(f"  {i['severity'].upper():7} [{i['flow']}:{i['step']}] ({i['rule']}) {i['msg']}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("flow", nargs="?"); ap.add_argument("out_dir")
    ap.add_argument("--scope", default=None)
    ap.add_argument("--from-review", default=None, help="brand-review dir (scope.json + doc_model.json) → generate the deck")
    a = ap.parse_args()
    if a.from_review:
        return run_from_review(a.from_review, a.out_dir)
    out = Path(a.out_dir); out.mkdir(parents=True, exist_ok=True)
    flow_data = json.loads(Path(a.flow).read_text())
    scope = json.loads(Path(a.scope).read_text()) if a.scope and Path(a.scope).exists() else {}
    brand = (flow_data.get("brand", "brand")).lower().replace(" ", "-")

    issues = validate.validate(flow_data)
    blockers = [i for i in issues if i["severity"] == "blocker"]
    warns = [i for i in issues if i["severity"] == "warn"]
    by_key = {}
    for i in blockers:
        by_key.setdefault(f"{i['flow']}:{i['step']}", []).append(f"({i['rule']}) {i['msg']}")

    checks = self_check(flow_data, scope)
    html_doc = render.render_html(flow_data, by_key, checks)
    (out / f"storyboard-{brand}.html").write_text(html_doc)
    sl = shotlist(flow_data)
    (out / f"shotlist-{brand}.json").write_text(json.dumps({"brand": brand, "steps": sl}, indent=2))

    print(f"storyboard-{brand}.html · {len(sl)} steps · shotlist-{brand}.json")
    print(f"validation: {len(blockers)} blocker(s), {len(warns)} warning(s)")
    for i in blockers:
        print(f"  BLOCKER [{i['flow']}:{i['step']}] ({i['rule']}) {i['msg']}")
    for i in warns:
        print(f"  warn    [{i['flow']}:{i['step']}] ({i['rule']}) {i['msg']}")
    print("Standards 2.18 self-check:")
    for c in checks:
        print("  " + c)
    return 0


if __name__ == "__main__":
    sys.exit(main())
