#!/usr/bin/env python3
"""
Tool 1 (Brand Approval Doc generator) — orchestrator.

    python brand_doc.py <intake.json> <out_dir>

Runs: generate (LLM: intake → doc model + scope) → build_doc (Walmart-shape HTML +
readiness note) → fill_forms (Apple Use Cases + Readiness AcroForms). Emits, per
brand: brand-approval-<brand>.html, <brand>-usecases.pdf, <brand>-readiness.pdf,
scope.json (for Tools 2/3), readiness-<brand>.md. The Slack `/amb brand-doc` calls this.
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

import generate
import build_doc
import fill_forms


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("intake")
    ap.add_argument("out_dir")
    a = ap.parse_args()

    g = generate.run(a.intake, a.out_dir)
    print(f"· generate: {g['use_cases']} use cases · features {g['features']}")
    if g["flags"].get("pre_approval"):
        print(f"  ⚠ pre-approval: {g['flags']['pre_approval']}")
    d = build_doc.build(a.out_dir)
    print(f"· doc: {d['html']} · {d['open_questions']} open questions · {d['terminology_hits']} terminology hits")
    f = fill_forms.fill_all(str(Path(a.out_dir) / "scope.json"), a.out_dir)
    for key, info in f.items():
        print(f"· form {key}: filled {info['filled']}/{info['total_fields']} "
              f"({len(info['blank_open_questions'])} open)")
    print(f"\nArtifacts written to {a.out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
