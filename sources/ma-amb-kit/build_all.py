#!/usr/bin/env python3
"""
build_all.py — One command to regenerate every ancillary artifact from the canonical.

Runs, in order, with CONSISTENT paths so the FRESH index feeds downstream steps:
  1) build_index.py        -> amb_index.json
  2) extract_schemas.py    -> schemas/, structural/, amb_schemas_bundle.json, schema_coverage_report.md
  3) build_openapi.py      -> amb.openapi.json
  4) generate_reference.py -> AMB_Schemas_Reference.md

The canonical path is a single argument (default: the uploads copy) threaded to every
step via env vars. Each step self-validates and exits non-zero on failure; this
orchestrator aborts on the first failure and prints a summary with counts, validation
status, and coverage deltas vs the previous build.

Usage:
  python3 build_all.py [/path/to/AMB_Layer2_Canonical_v7_0.md]
"""
import os, sys, json, subprocess, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# Prefer the kit's own canonical (carries the C4 ligature fix); fall back to uploads.
_kit_canon = ROOT / "AMB_Layer2_Canonical_v7_0.md"
_default_canon = _kit_canon if _kit_canon.exists() else \
    Path("/mnt/user-data/uploads/AMB_Layer2_Canonical_v7_0.md")
CANONICAL = Path(sys.argv[1]) if len(sys.argv) > 1 else _default_canon
INDEX  = ROOT / "amb_index.json"
BUNDLE = ROOT / "amb_schemas_bundle.json"

ENV = {**os.environ,
       "AMB_CANONICAL": str(CANONICAL),
       "AMB_INDEX":     str(INDEX),
       "AMB_BUNDLE":    str(BUNDLE)}

# Dependency-ordered: fixtures BEFORE schemas (schemas consume type_enrichments.json);
# validate + conformance AFTER schemas; reference LAST (renders the finished bundle).
STEPS = [
    "build_index.py",            # -> amb_index.json
    "extract_fixtures.py",       # -> fixtures/, type_enrichments.json
    "extract_schemas.py",        # -> schemas/, structural/, bundle, coverage (uses enrichments)
    "validate_fixtures.py",      # -> fixtures_validation.md (fixtures vs fresh schemas)
    "build_openapi.py",          # -> amb.openapi.json
    "build_conformance.py",      # -> conformance_matrix.json, conformance_checklist.md
    "build_decision_records.py", # -> decision_records/
    "generate_reference.py",     # -> AMB_Schemas_Reference.md
]

def metrics():
    """Snapshot key counts from the current artifacts (missing -> None)."""
    m = {}
    try:
        idx = json.loads(INDEX.read_text())
        m["index_schemas"]     = idx["meta"]["schema_count"]
        m["index_endpoints"]   = idx["meta"]["endpoint_count"]
        m["open_decisions"]    = idx["meta"]["open_decision_point_count"]
        m["conflicts"]         = idx["meta"]["conflict_count"]
    except Exception:
        pass
    try:
        b = json.loads(BUNDLE.read_text())
        defs = b["$defs"]
        m["bundle_schemas"]    = len(defs)
        m["bundle_properties"] = sum(len(s.get("properties", {})) for s in defs.values())
        m["bundle_required"]   = sum(len(s.get("required", [])) for s in defs.values())
        g = b.get("x-amb-generator", {})
        m["structural"]        = g.get("structural_object_schema_count")
    except Exception:
        pass
    return m

def main():
    if not CANONICAL.exists():
        print(f"ABORT: canonical not found: {CANONICAL}", file=sys.stderr); sys.exit(1)

    before = metrics()
    print(f"AMB kit — regenerating from {CANONICAL.name}")
    print("=" * 64)
    for step in STEPS:
        print(f"\n▶ {step}")
        r = subprocess.run([sys.executable, str(ROOT / step)], env=ENV, cwd=str(ROOT))
        if r.returncode != 0:
            print(f"\nABORT: {step} failed (exit {r.returncode}). Downstream steps skipped.",
                  file=sys.stderr)
            sys.exit(r.returncode)
    after = metrics()

    print("\n" + "=" * 64)
    print("SUMMARY")
    print(f"  canonical:        {CANONICAL.name}")
    print(f"  index schemas:    {after.get('index_schemas')}  "
          f"endpoints: {after.get('index_endpoints')}  "
          f"open-decisions: {after.get('open_decisions')}  "
          f"conflicts: {after.get('conflicts')}")
    print(f"  object schemas:   {after.get('bundle_schemas')} "
          f"(incl. {after.get('structural')} structural)")
    print(f"  properties:       {after.get('bundle_properties')}  "
          f"required: {after.get('bundle_required')}")
    print("  validation:       all steps self-validated OK (would have aborted otherwise)")

    # coverage deltas vs previous build
    deltas = []
    for k in ("index_schemas", "bundle_schemas", "bundle_properties",
              "bundle_required", "index_endpoints", "open_decisions", "conflicts"):
        b_, a_ = before.get(k), after.get(k)
        if b_ is not None and a_ is not None and b_ != a_:
            deltas.append(f"{k}: {b_} -> {a_} ({a_-b_:+d})")
    print("  deltas:           " + ("; ".join(deltas) if deltas else "none (stable vs previous build)"))
    print(f"  finished:         {datetime.datetime.now(datetime.timezone.utc).isoformat()}")

if __name__ == "__main__":
    main()
