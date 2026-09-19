#/usr/bin/env bash
set -euo pipefail
REPO="https://github.com/Wanderson-Magalhaes/blender_for_android.git"
PIN="76dc70df95ae32dcd15f3f86abfd82f4c5691140"
TARGET="${1:-engines/blender-android}"
if [ -e "$TARGET/.git" ] || [ -f "$TARGET/.git" ]; then
  git -C "$TARGET" fetch --tags origin
  git -C "$TARGET" checkout "$PIN"
else
  git clone "$REPO" "$TARGET"
  git -C "$TARGET" checkout "$PIN"
fi
echo "Blender Android pinned to $PIN"
