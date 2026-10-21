#!/usr/bin/env python3
"""Rule-set invariants. Run: python3 test_rules.py  (non-zero exit on failure)."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RULES = json.loads((HERE / "rules.json").read_text())
r = RULES["rules"]
VALID_SEVERITY = {"Non negotiable", "Apple standard", "Field"}
VALID_STAGES = {"doc", "storyboard", "video"}
# Apple's five non-negotiables (legend) + the two extra Section-0 gate items.
EXPECTED_GATE = {"0.1", "0.2", "0.3", "0.4", "7.4", "7.8", "8.1", "8.2", "8.5", "10.1", "10.2", "10.8"}

fails = []
def check(cond, msg):
    if not cond:
        fails.append(msg)

check(len(r) == 114, f"expected 114 rules, got {len(r)}")
ids = [x["id"] for x in r]
check(len(ids) == len(set(ids)), "duplicate rule ids")

for x in r:
    check(x["severity"] in VALID_SEVERITY, f"{x['id']}: bad severity {x['severity']!r}")
    check(bool(x["source_anchor"]), f"{x['id']}: no source anchor")       # plan: every rule cites a source
    check(bool(x["name"]) and bool(x["check"]), f"{x['id']}: empty name/check")
    check(set(x["stages"]) <= VALID_STAGES, f"{x['id']}: bad stages {x['stages']}")
    check(x["source"] in {"Apple", "MA (Field)"}, f"{x['id']}: bad source {x['source']!r}")
    # Field severity must be an MA observation, never tagged Apple.
    if x["severity"] == "Field":
        check(x["source"] == "MA (Field)", f"{x['id']}: Field severity must be MA-sourced")
    else:
        check(x["source"] == "Apple", f"{x['id']}: non-Field must be Apple-sourced")

# Section 0 gate items present (these block submission on their own).
present = set(ids)
missing_gate = {g for g in EXPECTED_GATE if g.split(".")[0] == "0"} - present
check(not missing_gate, f"missing Section-0 gate rules: {sorted(missing_gate)}")

nn = [x["id"] for x in r if x["severity"] == "Non negotiable"]
check(len(nn) >= 5, f"expected >=5 non-negotiables, got {len(nn)}")

if fails:
    print("FAIL:", file=sys.stderr)
    for f in fails:
        print("  -", f, file=sys.stderr)
    sys.exit(1)
print(f"PASS — {len(r)} rules, {len(nn)} non-negotiable, all cite a source anchor.")
