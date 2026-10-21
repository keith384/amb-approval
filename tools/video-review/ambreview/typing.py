"""
Typing-indicator detector (visual, pixel-shape pass).

Apple Messages for Business shows a small light-grey rounded "thought" bubble at
the BOTTOM-LEFT of the conversation (business side) containing three animated
medium-grey dots while the business is composing a reply, just before a business
message bubble appears. OCR cannot see it (there is no text), so this is a focused
per-frame shape classifier run across every extracted frame, with positive frames
merged into on-screen intervals.

What the indicator looks like (measured on the Ramp capture, 592x1280 @ 5fps):
  - A light-grey bubble body, RGB ~ (231, 231, 234), low saturation.
  - Three roughly-equal medium-grey dots in a horizontal row inside it. The dots
    animate (pulse), so their grey drifts ~ (122..180); crucially they are MEDIUM
    grey, NOT the near-black of message text — that is the main discriminator.
  - The three dots span ~50 px wide, ~12 px tall, sitting in the lower-left of the
    conversation column (just above the compose field; its exact y depends on
    whether the keyboard is up and on scroll position).

Detection, per frame (all measurement, no judgement):
  1. In the left conversation column, mask "dot-grey" pixels (value 100..200, low
     saturation) and "bubble-grey" pixels (value ~218..246, low saturation).
  2. Connected components of the dot-grey mask -> keep small, roughly-circular,
     roughly-equal blobs (the antialiased edges of black text fail these filters).
  3. Find a horizontal triple: 3 such blobs at the same y (+/- a few px), evenly
     spaced, within a narrow x span, of similar size.
  4. Require the triple to sit on a light-grey bubble (local bubble-grey fraction),
     which rejects keyboard glyphs, the "+" compose button, and bubble text.
  5. A frame is positive if such a triple exists. Positive frames are merged into
     intervals (bridging short <=2-frame gaps for the dot animation / mid-scroll).

Timestamps come from frames.json (idx -> t_ms).
"""
from __future__ import annotations

import json
from pathlib import Path

import cv2
import numpy as np

# ---- search region (fraction of frame) -------------------------------------
# Left conversation column. y spans both keyboard-up (~0.45-0.55) and
# keyboard-down (~0.78-0.88) resting positions of the indicator.
X_LO, X_HI = 0.00, 0.44
Y_LO, Y_HI = 0.34, 0.93

# ---- colour thresholds ------------------------------------------------------
DOT_V_LO, DOT_V_HI = 100, 200        # medium grey (NOT black text, NOT white bg)
BUBBLE_V_LO, BUBBLE_V_HI = 216, 247  # light iOS bubble grey
SAT_MAX = 30                         # R~=G~=B (grey, not coloured)

# ---- blob shape filters (full-res px) --------------------------------------
BLOB_AREA_LO, BLOB_AREA_HI = 28, 520
BLOB_WH_LO, BLOB_WH_HI = 5, 26
BLOB_EXTENT_MIN = 0.50               # area / bbox area -> roughly solid/round
BLOB_ASPECT = 2.2                    # w/h and h/w both below this

# ---- triple (three-in-a-row) geometry --------------------------------------
TRIPLE_DY = 7                        # vertical centroid spread
GAP_LO, GAP_HI = 11, 40              # centre-to-centre spacing between dots
GAP_BALANCE = 12                     # |gap1 - gap2|
SPAN_MAX = 95                        # total x span of the three centres
AREA_RATIO_MAX = 3.2                 # max/min dot area
BUBBLE_CTX_MIN = 0.18                # light-grey fraction around the triple
# The typing bubble is a business-side (left-aligned) bubble, so its dots always
# hug the left margin. This rejects accidental triples formed by the antialiased
# edges of message text deeper inside bubbles (observed at x_frac 0.18..0.38).
DOT_LEFT_FRAC = (0.03, 0.15)         # leftmost dot centre, as fraction of width
DOT_RIGHT_FRAC_MAX = 0.24            # rightmost dot centre, as fraction of width
# The three dots must sit inside ONE solid, correctly-sized light-grey bubble
# (bubble-grey + dots, morphologically closed). This rejects (a) accidental
# triples inside big text bubbles, whose enclosing grey region is huge/merged,
# and (b) rows of tiny dots inside app-switcher / photo-picker thumbnails, whose
# solid grey card is far larger than a chat bubble. Measured typing bubble on the
# Ramp capture: ~54..97 px wide, ~33..65 px tall, ~1500..4500 px area.
BUBBLE_W = (40, 120)
BUBBLE_H = (28, 78)
BUBBLE_AREA = (1100, 6800)
BUBBLE_EXTENT_MIN = 0.55

# ---- interval merging -------------------------------------------------------
MERGE_GAP_FRAMES = 2                 # bridge up to this many missing frames


def _masks(bgr: np.ndarray):
    """Return (dot_mask, bubble_mask) uint8 for a BGR crop."""
    a = bgr.astype(np.int16)
    v = a.mean(2)
    sat = a.max(2) - a.min(2)
    grey = sat <= SAT_MAX
    dot = (grey & (v >= DOT_V_LO) & (v <= DOT_V_HI)).astype(np.uint8)
    bubble = (grey & (v >= BUBBLE_V_LO) & (v <= BUBBLE_V_HI)).astype(np.uint8)
    return dot, bubble


def _blobs(dot_mask: np.ndarray):
    """Connected components of the dot mask passing the per-dot shape filters."""
    n, lbl, stats, cents = cv2.connectedComponentsWithStats(dot_mask, connectivity=8)
    out = []
    for i in range(1, n):
        x, y, w, h, area = stats[i]
        if not (BLOB_AREA_LO <= area <= BLOB_AREA_HI):
            continue
        if not (BLOB_WH_LO <= w <= BLOB_WH_HI and BLOB_WH_LO <= h <= BLOB_WH_HI):
            continue
        if area / float(w * h) < BLOB_EXTENT_MIN:
            continue
        if w / float(h) > BLOB_ASPECT or h / float(w) > BLOB_ASPECT:
            continue
        cx, cy = cents[i]
        out.append((cx, cy, float(area), x, y, w, h))
    return out


def _bubble_components(dot_mask: np.ndarray, bubble_mask: np.ndarray):
    """Label solid grey regions (bubble body + dots, closed) for containment test."""
    soft = ((bubble_mask | dot_mask) * 255).astype(np.uint8)
    soft = cv2.morphologyEx(soft, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    n, lbl, stats, _ = cv2.connectedComponentsWithStats((soft > 0).astype(np.uint8), 8)
    return lbl, stats


def _bubble_ok(lbl, stats, cx: int, cy: int) -> bool:
    """True if (cx, cy) lands in a component shaped like a typing bubble."""
    H, W = lbl.shape
    if not (0 <= cy < H and 0 <= cx < W):
        return False
    comp = int(lbl[cy, cx])
    if comp == 0:
        return False
    x, y, w, h, area = stats[comp]
    if not (BUBBLE_W[0] <= w <= BUBBLE_W[1] and BUBBLE_H[0] <= h <= BUBBLE_H[1]):
        return False
    if not (BUBBLE_AREA[0] <= area <= BUBBLE_AREA[1]):
        return False
    return area / float(w * h) >= BUBBLE_EXTENT_MIN


def _has_triple(blobs, dot_mask: np.ndarray, bubble_mask: np.ndarray, frame_w: int) -> bool:
    """True if three blobs form an evenly-spaced horizontal row on a grey bubble."""
    bl = sorted(blobs, key=lambda b: b[0])  # by x centre
    H, W = bubble_mask.shape
    lbl, stats = _bubble_components(dot_mask, bubble_mask)
    for i in range(len(bl)):
        for j in range(i + 1, len(bl)):
            for k in range(j + 1, len(bl)):
                a, b, c = bl[i], bl[j], bl[k]
                ys = [a[1], b[1], c[1]]
                if max(ys) - min(ys) > TRIPLE_DY:
                    continue
                g1, g2 = b[0] - a[0], c[0] - b[0]
                if not (GAP_LO <= g1 <= GAP_HI and GAP_LO <= g2 <= GAP_HI):
                    continue
                if abs(g1 - g2) > GAP_BALANCE:
                    continue
                if c[0] - a[0] > SPAN_MAX:
                    continue
                # left-margin gate (crop x == frame x because X_LO == 0)
                if not (DOT_LEFT_FRAC[0] <= a[0] / frame_w <= DOT_LEFT_FRAC[1]):
                    continue
                if c[0] / frame_w > DOT_RIGHT_FRAC_MAX:
                    continue
                areas = [a[2], b[2], c[2]]
                if max(areas) / max(min(areas), 1.0) > AREA_RATIO_MAX:
                    continue
                xs = [a[0], b[0], c[0]]
                cx = int(sum(xs) / 3)
                cy = int(sum(ys) / 3)
                # bubble context: pad the triple bbox and measure light-grey fraction
                pad = 14
                bx0 = max(int(min(xs)) - pad, 0)
                bx1 = min(int(max(xs)) + pad, W)
                by0 = max(cy - pad, 0)
                by1 = min(cy + pad, H)
                ctx = bubble_mask[by0:by1, bx0:bx1]
                if not (ctx.size and ctx.mean() >= BUBBLE_CTX_MIN):
                    continue
                # structural gate: the triple must sit inside a bubble-sized blob
                if _bubble_ok(lbl, stats, cx, cy):
                    return True
    return False


def _frame_has_indicator(path: str) -> bool:
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        return False
    H, W = img.shape[:2]
    x0, x1 = int(X_LO * W), int(X_HI * W)
    y0, y1 = int(Y_LO * H), int(Y_HI * H)
    crop = img[y0:y1, x0:x1]
    dot, bubble = _masks(crop)
    blobs = _blobs(dot)
    if len(blobs) < 3:
        return False
    return _has_triple(blobs, dot, bubble, W)


def _merge(positive_idxs, idx_to_ms, frame_dt_ms):
    """Merge sorted positive frame indices into intervals (bridging small gaps)."""
    intervals = []
    if not positive_idxs:
        return intervals
    run_start = prev = positive_idxs[0]
    for idx in positive_idxs[1:]:
        if idx - prev <= MERGE_GAP_FRAMES + 1:
            prev = idx
            continue
        intervals.append((run_start, prev))
        run_start = prev = idx
    intervals.append((run_start, prev))

    out = []
    for s, e in intervals:
        start_ms = idx_to_ms[s]
        # end is the moment the indicator leaves: last positive frame + one step
        end_ms = idx_to_ms[e] + frame_dt_ms
        out.append({"start_ms": int(start_ms), "end_ms": int(end_ms),
                    "dur_ms": int(end_ms - start_ms)})
    return out


def detect_typing(work_dir: str) -> dict:
    out = Path(work_dir)
    frames = json.loads((out / "frames.json").read_text())["frames"]
    idx_to_ms = {f["idx"]: f["t_ms"] for f in frames}

    # median inter-frame step (robust to any gaps)
    ts = [f["t_ms"] for f in frames]
    diffs = sorted(ts[i + 1] - ts[i] for i in range(len(ts) - 1)) or [200]
    frame_dt_ms = diffs[len(diffs) // 2]

    positive = []
    for f in frames:
        p = out / f["path"]
        if _frame_has_indicator(str(p)):
            positive.append(f["idx"])
    positive.sort()

    intervals = _merge(positive, idx_to_ms, frame_dt_ms)
    payload = {"intervals": intervals, "count": len(intervals)}
    (out / "typing.json").write_text(json.dumps(payload, indent=2))
    return payload


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Detect iMessage typing-indicator intervals.")
    ap.add_argument("work_dir", help="work dir containing frames.json + frames/")
    a = ap.parse_args()
    res = detect_typing(a.work_dir)
    print(f"{res['count']} typing interval(s):")
    for iv in res["intervals"]:
        print(f"  {iv['start_ms']/1000:7.2f}s -> {iv['end_ms']/1000:7.2f}s "
              f"({iv['dur_ms']/1000:.1f}s)")
