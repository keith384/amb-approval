"""
Stage 3 — event detection.

Turns the timed OCR transcript into a structured event stream the rules evaluate
against. Events: screen segments (stable screens between visual-diff boundaries),
message_appeared (new business/customer text), element_rendered (rich elements by
signature), and reply-latency pairs. The typing-indicator visual detector is a
separate focused pass (it is pixel-shape, not OCR-able); first-reply latency here
is message-to-message and is refined once the indicator detector lands.

Measurement only — no judgments. Every downstream finding cites an event + timestamp.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

STATUS_BAR_Y = 0.045          # crop the iPhone status bar (time / SOS / battery)
CONF_MIN = 0.40
URL_RE = re.compile(r"(https?://|www\.|\b[a-z0-9-]+\.(com|io|co|ai|net|org)\b)", re.I)

# Rich-element signatures (business-side). Conservative; refined against the corpus.
ELEMENT_SIGNS = {
    "apple_pay": re.compile(r"\b(apple pay|pay \$|\bpay\b.*\$)", re.I),
    "authentication": re.compile(r"\b(verification code|authenticate|passcode|sign in with)\b", re.I),
    "time_picker": re.compile(r"\b(select a time|choose a time|AM\b|PM\b|appointment)\b", re.I),
    "list_picker": None,   # inferred from option rows (see below)
    "quick_reply": None,   # inferred from option chips
    "rich_link": None,     # inferred from URL / link card
}
# Known Ramp CTA option labels help classify option rows during bring-up.
OPTIONISH = re.compile(r"^(submit|ask|talk|connect|yes|no|start|stop|help|agent|"
                       r"receipt|question|person|expense|continue|done|back|more)", re.I)


def _side_text(tokens, side):
    out = []
    for t in tokens or []:
        if t["conf"] < CONF_MIN or t["y"] < STATUS_BAR_Y:
            continue
        if t["side"] == side or (side == "business" and t["side"] == "center"):
            out.append(t)
    return out


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def detect(work_dir: str) -> dict:
    out = Path(work_dir)
    frames = json.loads((out / "frames.json").read_text())["frames"]
    ocr = json.loads((out / "ocr.json").read_text())["frames"]

    # 1) Screen segments: each OCR'd (non-dup) frame opens a segment that runs until
    #    the next OCR'd frame.
    kept = [(int(i), f) for i, f in ocr.items() if f["tokens"] is not None]
    kept.sort(key=lambda kv: kv[0])
    segments = []
    for n, (idx, f) in enumerate(kept):
        end_ms = kept[n + 1][1]["t_ms"] if n + 1 < len(kept) else frames[-1]["t_ms"]
        biz = _side_text(f["tokens"], "business")
        cust = _side_text(f["tokens"], "customer")
        segments.append({
            "seg": n, "frame_idx": idx, "start_ms": f["t_ms"], "end_ms": end_ms,
            "business_text": " | ".join(t["text"] for t in biz),
            "customer_text": " | ".join(t["text"] for t in cust),
            "tokens": f["tokens"],
        })

    # 2) message_appeared: new side-text lines vs the previous segment.
    events = []
    prev_biz, prev_cust = set(), set()
    for s in segments:
        for side, prev in (("business", prev_biz), ("customer", prev_cust)):
            cur_lines = {_norm(x) for x in (s[f"{side}_text"].split(" | ")) if len(_norm(x)) >= 4}
            new = cur_lines - prev
            for line in new:
                events.append({"t_ms": s["start_ms"], "type": "message_appeared",
                               "side": side, "text": line, "seg": s["seg"]})
            if side == "business":
                prev_biz = cur_lines | prev_biz
            else:
                prev_cust = cur_lines | prev_cust

        # 3) element_rendered (business side), by signature.
        btext = s["business_text"]
        for kind, rx in ELEMENT_SIGNS.items():
            if rx and rx.search(btext):
                events.append({"t_ms": s["start_ms"], "type": "element_rendered",
                               "element": kind, "seg": s["seg"]})
        # option rows → quick_reply (<=5) vs list_picker (>5), measured off option-ish labels
        opts = [t["text"] for t in s["tokens"]
                if t["conf"] >= CONF_MIN and t["y"] >= STATUS_BAR_Y and OPTIONISH.match(t["text"].strip())]
        if len(opts) >= 2:
            kind = "quick_reply" if len(opts) <= 5 else "list_picker"
            events.append({"t_ms": s["start_ms"], "type": "element_rendered",
                           "element": kind, "options": opts, "count": len(opts), "seg": s["seg"]})
        if URL_RE.search(btext):
            events.append({"t_ms": s["start_ms"], "type": "element_rendered",
                           "element": "rich_link_or_bare_url", "seg": s["seg"]})

    events.sort(key=lambda e: (e["t_ms"], e["type"]))

    # 4) reply latency: each customer message → next business message.
    msgs = [e for e in events if e["type"] == "message_appeared"]
    latencies = []
    for i, e in enumerate(msgs):
        if e["side"] != "customer":
            continue
        nxt = next((m for m in msgs[i + 1:] if m["side"] == "business"), None)
        if nxt:
            latencies.append({"customer_t_ms": e["t_ms"], "business_t_ms": nxt["t_ms"],
                              "latency_ms": nxt["t_ms"] - e["t_ms"],
                              "prompt": e["text"][:60]})

    payload = {
        "segments": len(segments),
        "events": events,
        "latencies": latencies,
        "first_reply_latency_ms": latencies[0]["latency_ms"] if latencies else None,
    }
    (out / "events.json").write_text(json.dumps({**payload, "segment_detail": segments}, indent=2))
    return payload


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("work_dir")
    a = ap.parse_args()
    p = detect(a.work_dir)
    el = {}
    for e in p["events"]:
        if e["type"] == "element_rendered":
            el[e["element"]] = el.get(e["element"], 0) + 1
    msgs = [e for e in p["events"] if e["type"] == "message_appeared"]
    print(f"{p['segments']} screen segments · {len(msgs)} message events "
          f"({sum(m['side']=='business' for m in msgs)} biz / {sum(m['side']=='customer' for m in msgs)} cust)")
    print("elements detected:", el)
    print("reply latencies (first 6):")
    for l in p["latencies"][:6]:
        s, ms = divmod(l["latency_ms"], 1000)
        print(f"  +{l['latency_ms']/1000:5.1f}s  after customer: {l['prompt']!r}")
