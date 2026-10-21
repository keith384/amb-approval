#!/usr/bin/env python3
"""
Tool 3 (Video Review) — pipeline orchestrator.

    python review.py <recording.mp4> <work_dir> [--fps 5] [--brand NAME]

Runs: extract → OCR → typing (if available) → events → evaluate → report.
Each stage caches to <work_dir>; re-running reuses prior stages' output. The
Slack `/amb review <brand>` and the board's upload worker call this.
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

from ambreview import extract, ocr, events, evaluate, report

try:
    from ambreview import typing as typing_mod  # optional until the detector lands
except Exception:
    typing_mod = None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("work_dir")
    ap.add_argument("--fps", type=float, default=5.0)
    ap.add_argument("--brand", default=None)
    ap.add_argument("--skip-extract", action="store_true", help="reuse existing frames")
    ap.add_argument("--skip-ocr", action="store_true", help="reuse existing ocr.json")
    ap.add_argument("--no-llm", action="store_true", help="deterministic rules only")
    a = ap.parse_args()
    work = Path(a.work_dir)

    if not a.skip_extract or not (work / "frames.json").exists():
        m = extract.extract_frames(a.video, a.work_dir, a.fps)
        print(f"· extract: {m['frame_count']} frames ({m['first_ts']}→{m['last_ts']})")
    if not a.skip_ocr or not (work / "ocr.json").exists():
        o = ocr.ocr_frames(a.work_dir)
        print(f"· ocr: {o['ocr_frames']}/{o['total_frames']} distinct screens")
    if typing_mod and hasattr(typing_mod, "detect_typing"):
        t = typing_mod.detect_typing(a.work_dir)
        print(f"· typing: {t.get('count', 0)} indicator intervals")
    else:
        print("· typing: detector not available — indicator rules will be marked pending")
    e = events.detect(a.work_dir)
    print(f"· events: {e['segments']} segments, {len(e['events'])} events")
    rv = evaluate.evaluate(a.work_dir)
    print(f"· evaluate (deterministic): {rv['counts']}")
    if not a.no_llm and __import__("os").environ.get("ANTHROPIC_API_KEY"):
        try:
            from ambreview import llm
            s = llm.run(a.work_dir)
            print(f"· llm ({s['model']}): +{s['kept']} qualitative findings, dropped {s['dropped']}")
            rv = __import__("json").loads((work / "review.json").read_text())
        except Exception as ex:
            print(f"· llm: skipped ({ex})")
    else:
        print("· llm: skipped (no ANTHROPIC_API_KEY or --no-llm)")
    report.write_report(a.work_dir)
    print(f"· report: {rv['counts']} — verdict: {rv['verdict']}")
    print(f"\nWrote review-*.md, timestamp-index-*.txt, review.json to {a.work_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
