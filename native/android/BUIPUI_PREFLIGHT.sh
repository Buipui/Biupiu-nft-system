#!/bin/bash
set -euo pipefail

echo "== Buipui AOSP preflight =="

command -v repo >/dev/null || { echo "ERROR: repo tool missing"; exit 1; }
command -v git >/dev/null || { echo "ERROR: git missing"; exit 1; }

if [ ! -d .repo ]; then
  echo "ERROR: not an AOSP checkout (.repo missing)"
  exit 2
fi

if [ ! -e /dev/kvm ]; then
  echo "ERROR: /dev/kvm unavailable; Cuttlefish cannot be validated here"
  exit 3
fi

if command -v adb >/dev/null; then
  echo "ADB: present"
else
  echo "WARNING: adb not found"
fi

if command -v lunch >/dev/null 2>&1; then
  echo "Build environment appears initialized"
else
  echo "NOTE: run build/envsetup.sh before lunch"
fi

echo "Preflight checks passed. Next: apply overlay, configure product/device, build userdebug, boot Cuttlefish."
