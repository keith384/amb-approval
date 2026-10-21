"""
Stage 2 — OCR to a timed, side-tagged transcript.

Apple Vision (via ocrmac) reads every frame kept after a visual-diff dedup
(consecutive 5 fps frames are near-identical; the dedup both cuts OCR cost and
marks screen-change boundaries used by event detection in stage 3).

Each kept frame yields text tokens with a normalized bbox and a side tag
(customer = right-aligned, business = left-aligned) from the token's horizontal
center. Output: ocr.json keyed by frame idx. Idempotent/cached.
"""
from __future__ import annotations
import json
from pathlib import Path

import cv2
import numpy as np


def _phash_gray(img, size: int = 32):
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.resize(g, (size, size), interpolation=cv2.INTER_AREA).astype(np.int16)


def _diff(a, b) -> float:
    return float(np.mean(np.abs(a - b))) if a is not None and b is not None else 1e9


def ocr_frames(work_dir: str, diff_threshold: float = 2.0, limit: int | None = None,
               engine: str = "vision") -> dict:
    out = Path(work_dir)
    manifest = json.loads((out / "frames.json").read_text())
    frames = manifest["frames"]
    if limit:
        # Evenly sample for a quick quality check.
        idxs = np.linspace(0, len(frames) - 1, limit).astype(int)
        frames = [frames[i] for i in idxs]

    from ocrmac import ocrmac  # Apple Vision; imported here so extract works without it

    results = {}
    prev_sig = None
    kept = 0
    for fr in frames:
        img = cv2.imread(str(out / fr["path"]))
        sig = _phash_gray(img)
        changed = limit is not None or prev_sig is None or _diff(prev_sig, sig) >= diff_threshold
        if not changed:
            results[str(fr["idx"])] = {"t_ms": fr["t_ms"], "dup_of": kept_idx, "tokens": None}
            continue
        prev_sig = sig
        kept_idx = fr["idx"]
        kept += 1

        anns = ocrmac.OCR(str(out / fr["path"]), framework="vision").recognize()
        h, w = img.shape[:2]
        tokens = []
        for text, conf, bbox in anns:
            # Vision bbox is normalized [x, y, width, height] with origin bottom-left.
            bx, by, bw, bh = bbox
            cx = bx + bw / 2.0
            top = 1.0 - (by + bh)  # convert to top-left-origin y
            side = "customer" if cx > 0.52 else ("business" if cx < 0.48 else "center")
            tokens.append({
                "text": text, "conf": round(float(conf), 3),
                "x": round(bx, 4), "y": round(top, 4), "w": round(bw, 4), "h": round(bh, 4),
                "side": side,
            })
        results[str(fr["idx"])] = {"t_ms": fr["t_ms"], "dup_of": None, "tokens": tokens}

    payload = {
        "engine": engine,
        "diff_threshold": diff_threshold,
        "total_frames": len(frames),
        "ocr_frames": kept,
        "frames": results,
    }
    if not limit:
        (out / "ocr.json").write_text(json.dumps(payload))
    return payload


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("work_dir")
    ap.add_argument("--limit", type=int, default=None, help="evenly-sample N frames (quality check)")
    ap.add_argument("--threshold", type=float, default=2.0)
    ap.add_argument("--show", action="store_true", help="print recognized text per frame")
    a = ap.parse_args()
    p = ocr_frames(a.work_dir, a.threshold, a.limit)
    print(f"OCR'd {p['ocr_frames']} of {p['total_frames']} frames "
          f"(dedup threshold {p['diff_threshold']}).")
    if a.show:
        for idx, fr in p["frames"].items():
            if fr["tokens"] is None:
                continue
            line = " | ".join(f"{t['side'][0]}:{t['text']}" for t in fr["tokens"] if t["conf"] > 0.3)
            s, ms = divmod(fr["t_ms"], 1000); m, s = divmod(s, 60)
            print(f"[{m:02d}:{s:02d}] {line[:160]}")
