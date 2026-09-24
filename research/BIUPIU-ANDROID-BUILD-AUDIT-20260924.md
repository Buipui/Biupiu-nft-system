# Biupiu Android Build Audit + Foreign-Language Module Harvest

Date: 2026-09-24
Branch: android-audit-20260924

## Reconciled architecture
- R&D OS Android: `mini-os/android/apps/rnd-os/`
- Biupiu World / smart farming Android: `mini-os/android/apps/world/`
- R&D OS Mobile: `mini-os/android/apps/rnd-os-mobile/`
- Canonical cross-platform runtime: `apps/shared/runtime/`

The prior shared-runtime relocation into `mini-os/android/shared/runtime/` was identified as an integration defect and removed.

## Foreign-language harvest
Japanese, German, Simplified Chinese and Traditional Chinese AOSP references confirm that a platform Android build is broader than the Gradle application layer. Candidate modules are recorded in `mini-os/android/PLATFORM-MODULE-HARVEST-v1.json`.

Sources:
- https://source.android.com/docs/setup/build?hl=ja
- https://source.android.com/docs/setup/build?hl=de
- https://source.android.com/docs/setup/build/make-to-soong?hl=de
- https://source.android.com/docs/setup/build?hl=zh-cn
- https://source.android.com/docs/setup/reference/androidbp?hl=zh-CN
- https://source.android.google.cn/docs/setup/build?hl=zh-tw

## Gate state
ANDROID_SOURCE_RECONCILIATION = IMPLEMENTED
FOREIGN_MODULE_HARVEST = IMPLEMENTED_AS_EVIDENCE
ANDROID_BUILD = OPEN_PENDING_CI
APK = NOT_VERIFIED
EMULATOR = NOT_VERIFIED
OEM_DEVICE = OPEN
AOSP_PLATFORM = OPEN
VTS_CTS = OPEN

## Governance
CHAT = interface
TXT/JSON = state
Git/repository = source
Build/test result = evidence
Handoff = machine-readable state

No foreign source is an authority override. No proprietary OEM binary or SDK was copied.
