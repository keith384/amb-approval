"""
Acceptance test — does Tool 3 reproduce MA's Ramp review?

Compares work/ramp/review.json against the ground truth extracted from MA's Ramp
report (tests/ramp-ground-truth.json). The build plan's bar: reproduce the six
Fails and >=15 of the 20 Caveats, with timestamps within 2 seconds. A ground-truth
finding is "reproduced" when our report has a finding whose rule letter-id matches
(or, for untagged GT rows, a same-bucket finding within the time tolerance) and
whose timestamp is within TOL seconds.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
GT_PATH = REPO / "tests/ramp-ground-truth.json"
TOL_S = 2.0


def _to_s(ts):
    if not ts:
        return None
    first = re.split(r"[-–]", str(ts))[0].strip()
    m = re.match(r"(\d+):(\d+)", first)
    return int(m.group(1)) * 60 + int(m.group(2)) if m else None


def _review_index(findings):
    rows = []
    for f in findings:
        rows.append({
            "letters": set(f.get("letter_ids") or []),
            "rule_id": f.get("rule_id"),
            "bucket": f.get("bucket"),
            "t": _to_s(f.get("t_start")),
            "t_end": _to_s(f.get("t_end")),
            "issue": f.get("issue", ""),
        })
    return rows


def _gt_letters(gl):
    """Expand a ground-truth letter_id into a token set: 'AT1 / AT2' -> {AT1,AT2};
    'RL1 to RL4' -> {RL1,RL2,RL3,RL4}."""
    if not gl:
        return set()
    out = set()
    for part in re.split(r"[/,]", gl):
        part = part.strip()
        rng = re.match(r"([A-Za-z]+)(\d+)\s+to\s+([A-Za-z]+)(\d+)", part)
        if rng:
            pre, a, _, b = rng.groups()
            for n in range(int(a), int(b) + 1):
                out.add(f"{pre}{n}")
        elif part:
            out.add(part)
    return out


def _matches(gt, rows, used):
    gt_t = _to_s(gt.get("timestamp"))
    glset = _gt_letters(gt.get("letter_id"))
    for i, r in enumerate(rows):
        if i in used:
            continue
        # rule identity: letter-id overlap, else same-bucket (for untagged GT rows)
        id_ok = (glset and (glset & r["letters"])) or (not glset and r["bucket"] == _bucket(gt["bucket"]))
        if not id_ok:
            continue
        # timestamp: GT has none → id match suffices; else within 2s of our t_start,
        # OR inside our [t_start, t_end] span (fair for findings that span a range).
        if gt_t is None:
            used.add(i); return i
        if r["t"] is not None:
            if abs(r["t"] - gt_t) <= TOL_S:
                used.add(i); return i
            if r["t_end"] is not None and r["t"] - TOL_S <= gt_t <= r["t_end"] + TOL_S:
                used.add(i); return i
    return None


def _bucket(b):
    return b  # ground truth already uses our bucket vocabulary


def run(work_dir: str) -> dict:
    gt = json.loads(GT_PATH.read_text())
    review = json.loads((Path(work_dir) / "review.json").read_text())
    rows = _review_index(review["findings"])
    used = set()

    per_bucket = {}
    misses = []
    for f in gt["findings"]:
        b = f["bucket"]
        per_bucket.setdefault(b, {"total": 0, "hit": 0})
        per_bucket[b]["total"] += 1
        if _matches(f, rows, used) is not None:
            per_bucket[b]["hit"] += 1
        else:
            misses.append(f)

    extra = [rows[i] for i in range(len(rows)) if i not in used]
    fails = per_bucket.get("Fail", {"total": 0, "hit": 0})
    cavs = per_bucket.get("Caveat", {"total": 0, "hit": 0})
    passed = fails["hit"] >= 6 and cavs["hit"] >= 15

    return {
        "passed": passed, "tolerance_s": TOL_S,
        "per_bucket": per_bucket,
        "fails_reproduced": f'{fails["hit"]}/{fails["total"]}',
        "caveats_reproduced": f'{cavs["hit"]}/{cavs["total"]}',
        "extra_findings": len(extra),
        "misses": misses,
    }


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("work_dir")
    ap.add_argument("--show-misses", action="store_true")
    a = ap.parse_args()
    r = run(a.work_dir)
    print(f"{'PASS' if r['passed'] else 'NOT YET'} (tol {r['tolerance_s']}s)")
    for b, c in r["per_bucket"].items():
        print(f"  {b:20} {c['hit']}/{c['total']} reproduced")
    print(f"  extra (over-flagged) findings: {r['extra_findings']}")
    if a.show_misses:
        print("\nMISSED ground-truth findings:")
        for m in r["misses"]:
            print(f"  [{m['bucket']:18}] {m.get('letter_id') or '--':5} {m.get('timestamp') or '--':>11}  {m['issue'][:66]}")
