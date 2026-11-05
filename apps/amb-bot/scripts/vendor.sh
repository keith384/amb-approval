#!/bin/bash
# Vercel buildCommand: vendor the Python tools + amb dispatcher + the 12 AMB
# element frames the compositor actually uses into _vendor/ so the serverless
# functions can bundle them. Runs from the project root (apps/amb-bot) with the
# full monorepo checked out, so ../../ reaches the repo. Idempotent.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$(cd "$ROOT/../.." && pwd)"
V="$ROOT/_vendor"

# On a CLI deploy only apps/amb-bot is uploaded, so the repo tools aren't reachable
# — the pre-vendored _vendor/ (uploaded with the project) is used as-is. On a
# git-integration build the whole repo is checked out, so re-vendor fresh.
if [ ! -d "$REPO/tools/storyboard" ]; then
  echo "repo tools not present (CLI deploy) — using existing _vendor/"
  [ -d "$V" ] || { echo "ERROR: no _vendor/ to use; run vendor.sh locally first"; exit 1; }
  exit 0
fi

rm -rf "$V"; mkdir -p "$V/tools" "$V/slack-bot"

cp "$REPO/apps/slack-bot/amb.py" "$V/slack-bot/amb.py"
cp -R "$REPO/tools/brand-doc" "$V/tools/brand-doc"
cp -R "$REPO/tools/storyboard" "$V/tools/storyboard"

# Drop per-tool venvs, scratch dirs, + the full 116MB figma mirror (keep 12 frames).
find "$V/tools" -type d \( -name ".venv" -o -name "work" -o -name "examples" -o -name "__pycache__" \) -exec rm -rf {} + 2>/dev/null || true
FIG_SRC="$REPO/tools/storyboard/assets/amb-figma"
FIG_DST="$V/tools/storyboard/assets/amb-figma"
rm -rf "$FIG_DST"; mkdir -p "$FIG_DST"
cp "$FIG_SRC/manifest.json" "$FIG_DST/" 2>/dev/null || true
python3 - "$REPO/apps/slack-bot/../../tools/storyboard/amb_assets.py" "$FIG_SRC" "$FIG_DST" <<'PY'
import re, sys, os, shutil
src_py, figsrc, figdst = sys.argv[1], sys.argv[2], sys.argv[3]
used = set(re.findall(r'"(\d+_AMB_[A-Za-z0-9_\-]+)"', open(src_py).read()))
n = 0
for name in used:
    p = os.path.join(figsrc, name + ".png")
    if os.path.exists(p):
        shutil.copy(p, os.path.join(figdst, name + ".png")); n += 1
print(f"vendored {n} AMB frames")
PY
echo "vendor complete → $V"
