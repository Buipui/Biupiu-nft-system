# Buipui Native Android — Upstream Resource Lock

Updated: 2026-09-21

## Upstream baseline
- AOSP recommended release manifest: android-latest-release
- Current observed manifest update: android17-release
- AOSP Gerrit review endpoint: android-review.googlesource.com
- Android common kernel: kernel/common
- Current observed Android 17 6.18 kernel release tag: android17-6.18-2026-09_r3
- Android build: Soong/Android.bp; Bazel support is also present but described by AOSP as experimental.

## Required upstream components to evaluate
1. platform/manifest
2. build/make
3. build/soong
4. build/bazel and bazel_common_rules where required by the selected release
5. system/core
6. system/sepolicy
7. system/security
8. frameworks/base
9. packages/modules/adb
10. packages/modules/Virtualization
11. system/libbase / libcutils / libutils and required platform dependencies
12. kernel/common
13. device/google/cuttlefish for first bootable virtual target
14. CTS/VTS and relevant security test suites

## Integration rule
Do not copy arbitrary upstream code into the Biupiu repository. AOSP source is maintained as its own repo-manifest dependency. Buipiu overlays and modules belong in a separate namespace and are applied to the selected AOSP baseline.

## Current security integration candidates
- SELinux/SEAndroid policy
- Linux LSM framework
- SELinux
- lockdown
- module signing
- fs-verity/dm-verity integrity mechanisms
- Android Verified Boot / update integrity
- Keystore/KeyMint security boundary
- Binder/service isolation
- kernel hardening configuration
- KUnit/kernel self-tests where appropriate
- CTS/VTS security validation

## Verification requirement
Every imported or referenced component must pass:
LICENSE -> PROVENANCE -> COMPATIBILITY -> BUILD -> TEST -> SECURITY REVIEW -> INTEGRATION.

No automatic promotion of third-party code into kernel space.
