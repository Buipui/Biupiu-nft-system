# Biupiu Android Federation Housekeeping / Extermination / Smoke / Fault Log — 2026-09-24

Status: SOURCE-LEVEL HOUSEKEEPING COMPLETE / EXECUTABLE SMOKE GATE OPEN

## Build status

The Android CI workflow is configured for JDK 17, Android SDK 35, Gradle 8.9, unit tests, assembleDebug and repository source sanity checks.

Current commit status for the integration branch is PENDING with zero reported CI statuses. Therefore no successful Gradle build is claimed.

## Static smoke checks

- Android Gradle source-set change is present.
- NativeIntelligenceFederationAdapter is present.
- NativeIntelligenceFederationAdapterTest is present.
- Standalone machine-readable integration record is present.
- Foreign-language harvest record is present.
- Native system catalogue remains canonical.
- External material remains reference/candidate/quarantine classified.
- Existing source sanity rule blocks the legacy duplicate federation transport-interface path.

## Extermination / housekeeping

No destructive deletion was performed where lineage was ambiguous. The existing ExternalTransportAdapter interface under the Android application source tree remains the known transport contract; adapter implementations reference it. The new native-intelligence bridge deliberately does not duplicate that transport interface.

Potential duplicate or obsolete material is classified rather than silently deleted.

## Fault findings

1. CI evidence gap — OPEN. No observed workflow result is attached to the current integration commit.
2. Runtime evidence gap — OPEN. Android device, GPU/Vulkan, NPU, Android Auto and hardware gates remain unverified.
3. Foreign-module evidence gap — CONTROLLED. External candidates have no promotion authority until gates pass.
4. AOSP platform boundary — OPEN. Mini OS application build is distinct from a complete AOSP/Pixel platform build.

## Smoke-test contract

A successful run must record BUILD_ID, COMMIT, JDK, Gradle, SDK, unit-test result, APK output, warnings, source-sanity result, dependency resolution and failure fingerprint.

## Learning/failure memory

Failures remain retained. Repeated failure without new evidence is a stalled gate. A fix becomes promotable only after regression evidence and provenance are recorded.
