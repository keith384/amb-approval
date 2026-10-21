"""
Tool 1 synthesis — intake → doc model + scope.

Takes brand facts + the four use cases (in the customer's words; optionally a
kick-off transcript) and produces: (1) a doc_model.json with the Walmart-shape
narrative prose + per-use-case archetype + feature fit + flags, and (2) the
canonical scope.json that fill_forms.py and Tools 2/3 consume. The model is
constrained to MA's five archetypes and the Standards feature inventory; it
classifies and writes prose but never invents Apple features or claims. The
terminology lint + open-question audit run on the output in build_doc.py.
"""
from __future__ import annotations
import json
import os
import re
from pathlib import Path

MODEL = os.environ.get("AMB_LLM_MODEL", "claude-opus-4-8")

ARCHETYPES = ["find_and_choose", "book_and_manage", "check_and_resolve",
              "enrol_and_receive", "reach_a_person"]
FEATURES = ["quick_reply", "list_picker", "time_picker", "rich_link",
            "apple_pay", "authentication", "forms", "attachments"]

SCHEMA_HINT = {
    "brand": {"name": "", "requested_date": "", "define_success": "",
              "founded": "", "hq": "", "headcount": "", "financials": ""},
    "use_cases": [{"title": "", "sentence": "", "archetype": "one of " + "|".join(ARCHETYPES),
                   "features": ["subset of " + "|".join(FEATURES)], "description": ""}],
    "narrative": {"use_case_para": "", "experience": "", "why_it_fits": "",
                  "value_to_users": "", "value_to_society": ""},
    "features_table": [{"feature": "", "how_used": ""}],
    "entry_points": ["app_messages_button|web_messages_button|qr_code|message_suggest|ivr_deflect|apple_maps|social_media"],
    "flags": {"pre_approval": ["use cases needing Apple pre-approval, if any"],
              "consumer_ai_pause": "note if AI is the product not the channel, else empty"},
    "scope": {"brand": {"name": "", "requested_date": "", "define_success": ""},
              "entry_point": {}, "global": {}, "usecase": {}, "readiness": {},
              "enhanced_features": {}, "live_agent": True, "out_of_hours": True},
}


KNOWN_EPS = {"app_messages_button", "web_messages_button", "qr_code", "message_suggest",
             "ivr_deflect", "apple_maps", "social_media"}
# doc-model feature name → form scope key (Apple uses "form", "rich_link")
FEAT_TO_SCOPEKEY = {"quick_reply": "quick_reply", "list_picker": "list_picker",
                    "time_picker": "time_picker", "rich_link": "rich_link",
                    "apple_pay": "apple_pay", "attachments": "attachments", "forms": "form"}


def build_scope(intake: dict, model: dict) -> dict:
    """Deterministically assemble scope to match form-field-map maps_to keys (so the
    AcroForm filler and Tools 2/3 get aligned data), driven by the LLM's classification."""
    ib = intake.get("brand", {})
    cb = intake.get("company_background", {})
    ucs = model.get("use_cases", [])
    all_feat = set()
    usecase = {}
    for i, uc in enumerate(ucs, 1):
        entry = {"description": uc.get("description") or uc.get("sentence") or ""}
        for f in uc.get("features", []):
            all_feat.add(f)
            key = FEAT_TO_SCOPEKEY.get(f)
            if key:
                entry[key] = True
        usecase[str(i)] = entry
    return {
        "brand": {"name": ib.get("name", ""), "requested_date": ib.get("requested_date", ""),
                  "define_success": ib.get("define_success", "")},
        "entry_point": {ep: True for ep in intake.get("entry_points", []) if ep in KNOWN_EPS},
        "global": {"automated_welcome": True, "csat_survey": True,
                   "authentication": "authentication" in all_feat},
        "usecase": usecase,
        "readiness": {
            "brand_name": ib.get("name", ""),
            "industry_vertical": intake.get("industry_vertical") or ib.get("vertical", ""),
            "country_hq": cb.get("hq", ""), "country_coverage": intake.get("country_coverage", ""),
            "current_msp": ib.get("existing_agent", ""),
        },
        "enhanced_features": {f: (f in all_feat) for f in FEATURES},
        "live_agent": True, "out_of_hours": True,
    }


def run(intake_path: str, out_dir: str) -> dict:
    import anthropic
    intake = json.loads(Path(intake_path).read_text())
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)

    system = (
        "You prepare Apple Messages for Business brand-approval submissions for Linq (the MSP). "
        "From the brand facts and use cases, produce the submission doc model and scope. "
        f"Classify each use case into exactly one archetype ({', '.join(ARCHETYPES)}) and map it to "
        f"a subset of the Standards feature inventory ({', '.join(FEATURES)}). Write the narrative "
        "prose in Apple's required shape (use case; the experience; why it fits — naming the feature "
        "for each step; value to users; value to society). NEVER invent Apple features, metrics, or "
        "claims; leave unknown facts as empty strings (they become open questions). NEVER use "
        '"iMessage", "AMB", "Apple Chat", or exclusivity/endorsement wording. Also fill the scope '
        "object: scope.enhanced_features is the union of features across use cases (true/false for "
        f"each of {FEATURES}); scope.usecase.N.<feature>=true for features that use case uses; "
        "scope.entry_point.<name>=true for entry points in use; scope.brand mirrors brand. "
        "Return STRICT JSON matching this shape (no prose outside JSON):\n"
        + json.dumps(SCHEMA_HINT))
    user = ("BRAND FACTS + USE CASES (intake):\n" + json.dumps(intake, indent=2)
            + "\n\nProduce the doc model + scope as strict JSON.")

    client = anthropic.Anthropic()
    resp = client.messages.create(model=MODEL, max_tokens=4000, system=system,
                                  messages=[{"role": "user", "content": user}])
    m = re.search(r"\{.*\}", resp.content[0].text, re.S)
    model = json.loads(m.group(0)) if m else {}

    (out / "doc_model.json").write_text(json.dumps(model, indent=2))
    scope = build_scope(intake, model)   # deterministic, key-aligned to the forms
    (out / "scope.json").write_text(json.dumps(scope, indent=2))
    return {"model": MODEL, "use_cases": len(model.get("use_cases", [])),
            "features": sorted(k for k, v in (scope.get("enhanced_features") or {}).items() if v),
            "flags": model.get("flags", {})}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("intake"); ap.add_argument("out_dir")
    a = ap.parse_args()
    s = run(a.intake, a.out_dir)
    print(f"generated doc_model.json + scope.json ({s['model']})")
    print(f"  use cases: {s['use_cases']} · features in scope: {s['features']}")
    if s["flags"].get("pre_approval"):
        print(f"  ⚠ pre-approval flags: {s['flags']['pre_approval']}")
