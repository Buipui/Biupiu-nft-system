# Buipui Native Android — Foreign-Language Harvest v1

Updated: 2026-09-21

## Harvested sources

| Language/source | Finding | Integration rule |
|---|---|---|
| Chinese AOSP mirror/documentation | SELinux is default-deny; custom policy belongs in device/vendor policy rather than modifying core policy. | Adopt as a design constraint; do not replace upstream policy. |
| Traditional Chinese AOSP documentation | SELinux remains enforcing and protects processes including privileged/root processes. | Preserve global enforcing mode. |
| Korean AOSP documentation | Android 17 security-domain compatibility includes the ashmem/memfd transition and API-level-dependent behavior. | Keep vendor policy isolated and test Android 17 compatibility paths. |
| Korean Cuttlefish documentation | Cuttlefish host setup requires KVM and provides an AOSP virtual-device validation path. | Make Cuttlefish the first boot target before physical hardware. |
| Chinese Cuttlefish documentation | AOSP Cuttlefish can be validated through x86_64/ARM64 targets and KVM. | Add automated host/KVM preflight. |

## Cross-reference outcome

The foreign-language sources independently reinforce the same architecture:

1. Upstream AOSP SELinux policy remains authoritative.
2. Buipui policy is device/vendor scoped and least-privilege.
3. Production SELinux remains enforcing.
4. Cuttlefish is the first practical boot/validation target.
5. Android 17 compatibility behavior must be tested rather than assumed.

## Harvest classification

- KEEP-AOSP: SELinux, CDD requirements, Cuttlefish, Android 17 compatibility behavior.
- KEEP-NATIVE: Buipui health/audit/acceleration/repository bridge interfaces.
- KEEP-SYSTEM-APK: privileged control/diagnostics clients after policy validation.
- RESEARCH-ONLY: third-party implementations whose provenance/license/build/security status is not verified.
- REJECT: code or policy that weakens SELinux, adds backdoors, bypasses AVB, or circumvents platform security.

Foreign-language material is evidence for cross-checking, not a license to copy unverified code.
