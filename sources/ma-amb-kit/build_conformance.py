#!/usr/bin/env python3
"""
build_conformance.py — C2. Turn Apple's Required Features table into a
machine-checkable matrix: each required feature -> schema(s) -> endpoint(s) ->
fixture(s), so approval-criteria coverage is visible at a glance.

Associations are derived by keyword match against the extracted artifacts and are
labelled as such — where nothing matches, the cell is a gap the integrator owns
(honest: we don't fabricate a link). Reads:
  structural/required-features.json  (from extract_schemas.py, A3)
  amb_schemas_bundle.json            (schema anchors)
  amb_index.json                     (endpoints)
  fixtures/manifest.json             (fixture groups)  [optional]

Outputs: conformance_matrix.json, conformance_checklist.md
"""
import json, os, re, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
_def_index = ROOT / "amb_index.json"
if not _def_index.exists():
    _def_index = Path("/mnt/user-data/uploads/amb_index.json")
INDEX = Path(os.environ.get("AMB_INDEX", str(_def_index)))
BUNDLE = Path(os.environ.get("AMB_BUNDLE", str(ROOT / "amb_schemas_bundle.json")))
RF = ROOT / "structural" / "required-features.json"
FIX_MANIFEST = ROOT / "fixtures" / "manifest.json"

# feature keyword -> (schema-anchor substrings, endpoint path substrings, fixture groups)
# Curated, conservative hints; empty lists mean "no direct spec artifact — integrator owns".
HINTS = {
    "receiving and sending messages": (["http-body", "receivedmessage", "replymessage"], ["/message"], ["text"]),
    "receiving and sending attachments": (["imageitem"], ["/preupload", "/predownload"], []),
    "tapback reactions": ([], [], []),
    "receiving closed conversation messages": ([], ["/message"], ["close-session"]),
    "rich link messages": ([], ["/constructpayload"], []),
    "quick reply messages": (["quick-reply", "quickreply"], ["/message"], ["quick-reply"]),
    "list picker message": (["listpicker", "listpickersection", "listpickeritem"], ["/message"], ["list-picker"]),
    "time picker message": (["timepicker", "event", "locationitem", "timeitem"], ["/message"], ["time-picker"]),
    "apple pay message": (["applepay", "payment"], ["/message", "paymentgateway"], ["apple-pay"]),
    "authentication message": (["authenticate", "oauth"], ["/authenticate"], ["authentication"]),
    "imessage apps": (["interactivedata", "baseinteractivemessage"], ["/message"], []),
    "form message": (["form"], ["/message"], ["form"]),
    "construct payload api": ([], ["/constructpayload"], []),
    "invitation messages": ([], [], []),
    "typing indicator message": (["http-body"], ["/message"], []),
    "routing based on entrypoint parameters": ([], [], []),
    "channel settings and landing page": ([], [], []),
    "device capabilities": ([], [], []),
}

def norm(s): return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()

def main():
    for p, name in [(RF, "required-features.json"), (BUNDLE, "bundle"), (INDEX, "index")]:
        if not p.exists():
            print(f"ABORT: missing {name}: {p}", file=sys.stderr); sys.exit(1)

    features = json.loads(RF.read_text(encoding="utf-8"))["rows"]
    defs = json.loads(BUNDLE.read_text(encoding="utf-8"))["$defs"]
    anchors = list(defs.keys())
    endpoints = json.loads(INDEX.read_text(encoding="utf-8"))["catalogs"]["endpoints"]
    ep_targets = sorted({e["target"] for e in endpoints})
    fixture_groups = {}
    if FIX_MANIFEST.exists():
        fixture_groups = json.loads(FIX_MANIFEST.read_text(encoding="utf-8")).get("by_group", {})

    matrix = []
    for row in features:
        feat = row["feature"]
        key = norm(feat)
        sub_anchors, sub_eps, groups = HINTS.get(key, ([], [], []))
        matched_schemas = sorted({a for a in anchors if any(s in a for s in sub_anchors)})
        matched_eps = sorted({t for t in ep_targets
                              if any(s in t.lower() for s in sub_eps)})
        matched_fixtures = {g: fixture_groups.get(g, 0) for g in groups}
        status = "spec-linked" if (matched_schemas or matched_eps) else "integrator-owned"
        matrix.append({
            "feature": feat,
            "bot_api": row.get("bot_api"),
            "agent_triggered": row.get("agent_triggered"),
            "description": row.get("description"),
            "schemas": matched_schemas,
            "endpoints": matched_eps,
            "fixtures": matched_fixtures,
            "status": status,
        })

    doc = {"generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "source": "Apple Required Features table (canonical L101-124)",
           "note": "Associations are keyword-derived from extracted artifacts, not from an "
                   "explicit Apple mapping. 'integrator-owned' = no direct schema/endpoint "
                   "artifact exists; the integrator must build & demonstrate it for approval.",
           "features": matrix}
    (ROOT / "conformance_matrix.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")

    linked = sum(1 for m in matrix if m["status"] == "spec-linked")
    owned = len(matrix) - linked
    md = ["# AMB Conformance Checklist\n",
          f"_Generated {doc['generated_utc']} from Apple's Required Features table "
          "(canonical L101–124)._\n",
          "Each of Apple's required features mapped to the schema(s), endpoint(s), and "
          "fixture group(s) in this kit. Associations are **keyword-derived** from the extracted "
          "artifacts (not an official Apple mapping); `integrator-owned` rows have no direct spec "
          "artifact and must be built and demonstrated for approval.\n",
          f"- Features: **{len(matrix)}**  ·  spec-linked: **{linked}**  ·  integrator-owned: **{owned}**\n",
          "\n| Feature | Bot/API | Agent | Schemas | Endpoints | Fixtures | Status |",
          "|---|:---:|:---:|---|---|---|---|"]
    for m in matrix:
        sc = "<br>".join(f"`{a}`" for a in m["schemas"][:4]) or "—"
        if len(m["schemas"]) > 4: sc += f"<br>+{len(m['schemas'])-4}"
        ep = "<br>".join(m["endpoints"][:3]) or "—"
        fx = ", ".join(f"{g}({n})" for g, n in m["fixtures"].items() if n) or "—"
        md.append(f"| {m['feature']} | {m['bot_api']} | {m['agent_triggered']} | "
                  f"{sc} | {ep} | {fx} | {m['status']} |")
    md.append("\n## Integrator-owned features (no direct spec artifact)\n")
    for m in matrix:
        if m["status"] == "integrator-owned":
            md.append(f"- **{m['feature']}** — {m['description']}")
    (ROOT / "conformance_checklist.md").write_text("\n".join(md), encoding="utf-8")

    print(f"features:      {len(matrix)}")
    print(f"spec-linked:   {linked}")
    print(f"integrator-owned: {owned}")

if __name__ == "__main__":
    main()
