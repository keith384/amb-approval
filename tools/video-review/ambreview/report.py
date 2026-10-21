"""
Stage 6 — report render.

Renders review.json into the MA Ramp-report format: five buckets with a header
count line and a verdict, each finding as TIME · TEST · ISSUE · FIX. Emits a
Markdown report (for Slack) and the timestamp index Apple wants alongside the
video. The HTML→PDF path (shared with Tool 2) is a later step.
"""
from __future__ import annotations
import json
from pathlib import Path

BUCKETS = [
    ("Fail", "Fail"),
    ("Caveat", "Caveat"),
    ("NotShownMandatory", "Not shown — Mandatory"),
    ("NotShownRecommended", "Not shown — Recommended"),
    ("AppleWillAsk", "Apple will ask"),
]


def _test_label(f):
    lt = ", ".join(f["letter_ids"]) if f["letter_ids"] else ""
    return f"{lt + ' ' if lt else ''}({f['rule_id']}) {f['name']}"


def render_markdown(review: dict) -> str:
    c = review["counts"]
    header = " · ".join(f"{c.get(k, 0)} {label}" for k, label in BUCKETS)
    out = [
        f"# Experience Review — {review['brand']}",
        f"_Rule set {review.get('ruleset_version')} · "
        f"typing detector: {'on' if review.get('typing_detector') else 'OFF (indicator rules pending)'}_",
        "",
        f"**{header}**",
        "",
        f"**Verdict: {review['verdict']}.**",
        "",
    ]
    for key, label in BUCKETS:
        items = [f for f in review["findings"] if f["bucket"] == key]
        if not items:
            continue
        out.append(f"## {label} ({len(items)})")
        out.append("")
        out.append("| Time | Test | Issue | Fix |")
        out.append("|---|---|---|---|")
        for f in items:
            tr = f["t_start"] or ""
            if f["t_end"] and f["t_end"] != f["t_start"]:
                tr = f"{f['t_start']}–{f['t_end']}"
            out.append(f"| {tr} | {_test_label(f)} | {f['issue']} | {f['fix']} |")
        out.append("")
    return "\n".join(out)


def render_timestamp_index(review: dict) -> str:
    rows = sorted((f for f in review["findings"] if f["t_start"]), key=lambda f: f["t_start"])
    lines = [f"V1  {f['t_start']}   {_test_label(f)}" for f in rows]
    return "\n".join(lines) + "\n"


def write_report(work_dir: str) -> dict:
    work = Path(work_dir)
    review = json.loads((work / "review.json").read_text())
    brand = review.get("brand", "brand")
    md = render_markdown(review)
    (work / f"review-{brand}.md").write_text(md + "\n")
    (work / f"timestamp-index-{brand}.txt").write_text(render_timestamp_index(review))
    return {"md": md, "counts": review["counts"]}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("work_dir")
    a = ap.parse_args()
    r = write_report(a.work_dir)
    print(r["md"])
