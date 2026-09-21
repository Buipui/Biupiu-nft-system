# Buipui Native Android — Integration Matrix v1

## ROM core
AOSP platform: REQUIRED
Kernel: REQUIRED
Device/vendor/HAL: REQUIRED
Build system: REQUIRED
Boot/recovery/update: REQUIRED
SELinux policy: REQUIRED
Verified boot/integrity: REQUIRED

## Buipui native
System Core: SYSTEM SERVICE / NATIVE LIBRARY
Intelligence: SYSTEM SERVICE + APK interface
DMS: SYSTEM SERVICE + APK interface
Security/Audit: SYSTEM SERVICE + NATIVE SECURITY LIBRARIES
Diagnostics: SYSTEM SERVICE + APK
Acceleration: NATIVE SERVICE/LIBRARY, with kernel work only where justified
Repository bridge: SYSTEM SERVICE/API boundary

## APK track
Control Centre: APK
Intelligence client: APK
DMS client: APK
Diagnostics/security dashboard: APK
Research modules: APK unless system privilege is demonstrably required

## Virtual validation target
Cuttlefish is the first integration target because it provides a configurable Android virtual device and is actively maintained. It is a validation target, not a substitute for physical-device HAL/device-tree work.

## Kernel security policy
Prefer existing upstream/AOSP mechanisms over new kernel code. Evaluate LSM, SELinux, lockdown, module signing, integrity mechanisms, and kernel hardening before introducing any custom security module.

## Gate
This matrix is integrated into the planning branch. Actual AOSP source synchronization, compilation, Cuttlefish boot, and physical-device bring-up remain separate verification gates.
