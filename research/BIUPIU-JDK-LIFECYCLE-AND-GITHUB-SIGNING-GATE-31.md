# BIUPIU JDK LIFECYCLE + GITHUB SIGNING — GATE 31

Date: 21 September 2026

## JDK lifecycle
- Android CI baseline: Temurin JDK 17.
- CI asserts the JDK major version.
- Gradle/AGP compatibility remains governed by the Gradle system manifest.
- Major JDK upgrades require an explicit compatibility-matrix update and CI verification; no silent drift.

## GitHub signing boundary
Required secret names:
- `BIUPIU_ANDROID_KEYSTORE_B64`
- `BIUPIU_ANDROID_KEYSTORE_PASSWORD`
- `BIUPIU_ANDROID_KEY_ALIAS`
- `BIUPIU_ANDROID_KEY_PASSWORD`

Rules: secrets are referenced only through GitHub Actions secret contexts; no keystore or private signing material is committed; signing is release-only; missing secrets fail closed; values are never echoed or uploaded.

## Status
- JDK lifecycle policy: IMPLEMENTED
- JDK 17 CI assertion: IMPLEMENTED
- Signing workflow boundary: IMPLEMENTED
- Actual repository secrets: NOT VERIFIED/NOT CONFIGURED by this gate
- Keystore provenance: OPEN
- Signed APK/AAB: NOT VERIFIED

## Next gate
G31-A — signing-key onboarding and wrapper completion.