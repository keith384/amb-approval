#!/usr/bin/env python3
"""
Build the AMB rule set from its sources into a single versioned rules.json.

Phase 0 foundation. The primary source is Messaging Advisory's Experience Review
checklist (114 test cases), extracted to CSV. Each test case becomes one rule
record. Severity drives the source tag per the workbook legend:
  - "Non negotiable" / "Apple standard"  -> Apple requirement
  - "Field"                              -> Messaging Advisory observation

IMPORTANT (per build plan): we do NOT author Apple rules. Where a source is
silent, the rule set is silent. This script only normalizes existing sources.
Letter-ID aliases (Ramp report scheme: B1, C1, RL1 ...) are layered in from a
separate mapping file once extracted; they are never invented here.

Usage:  python3 build_rules.py            # writes rules.json + prints summary
        python3 build_rules.py --check    # validate only, non-zero exit on error
"""
from __future__ import annotations
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CHECKLIST = REPO / "sources/ma-experience-review/checklist-extracted/sheet2-checklist.csv"
ALIASES = HERE / "sources/letter-id-aliases.json"   # {numeric_ref: letter_id}, built from Ramp report
STAGE_OVERRIDES = HERE / "sources/stage-overrides.json"  # {ref: ["doc","storyboard","video"]}
OUT = HERE / "rules.json"

RULESET_VERSION = "0.1.0"
SOURCE_ANCHOR = "MA Experience Review checklist & test cases v2.0 (31 Aug 2026)"

SEVERITY_TO_SOURCE = {
    "Non negotiable": "Apple",
    "Apple standard": "Apple",
    "Field": "MA (Field)",
}

# Heuristic only — refined later. Measurable/threshold language => code can check it;
# qualitative judgement => the model (constrained to the rule). Flagged provisional.
MACHINE_HINTS = re.compile(
    r"\b(within|second|seconds|\bs\b|latency|fps|count|number|url|link|exact|\d+\s*(s|sec|ms)|"
    r"wording|naming|iMessage|AMB|Apple Chat|option|options|character|chars?)\b",
    re.I,
)
MODEL_HINTS = re.compile(
    r"\b(clear|honest|announced?|reason|appropriate|natural|confusing|tone|friendly|"
    r"understandable|disclos|transparent|quality)\b",
    re.I,
)


def load_json(p: Path, default):
    if p.exists():
        return json.loads(p.read_text())
    return default


def classify_machine_checkable(text: str) -> bool:
    m = bool(MACHINE_HINTS.search(text))
    j = bool(MODEL_HINTS.search(text))
    # Prefer code when measurable language present and no strong judgement language.
    if m and not j:
        return True
    if j and not m:
        return False
    # Mixed/neither: default to model (safer — code false-positives are worse here).
    return False


def main() -> int:
    check_only = "--check" in sys.argv
    if not CHECKLIST.exists():
        print(f"ERROR: checklist source not found: {CHECKLIST}", file=sys.stderr)
        return 2

    # Invert the Ramp letter-ID map {letter: {ref, confidence,...}} into
    # {numeric_ref: [letter_ids]} — a rule can carry several letter aliases.
    raw_aliases = load_json(ALIASES, {})
    alias_entries = raw_aliases.get("aliases", raw_aliases)
    ref_to_letters: dict[str, list[str]] = {}
    for letter, info in alias_entries.items():
        if letter.startswith("_"):
            continue
        ref = info.get("ref") if isinstance(info, dict) else info
        if ref:
            ref_to_letters.setdefault(ref, []).append(letter)
    stage_overrides = load_json(STAGE_OVERRIDES, {})

    rules = []
    errors = []
    with CHECKLIST.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            ref = (row.get("Ref") or "").strip()
            name = (row.get("Test case") or "").strip()
            if not ref or not name:
                continue  # section header / spacer row
            steps = (row.get("Test steps") or "").strip()
            expected = (row.get("Expected result") or "").strip()
            severity = (row.get("Severity") or "").strip()
            applies_when = (row.get("Applies when") or "").strip() or "Always"
            section = (row.get("Section") or "").strip()
            rule_ref = (row.get("Rule ref") or "").strip() or None

            source = SEVERITY_TO_SOURCE.get(severity)
            if source is None:
                errors.append(f"{ref}: unknown severity {severity!r}")
                source = "MA (Field)"

            check_text = expected or steps
            default_stage = ["video"]  # checklist is the Experience Review (video) stage
            stages = stage_overrides.get(ref, default_stage)

            rules.append({
                "id": ref,
                "letter_ids": ref_to_letters.get(ref, []),  # Ramp report aliases (0+)
                "section": section,
                "name": name,
                "check": check_text,
                "test_steps": steps,
                "expected_result": expected,
                "severity": severity,                    # Non negotiable | Apple standard | Field
                "source": source,                        # Apple | MA (Field)
                "source_anchor": SOURCE_ANCHOR,
                "rule_ref": rule_ref,                    # Standards v2.1 section
                "applies_when": applies_when,            # keyed to scope.json (normalized later)
                "stages": stages,                        # doc | storyboard | video
                "machine_checkable": classify_machine_checkable(f"{steps} {expected}"),
            })

    # Validation: every rule cites a source anchor + has a severity we recognize.
    for r in rules:
        if not r["source_anchor"]:
            errors.append(f"{r['id']}: missing source anchor")
        if r["severity"] not in SEVERITY_TO_SOURCE:
            errors.append(f"{r['id']}: bad severity {r['severity']!r}")

    summary = {
        "total": len(rules),
        "by_severity": _count(rules, "severity"),
        "non_negotiables": [r["id"] for r in rules if r["severity"] == "Non negotiable"],
        "machine_checkable": sum(1 for r in rules if r["machine_checkable"]),
        "with_letter_id": sum(1 for r in rules if r["letter_ids"]),
    }

    if errors:
        print("VALIDATION ERRORS:", file=sys.stderr)
        for e in errors:
            print("  -", e, file=sys.stderr)
        return 1

    if check_only:
        print(f"OK — {len(rules)} rules valid.")
        return 0

    OUT.write_text(json.dumps({
        "version": RULESET_VERSION,
        "generated_from": SOURCE_ANCHOR,
        "note": "Normalized from MA sources. No rules authored here. "
                "Letter-IDs and applies-when scope keys layered in later phases.",
        "summary": summary,
        "rules": rules,
    }, indent=2) + "\n")
    print(f"Wrote {OUT.relative_to(REPO)} — {summary['total']} rules "
          f"({summary['by_severity']}). {summary['machine_checkable']} machine-checkable (provisional).")
    return 0


def _count(rules, key):
    out = {}
    for r in rules:
        out[r[key]] = out.get(r[key], 0) + 1
    return out


if __name__ == "__main__":
    raise SystemExit(main())
