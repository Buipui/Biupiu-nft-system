# Buipui Native Android Housekeeping — 2026-09-21

## Consolidated state

Kept:
- AOSP upstream lock
- Soong build specification
- Cuttlefish validation target
- Android 17 6.18 GKI lock
- security architecture
- native core bootstrap
- Control APK bootstrap
- foreign-language harvest
- integration matrix/status

Rejected by policy:
- unverified third-party kernel code
- security bypasses
- permissive SELinux production configuration
- AVB bypasses
- duplicate build-system implementations
- speculative "verified" states without execution evidence

## Naming

Canonical project spelling in this native tree: Buipui.

## Verification discipline

DESIGNED, SOURCE-INTEGRATED, COMPILED, BOOT-VERIFIED, FUNCTION-VERIFIED, SECURITY-VERIFIED and DEVICE-VERIFIED are separate states.

No promotion without evidence.
