#!/usr/bin/env python3
"""
Mirror the official Messaging Advisory AMB screens out of the shared Figma into a
local asset library (tools/storyboard/assets/amb-figma/) + manifest.json so the
storyboard renderer can composite against pixel-perfect Apple chrome.

    FIGMA_TOKEN=... python fetch_amb_assets.py [figma_file_key]

Dedupes the ~124 unique `NN_AMB_<Category>_<Name>` frames (they appear twice across
the file's two pages), exports each as PNG, and writes manifest.json.
"""
from __future__ import annotations
import json, os, re, sys, urllib.parse, urllib.request

K = sys.argv[1] if len(sys.argv) > 1 else "Wxm5RpbOVOCnow04AUE3pK"
T = os.environ["FIGMA_TOKEN"]
SCALE = os.environ.get("AMB_ASSET_SCALE", "1")
BASE = os.path.join(os.path.dirname(__file__), "assets", "amb-figma")
os.makedirs(BASE, exist_ok=True)


def api(url: str):
    req = urllib.request.Request(url, headers={"X-Figma-Token": T})
    return json.load(urllib.request.urlopen(req, timeout=60))


def main():
    doc = api(f"https://api.figma.com/v1/files/{K}?depth=4")["document"]
    seen: dict[str, str] = {}

    def walk(n):
        nm = n.get("name", "")
        if re.match(r"\d+_AMB_", nm) and n.get("type") == "FRAME" and nm not in seen:
            seen[nm] = n["id"]
        for c in n.get("children", []):
            walk(c)

    walk(doc)
    items = list(seen.items())
    print(f"{len(items)} unique AMB frames → exporting at scale {SCALE}", flush=True)

    manifest = {}
    for i in range(0, len(items), 15):
        batch = items[i:i + 15]
        ids = ",".join(nid for _, nid in batch)
        r = api(f"https://api.figma.com/v1/images/{K}?ids={urllib.parse.quote(ids)}&format=png&scale={SCALE}")
        imgs = r.get("images") or {}
        name_by_id = {nid: nm for nm, nid in batch}
        for nid, u in imgs.items():
            if not u:
                continue
            nm = name_by_id[nid]
            urllib.request.urlretrieve(u, os.path.join(BASE, f"{nm}.png"))
            manifest[nm] = {"node": nid, "file": f"assets/amb-figma/{nm}.png"}
        print(f"  batch {i // 15 + 1}/{(len(items) + 14) // 15}: {len(manifest)} total", flush=True)

    json.dump({"figma_file": K, "scale": SCALE, "count": len(manifest), "screens": manifest},
              open(os.path.join(BASE, "manifest.json"), "w"), indent=2)
    print(f"done — {len(manifest)} screens + manifest.json", flush=True)


if __name__ == "__main__":
    main()
