# Biupiu G32-D — Android Keystore / Runtime Validation

## Status
IMPLEMENTED_NOT_VERIFIED

## Implemented
- Current R&D OS security policy is present in `apps/android`.
- Current runtime session contract requires an active session and nonblank subscriber ID.
- Android manifest explicitly denies cleartext traffic and backup of sensitive domains.
- Current `software/rnd-os-mobile` contains a real AndroidKeyStore AES-GCM session store.
- Native unit tests were added for the security policy.
- Security CI now pins the verified checkout/setup-java/Gradle action references by full commit SHA and runs `gradle :app:testDebugUnitTest`.

## Verification boundary
- Latest Security Gate and related workflows are queued; no new runtime/build pass is claimed yet.
- Physical Android/OEM Keystore validation remains open.
- Signed APK/AAB verification remains open because repository signing secrets and committed Gradle wrappers are not yet verified.

## Next
G32-E — inspect workflow results, fix any failures, then verify Android build/test and signing boundaries.
