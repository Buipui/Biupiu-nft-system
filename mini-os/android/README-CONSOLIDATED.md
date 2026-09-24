# Biupiu Mini Android OS — Consolidated Android Build Tree v1.1

- `mini-os/android/apps/rnd-os/` — native R&D OS Android shell
- `mini-os/android/apps/world/` — Biupiu World / smart-farming Android client
- `mini-os/android/apps/rnd-os-mobile/` — R&D OS mobile client
- `apps/shared/runtime/` — canonical cross-platform runtime

The earlier relocation of the shared runtime into `mini-os/android/shared/runtime/` was identified by the deep audit as an integration defect and removed.

External Android/Blender resources remain attributed and quarantined/reference-only unless build, dependency, runtime and licence gates pass.

Source-tree consolidation does not imply APK, emulator, OEM-device, HIL or production verification.
