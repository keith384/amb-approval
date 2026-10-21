"""
Stage 1 — frame extraction.

Samples an iPhone POV recording at a fixed rate (default 5 fps, per MA's recording
guide / the build plan) and writes JPEG frames plus a frames.json index. Pure
OpenCV so no system ffmpeg is required; the decode is deterministic (frame index /
source fps = timestamp), which the latency rules in later stages depend on.
"""
from __future__ import annotations
import json
from dataclasses import dataclass, asdict
from pathlib import Path

import cv2


@dataclass
class Frame:
    idx: int          # sequential sampled-frame number (0-based)
    src_frame: int    # frame number in the source video
    t_ms: int         # timestamp in milliseconds from video start
    path: str         # relative path to the JPEG


def _fmt_ts(t_ms: int) -> str:
    s, ms = divmod(t_ms, 1000)
    m, s = divmod(s, 60)
    return f"{m:02d}:{s:02d}.{ms:03d}"


def extract_frames(video_path: str, out_dir: str, target_fps: float = 5.0,
                   jpeg_quality: int = 90) -> dict:
    """Extract frames at target_fps. Returns the manifest dict (also written to frames.json)."""
    vp = Path(video_path)
    if not vp.exists():
        raise FileNotFoundError(video_path)
    out = Path(out_dir)
    frames_dir = out / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(vp))
    if not cap.isOpened():
        raise RuntimeError(f"OpenCV could not open {video_path}")

    src_fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    src_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Sample every Nth source frame to approximate target_fps.
    step = max(1, round(src_fps / target_fps))
    effective_fps = src_fps / step

    frames: list[Frame] = []
    src_i = 0
    sampled = 0
    ok, img = cap.read()
    while ok:
        if src_i % step == 0:
            t_ms = int(round((src_i / src_fps) * 1000))
            rel = f"frames/f{sampled:05d}.jpg"
            cv2.imwrite(str(out / rel), img, [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality])
            frames.append(Frame(idx=sampled, src_frame=src_i, t_ms=t_ms, path=rel))
            sampled += 1
        src_i += 1
        ok, img = cap.read()
    cap.release()

    manifest = {
        "video": str(vp),
        "source": {
            "fps": round(src_fps, 4),
            "frame_count": src_count,
            "width": width,
            "height": height,
            "duration_ms": int(round((src_count / src_fps) * 1000)) if src_count else None,
        },
        "sampling": {"target_fps": target_fps, "step": step, "effective_fps": round(effective_fps, 4)},
        "frame_count": len(frames),
        "first_ts": _fmt_ts(frames[0].t_ms) if frames else None,
        "last_ts": _fmt_ts(frames[-1].t_ms) if frames else None,
        "frames": [asdict(f) for f in frames],
    }
    (out / "frames.json").write_text(json.dumps(manifest, indent=2))
    return manifest


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("out_dir")
    ap.add_argument("--fps", type=float, default=5.0)
    a = ap.parse_args()
    m = extract_frames(a.video, a.out_dir, a.fps)
    src = m["source"]
    print(f"Extracted {m['frame_count']} frames @ {m['sampling']['effective_fps']}fps "
          f"from {src['width']}x{src['height']} {src['fps']}fps video "
          f"({m['first_ts']} → {m['last_ts']}).")
