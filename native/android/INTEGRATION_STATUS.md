# Buipui Native Android — Integration Status

## Current gate

**SOURCE-INTEGRATION PACK: IMPLEMENTED**

Implemented in branch native-android/aosp-foundation:

- AOSP upstream resource lock
- ROM/APK integration matrix
- Foreign-language cross-reference/harvest record
- AOSP integration specification
- Native Buipui core bootstrap daemon
- Soong build definition
- init service declaration
- minimal vendor SELinux domain and file context
- privileged Control APK bootstrap
- host/AOSP/Cuttlefish preflight script

## Evidence-backed constraints

Android 17 CDD requires SELinux enforcing and prohibits weakening/replacing upstream neverallow rules. Vendor-specific services must remain outside AOSP coredomains. AVB/Keystore/KeyMint remain platform security boundaries.

## Not yet verified

- AOSP repo sync on a real build host
- clean Soong compilation
- Cuttlefish boot
- native daemon runtime
- SELinux policy compilation with the selected device configuration
- CTS/VTS
- AVB signing and boot-chain verification
- physical device HAL/device-tree bring-up

No item above is marked verified until the corresponding command/result exists.
