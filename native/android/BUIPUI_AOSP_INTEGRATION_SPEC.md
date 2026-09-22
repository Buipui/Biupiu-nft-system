# Buipui AOSP Native Integration Specification v1

## Objective
Provide a reproducible overlay that can be applied to an AOSP android-latest-release/android17-release checkout without treating the Buipui project repository as an AOSP source mirror.

## Modules

- buipui-core: native health/audit daemon.
- buipui-control: privileged system APK/client boundary.
- buipui-sepolicy: minimal vendor/device SELinux policy.
- buipui-init: init service declaration.
- buipui-build: Soong module definitions.
- buipui-validation: host preflight and device smoke checks.

## Security invariants

- No SELinux permissive mode in production.
- No modification/removal of upstream neverallow rules.
- No AOSP coredomain assignment to Buipui/vendor services.
- AVB remains enabled at the product/device layer.
- KeyMint/Keystore remains the platform cryptographic boundary.
- Buipui services run with least privilege and explicit SELinux domains.
- Repository/intelligence inputs are treated as untrusted data at the native boundary.

## Verification states

DESIGNED -> SOURCE-INTEGRATED -> COMPILED -> BOOT-VERIFIED -> FUNCTION-VERIFIED -> SECURITY-VERIFIED -> DEVICE-VERIFIED.

This repository currently establishes the source integration pack. Compile/boot/security/device verification require an actual AOSP checkout and build host.
