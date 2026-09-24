# Biupiu Mini Android OS — Consolidated Android Build Tree v1.0

All first-party Android application build roots formerly split across:
- apps/android
- smart-farming/android
- software/rnd-os-mobile

are now consolidated beneath this Mini OS tree.

```
mini-os/android/
├── app/                         # Mini OS host application
├── apps/
│   ├── rnd-os/                  # former apps/android
│   ├── world/                   # former smart-farming/android
│   └── rnd-os-mobile/           # former software/rnd-os-mobile
├── federation/                  # capability/adapters
├── shared/runtime/              # shared runtime code
└── BIUPIU-MINI-ANDROID-OS-CONSOLIDATION-v1.json
```

The moved projects retain their own Gradle project files so their original build boundaries remain explicit. The R&D OS shell's shared-runtime path was corrected for the new location.

External Android/Blender resources remain attributed and quarantined/reference-only unless their build, dependency and licence gates are passed.

No APK/device/runtime verification is implied by this source relocation.
