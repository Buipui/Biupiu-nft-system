# Buipui OS — ROM Optimisation Matrix v1.0

| Capability | Source family | Buipui action | Authority |
|---|---|---|---|
| Device/release discipline | LineageOS | Adopt support checklist concepts | Buipui release gate |
| SELinux enforcing | LineageOS/AOSP | Retain as hard invariant | AOSP security |
| Public source + dependency hygiene | LineageOS/crDroid | Adopt provenance gate | Federation |
| System customization | crDroid | Port selectively through Buipui Settings/SystemUI modules | Buipui UI |
| Privacy indicators | crDroid/AOSP | Keep and expose through Control Centre | Android framework |
| App sandbox/isolation concepts | crDroid/GrapheneOS | Research and implement only through Android-supported boundaries | Android security |
| Hardened memory allocator | GrapheneOS | Prototype compatibility branch for hardened_malloc/Bionic | Kernel/libc security |
| Browser/WebView hardening | GrapheneOS | Research Vanadium architecture; no blind transplant | Application security |
| Encrypted backup | CalyxOS SeedVault | Prototype Android-17-compatible integration | Data protection |
| Per-app firewall | CalyxOS Datura | Prototype as policy-controlled network layer | Enterprise/DMS |
| OTA/update discipline | LineageOS/crDroid/CalyxOS/AOSP | Consolidate under one Buipui updater authority | Release system |
| Enterprise management | AOSP Enterprise | Keep DevicePolicyManager/managed profiles | Enterprise broker |
| Multi-AI evidence/audit | Buipui | Federation remains sole orchestration/evidence authority | Buipui |
| AVB/KeyMint/Keystore | AOSP/GrapheneOS security model | Preserve; no alternate authority | Platform security |

## Explicit non-promotions
crDroid Integrity/attestation spoofing controls are excluded from Buipui's trusted security baseline. Any compatibility research is isolated and never allowed to alter attestation truth, AVB, KeyMint or enterprise policy.

## Optimisation sequence
1. Security primitives: hardened allocator compatibility study.
2. Privacy/network controls: Datura-style policy model.
3. Backup: SeedVault port/compatibility study.
4. UI: crDroid customization selectively implemented without fragmenting SystemUI.
5. Browser/WebView: Vanadium architecture study.
6. Enterprise: wrap all privileged actions in the existing audited Policy Broker.
7. Federation: log proposal, source commit, build result and runtime evidence for every promoted module.
