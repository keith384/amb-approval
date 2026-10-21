"""
Stage 4b — qualitative LLM pass.

Judges the rules Apple scores on that aren't machine-measurable (clear copy,
transfer announced with a reason, honest automation, confirmation after a tap,
clean screen, dead-ends, out-of-hours accuracy...). The model is handed ONLY the
rule set's qualitative video rules + the timestamped transcript + key frames, and
must return findings that each cite a provided rule_id and a timestamp. Anything
that cites an unknown rule or lacks a timestamp is dropped — measurement stays in
evaluate.py; this pass never invents rules or measures latency.
"""
from __future__ import annotations
import base64
import json
import os
import re
from pathlib import Path

import cv2

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
RULES_PATH = REPO / "packages/rules/rules.json"
MODEL = os.environ.get("AMB_LLM_MODEL", "claude-opus-4-8")
VALID_BUCKETS = {"Fail", "Caveat", "NotShownMandatory", "NotShownRecommended", "AppleWillAsk"}


def _ts(ms):
    s, _ = divmod(int(ms), 1000); m, s = divmod(s, 60)
    return f"{m:02d}:{s:02d}"


def _transcript(events, cap=70):
    segs = events["segment_detail"]
    out, last = [], None
    for s in segs:
        line = f"[{_ts(s['start_ms'])}] BIZ: {s['business_text'][:180]} || CUST: {s['customer_text'][:120]}"
        if line != last:
            out.append(line); last = line
    if len(out) > cap:  # thin evenly
        step = len(out) / cap
        out = [out[int(i * step)] for i in range(cap)]
    return "\n".join(out)


def _key_frames(work, events, n=10):
    segs = events["segment_detail"]
    picks = {s["frame_idx"]: s for s in segs if any(
        e for e in events["events"] if e.get("seg") == s["seg"] and e["type"] == "element_rendered")}
    ordered = sorted(picks.values(), key=lambda s: s["start_ms"])
    if len(ordered) > n:
        step = len(ordered) / n
        ordered = [ordered[int(i * step)] for i in range(n)]
    imgs = []
    for s in ordered:
        img = cv2.imread(str(work / s["tokens"][0].get("_path", "")) if False else str(work / f"frames/f{int(s['frame_idx']):05d}.jpg"))
        if img is None:
            continue
        h, w = img.shape[:2]
        img = cv2.resize(img, (320, int(320 * h / w)))
        ok, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 70])
        if ok:
            imgs.append((_ts(s["start_ms"]), base64.b64encode(buf).decode()))
    return imgs


def run(work_dir: str) -> dict:
    import anthropic
    work = Path(work_dir)
    rules = json.loads(RULES_PATH.read_text())["rules"]
    events = json.loads((work / "events.json").read_text())
    review = json.loads((work / "review.json").read_text())

    qual = [r for r in rules if "video" in r["stages"] and not r["machine_checkable"]]
    # keep the prompt focused: drop ones already covered deterministically
    done_ids = {f["rule_id"] for f in review["findings"]}
    qual = [r for r in qual if r["id"] not in done_ids][:45]
    rule_list = "\n".join(
        f'- {r["id"]} [{(r["letter_ids"] or [""])[0]}] ({r["severity"]}): {r["name"]} — {r["check"][:160]}'
        for r in qual)
    allowed = {r["id"] for r in qual}

    transcript = _transcript(events)
    frames = _key_frames(work, events)

    system = (
        "You are a Messaging Advisory reviewer grading an Apple Messages for Business "
        "experience recording before it goes to Apple. Judge ONLY the rules provided. "
        "Each finding MUST cite one of the provided rule ids and a timestamp (mm:ss) grounded "
        "in the transcript or a frame. Do not invent rules or requirements. Do not measure "
        "latency or counts (those are handled elsewhere). Be conservative: only flag what the "
        "evidence shows. Buckets: Fail (clear violation of an Apple rule), Caveat (quality risk), "
        "NotShownMandatory/NotShownRecommended (required thing not demonstrated), AppleWillAsk "
        "(question Apple will raise). Return STRICT JSON: "
        '{"findings":[{"rule_id","bucket","t_start","issue","fix"}]} and nothing else.')
    task = (
        f"RULES YOU MAY CITE (id [letter] (severity): name — check):\n{rule_list}\n\n"
        f"TIMESTAMPED TRANSCRIPT (OCR; business=agent, cust=customer):\n{transcript}\n\n"
        f"Key frames follow (each labeled with its timestamp). Judge the rules and return JSON.")

    content = [{"type": "text", "text": task}]
    for ts, b64 in frames:
        content.append({"type": "text", "text": f"frame @ {ts}:"})
        content.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": b64}})

    client = anthropic.Anthropic()
    resp = client.messages.create(model=MODEL, max_tokens=4000, system=system,
                                  messages=[{"role": "user", "content": content}])
    text = resp.content[0].text
    m = re.search(r"\{.*\}", text, re.S)
    parsed = json.loads(m.group(0)) if m else {"findings": []}

    by_id = {r["id"]: r for r in rules}
    kept, dropped = [], 0
    for f in parsed.get("findings", []):
        rid = str(f.get("rule_id", "")).strip()
        if rid not in allowed or not f.get("t_start") or f.get("bucket") not in VALID_BUCKETS:
            dropped += 1
            continue
        r = by_id[rid]
        kept.append({
            "rule_id": rid, "letter_ids": r.get("letter_ids", []), "name": r["name"],
            "severity": r["severity"], "source": r["source"], "origin": "llm",
            "bucket": f["bucket"], "issue": f["issue"][:200], "fix": f["fix"][:200],
            "t_start": f["t_start"], "t_end": None,
        })

    # merge (dedupe by rule_id+bucket already-present)
    seen = {(f["rule_id"], f["bucket"]) for f in review["findings"]}
    added = [f for f in kept if (f["rule_id"], f["bucket"]) not in seen]
    review["findings"].extend(added)
    counts = {}
    for f in review["findings"]:
        counts[f["bucket"]] = counts.get(f["bucket"], 0) + 1
    review["counts"] = counts
    review["verdict"] = ("fix Fails first" if counts.get("Fail") else
                         "not close yet" if counts.get("NotShownMandatory", 0) > 3 else "review before submit")
    (work / "review.json").write_text(json.dumps(review, indent=2))
    return {"model": MODEL, "judged_rules": len(qual), "returned": len(parsed.get("findings", [])),
            "kept": len(added), "dropped": dropped, "counts": counts}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("work_dir")
    a = ap.parse_args()
    s = run(a.work_dir)
    print(f"LLM pass ({s['model']}): judged {s['judged_rules']} rules · returned {s['returned']} · "
          f"kept {s['kept']} · dropped {s['dropped']} (bad rule/ts)")
    print("counts now:", s["counts"])
