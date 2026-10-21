#!/usr/bin/env python3
"""
validate_fixtures.py — C1 harness. Validate each extracted fixture against its
Gap #1 schema (resolved from amb_schemas_bundle.json), and report pass/fail.

Schema selection is deterministic and conservative: envelope payloads (sourceId +
destinationId + type) validate against `http-body`; section-named dictionaries map
to their anchor; anything without a confident mapping is reported as "no-mapping"
(not a failure — we don't guess a schema). A fixture that maps and fails is a real
signal (schema bug or a payload that violates a stated required field).

Outputs: fixtures_validation.md   (non-zero exit only on harness error)
"""
import json, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIX_DIR = ROOT / "fixtures"
BUNDLE = Path(os.environ.get("AMB_BUNDLE", str(ROOT / "amb_schemas_bundle.json")))

SECTION_ANCHOR = {
    "replymessage dictionary": "replymessage-dictionary",
    "imageitem dictionary": "imageitem-dictionary",
    "payment dictionary": "payment-dictionary",
    "payment method dictionary": "payment-method-dictionary",
    "data.authenticate dictionary": "data-authenticate-dictionary",
}

def pick_anchor(fix, defs):
    obj = fix["obj"]
    sect = fix["section"].lower()
    # section-named dictionary mapping only applies to object fixtures
    if isinstance(obj, dict) and sect in SECTION_ANCHOR and SECTION_ANCHOR[sect] in defs:
        return SECTION_ANCHOR[sect]
    # envelope mapping requires the FULL send-request envelope, not a fragment
    if isinstance(obj, dict) and {"sourceId", "destinationId", "type"} <= set(obj.keys()):
        return "http-body"
    return None

def main():
    if not BUNDLE.exists():
        print(f"ABORT: bundle not found: {BUNDLE}", file=sys.stderr); sys.exit(1)
    bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))
    defs = bundle["$defs"]
    bundle_uri = bundle["$id"]

    try:
        from jsonschema import Draft202012Validator
        from referencing import Registry, Resource
        resource = Resource.from_contents(bundle)
        registry = Registry().with_resource(uri=bundle_uri, resource=resource)
    except Exception as e:
        print(f"ABORT: cannot init validator: {e}", file=sys.stderr); sys.exit(1)

    manifest = json.loads((FIX_DIR / "manifest.json").read_text(encoding="utf-8"))
    fixtures = [f for f in manifest["fixtures"] if f["status"] == "ok"]

    results = {"pass": [], "fail": [], "no_mapping": []}
    for f in fixtures:
        path = FIX_DIR / f["group"] / f'{f["slug"]}.json'
        if not path.exists():
            continue
        f["obj"] = json.loads(path.read_text(encoding="utf-8"))
        anchor = pick_anchor(f, defs)
        if not anchor:
            results["no_mapping"].append(f["slug"])
            continue
        schema = {"$ref": f"{bundle_uri}#/$defs/{anchor}"}
        validator = Draft202012Validator(schema, registry=registry)
        errs = sorted(validator.iter_errors(f["obj"]), key=lambda e: list(e.path))
        if errs:
            results["fail"].append((f["slug"], anchor,
                                    [f"{list(e.path)}: {e.message[:80]}" for e in errs[:3]]))
        else:
            results["pass"].append((f["slug"], anchor))

    total = len(results["pass"]) + len(results["fail"]) + len(results["no_mapping"])
    md = ["# AMB Fixtures — Validation Report\n",
          f"_Validated {total} fixtures against the schema bundle._\n",
          f"- **Pass:** {len(results['pass'])}\n"
          f"- **Fail:** {len(results['fail'])}\n"
          f"- **No confident schema mapping (skipped, not a failure):** {len(results['no_mapping'])}\n",
          "\n## Passing (fixture -> schema)\n"]
    for slug, anchor in results["pass"]:
        md.append(f"- `{slug}` -> `{anchor}`")
    md.append("\n## Failing\n")
    md.append("_A failure here means a fixture that maps to a schema violates it — usually a "
              "genuine **spec-vs-example discrepancy** in Apple's docs (e.g. worked examples "
              "that omit a field the table marks REQUIRED), not a schema bug. Worth an integrator's attention._\n")
    if results["fail"]:
        for slug, anchor, errs in results["fail"]:
            md.append(f"- `{slug}` -> `{anchor}`")
            for e in errs:
                md.append(f"  - {e}")
    else:
        md.append("_None — every mapped fixture validates against its schema._")
    md.append("\n## No mapping (sub-fragments or need a human to assign a schema)\n")
    md.append(", ".join(f"`{s}`" for s in results["no_mapping"]) or "_None._")
    (ROOT / "fixtures_validation.md").write_text("\n".join(md), encoding="utf-8")

    print(f"fixtures validated: {total}")
    print(f"  pass:       {len(results['pass'])}")
    print(f"  fail:       {len(results['fail'])}")
    print(f"  no-mapping: {len(results['no_mapping'])}")
    for slug, anchor, errs in results["fail"][:5]:
        print(f"   FAIL {slug} -> {anchor}: {errs[0] if errs else ''}")

if __name__ == "__main__":
    main()
