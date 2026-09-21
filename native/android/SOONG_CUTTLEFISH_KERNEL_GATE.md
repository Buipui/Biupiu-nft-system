# Buipui Native Android — Soong / Cuttlefish / Kernel Gate

Updated: 2026-09-21

## Locked baseline

- AOSP manifest: android-latest-release -> android17-release.
- Android common GKI: android17-6.18-2026-09_r3.
- Soong: android17-release.
- Cuttlefish: upstream google/android-cuttlefish main, harvested through the latest available September 2026 commits.

## Soong integration

Primary build representation remains Android.bp. Avoid introducing Android.mk unless an upstream dependency requires it. Module names must remain unique and module conditionals should use supported Soong mechanisms.

Buipui modules:
- buipui-core: vendor cc_binary
- BuipuiControl: privileged system APK

## Cuttlefish integration

Cuttlefish is the first boot target. Latest upstream changes are treated as upstream dependencies, not copied blindly. Relevant current changes include host preparation/podcvd tooling, e2e test sharding, gfxstream updates, Bazel-7 support, and pKVM/virtualization work where supported by the selected AOSP/device configuration.

## Kernel integration

Use the locked Android 17 6.18 GKI release. Do not fork kernel/common merely to add Buipui functionality. Kernel changes require a demonstrated need and separate ABI/security validation.

## Verification ladder

SOURCE LOCKED
  -> OVERLAY CODED
  -> SOONG GRAPH CHECK
  -> BUILD
  -> CVD BOOT
  -> SERVICE HEALTH
  -> SELINUX
  -> CTS/VTS
  -> GKI/ABI
  -> AVB
  -> DEVICE

Only the first two states are currently directly evidenced in this repository. Later states require a real AOSP build host.
