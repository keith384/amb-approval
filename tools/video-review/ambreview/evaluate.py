"""
Stage 4+5 — rule evaluation + coverage.

Reads the rule set (packages/rules/rules.json) and the measured event stream
(events.json, typing.json, ocr.json) plus scope.json, and produces findings in
the Ramp five-bucket scheme. Deterministic checks only here; the qualitative LLM
pass (llm.py) layers on top. Every finding carries a rule id/letter + timestamp +
the evidence event — no finding may cite a rule absent from the rule set.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
RULES_PATH = REPO / "packages/rules/rules.json"

FORBIDDEN = re.compile(r"\b(imessage|apple chat|amb)\b", re.I)  # 0.3 / B3 naming
BARE_URL = re.compile(r"\b[a-z0-9-]+\.(com|io|co|ai|net|org)(/\S*)?\b", re.I)


def _ts(ms):
    s, msr = divmod(int(ms), 1000); m, s = divmod(s, 60)
    return f"{m:02d}:{s:02d}"


def _rule_index(rules):
    by_id = {r["id"]: r for r in rules}
    by_letter = {}
    for r in rules:
        for lt in r.get("letter_ids", []):
            by_letter[lt] = r
    return by_id, by_letter


def evaluate(work_dir: str) -> dict:
    work = Path(work_dir)
    rules = json.loads(RULES_PATH.read_text())["rules"]
    by_id, by_letter = _rule_index(rules)
    events = json.loads((work / "events.json").read_text())
    ocr = json.loads((work / "ocr.json").read_text())
    scope = json.loads((work / "scope.json").read_text()) if (work / "scope.json").exists() else {}
    typing = json.loads((work / "typing.json").read_text()) if (work / "typing.json").exists() else None

    findings = []

    def add(rule, bucket, issue, fix, t0=None, t1=None):
        """bucket: Fail | Caveat | NotShownMandatory | NotShownRecommended | AppleWillAsk"""
        if rule is None:
            return  # never emit a finding without a backing rule
        findings.append({
            "rule_id": rule["id"], "letter_ids": rule.get("letter_ids", []),
            "name": rule["name"], "severity": rule["severity"], "source": rule["source"],
            "bucket": bucket, "issue": issue, "fix": fix,
            "t_start": _ts(t0) if t0 is not None else None,
            "t_end": _ts(t1) if t1 is not None else None,
        })

    ev = events["events"]
    msgs = [e for e in ev if e["type"] == "message_appeared"]
    elements = [e for e in ev if e["type"] == "element_rendered"]
    present = {e["element"] for e in elements}

    # ── 0.3 / B3 — forbidden platform naming (deterministic, Non-negotiable) ──
    all_text = []
    for f in ocr["frames"].values():
        if f["tokens"]:
            for t in f["tokens"]:
                all_text.append((f["t_ms"], t["text"]))
    naming_hits = [(ms, tx) for ms, tx in all_text if FORBIDDEN.search(tx)]
    if naming_hits:
        r = by_id.get("0.3")
        first = naming_hits[0]
        add(r, "Fail",
            f'Forbidden platform wording on screen ("{first[1].strip()}"); {len(naming_hits)} occurrence(s).',
            'Replace with "Apple Messages for Business"; never "iMessage"/"AMB"/"Apple Chat".',
            first[0], naming_hits[-1][0])

    # ── 3.1 / C1 — first reply within 5s ──
    lats = events.get("latencies", [])
    if lats:
        first = lats[0]
        r = by_id.get("3.1")
        if first["latency_ms"] > 5000:
            add(r, "Fail", f'First business reply took {first["latency_ms"]/1000:.1f}s (> 5s).',
                "First response must arrive within 5s, with a typing indicator.",
                first["customer_t_ms"], first["business_t_ms"])

    # ── 3.5 / D1 — typing indicator before every business message ──
    r = by_id.get("3.5")
    if typing is None:
        add(r, "Caveat", "Typing-indicator detector not yet run — indicator-before-message "
            "unverified for this take.", "Run typing detection, then re-evaluate.")
    else:
        intervals = typing.get("intervals", [])
        # A typing indicator "covers" a reply if it ends shortly before the reply appears.
        def indicator_before(ms):
            return any(-500 <= (ms - iv["end_ms"]) <= 4000 for iv in intervals)
        # Collapse OCR-noisy business message events into reply BURSTS: a new burst
        # starts when >3s passes with no business text. One indicator is expected per burst.
        biz_ts = sorted(m["t_ms"] for m in msgs if m["side"] == "business")
        bursts = []
        for t in biz_ts:
            if not bursts or t - bursts[-1] > 3000:
                bursts.append(t)
        missing = [t for t in bursts if not indicator_before(t)]
        if bursts and missing:
            add(r, "Fail",
                f"{len(missing)} of {len(bursts)} business reply bursts had no typing indicator "
                f"before them ({len(intervals)} indicators detected).",
                "Show a typing indicator before every outbound message, including rich features.",
                missing[0], missing[-1])

    # ── bare URL (4.x rich links) ──
    url_hits = [(ms, tx) for ms, tx in all_text if BARE_URL.search(tx) and "http" not in tx.lower()]
    if url_hits:
        r = by_id.get("4.1")
        add(r, "Caveat", f'Possible bare URL text on screen ("{url_hits[0][1].strip()[:40]}").',
            "Use a Rich Link card, not a bare/tap-to-load URL.", url_hits[0][0])

    # ── Coverage / Not shown: scoped enhanced features with no on-screen evidence ──
    feat_to_element = {
        "quick_reply": "quick_reply", "list_picker": "list_picker", "time_picker": "time_picker",
        "rich_link": "rich_link_or_bare_url", "apple_pay": "apple_pay",
        "authentication": "authentication", "attachments": None, "forms": None,
    }
    # map features to a rule for the "not shown" line (best-effort by name match)
    name_rule = {
        "apple_pay": by_id.get("7.1") or by_id.get("7.2"),
        "authentication": by_id.get("7.9") or by_id.get("7.8"),
        "list_picker": by_letter.get("LP1"), "quick_reply": by_id.get("5.4"),
        "rich_link": by_id.get("4.1"), "time_picker": by_letter.get("TP1"),
        "attachments": by_letter.get("AT1"), "forms": None,
    }
    for feat, in_scope in (scope.get("enhanced_features") or {}).items():
        if not in_scope:
            continue
        el = feat_to_element.get(feat)
        shown = el in present if el else False
        if not shown:
            r = name_rule.get(feat)
            if r:
                add(r, "NotShownMandatory",
                    f'Feature "{feat}" is in scope but no evidence of it appears in the recording.',
                    f"Record a take that demonstrates {feat} on screen, or drop it from scope.")

    # ── Apple will ask (predicted questions keyed to features) ──
    awa = []
    if scope.get("enhanced_features", {}).get("apple_pay"):
        awa.append(("7.5", "What consent/verification gates Apple Pay card actions?"))
    if scope.get("live_agent"):
        awa.append(("9.2", "What is the live-agent target response time?"))
    if scope.get("enhanced_features", {}).get("authentication"):
        awa.append(("7.9", "How is the user verified before card/account actions?"))
    for rid, q in awa:
        r = by_id.get(rid)
        if r:
            add(r, "AppleWillAsk", q, "State this in writing in the submission.")

    counts = {}
    for f in findings:
        counts[f["bucket"]] = counts.get(f["bucket"], 0) + 1
    verdict = ("fix Fails first" if counts.get("Fail") else
               "not close yet" if counts.get("NotShownMandatory", 0) > 3 else "review before submit")

    review = {
        "brand": scope.get("brand", "unknown"),
        "ruleset_version": json.loads(RULES_PATH.read_text()).get("version"),
        "typing_detector": bool(typing),
        "counts": counts, "verdict": verdict, "findings": findings,
    }
    (work / "review.json").write_text(json.dumps(review, indent=2))
    return review


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("work_dir")
    a = ap.parse_args()
    rv = evaluate(a.work_dir)
    print(f"verdict: {rv['verdict']}  ·  counts: {rv['counts']}")
    for f in rv["findings"]:
        lt = f["letter_ids"][0] if f["letter_ids"] else f["rule_id"]
        print(f"  [{f['bucket']:18}] {lt:5} {f['t_start'] or '--':>5}  {f['issue'][:70]}")
