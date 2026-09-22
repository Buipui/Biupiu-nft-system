# Buipui Native Android — Best ROM Gate 2026-09-21

## Gate
ROM-BEST-03 — Security-first ROM integration candidate gate

## Decision
The first implementation candidate is **GrapheneOS hardened_malloc**, because its upstream documentation explicitly supports Android Bionic and the current Android 17 release branch, while providing a defined integration path and test suite. This is a candidate promotion, not a claim of compilation or runtime verification.

## Locked target
- AOSP: android-latest-release / android17-release
- Kernel target: Buipui locked Android 17 6.18 GKI baseline
- Architecture: arm64 / 64-bit
- Security invariants: SELinux enforcing, AVB, KeyMint/Keystore, Android sandboxing

## Candidate implementation order
1. hardened_malloc/Bionic compatibility branch — SECURITY PRIORITY
2. CalyxOS SeedVault Android-17 compatibility port
3. CalyxOS Datura-style network policy integration through Buipui Enterprise Policy Broker
4. crDroid modular SystemUI/Settings features, selectively and without replacing Android security authorities
5. LineageOS device/release/updater discipline

## hardened_malloc constraints
Upstream currently documents Android support for android17-release and requires attention to virtual-memory mapping capacity. The project supports Bionic and provides automated tests. Its documented Android integration uses Bionic rather than an unrestricted LD_PRELOAD-style approach.

Buipui must NOT:
- copy signing keys or proprietary blobs
- bypass AVB/KeyMint/Keystore
- weaken SELinux
- modify AOSP neverallow rules
- blindly replace Bionic before ABI/API/build validation
- enable configuration changes without measured regression evidence

## Proposed build integration
Phase A: vendor/source import with exact upstream commit recorded.
Phase B: build as isolated candidate target.
Phase C: Bionic integration patch review.
Phase D: clean AOSP build.
Phase E: Cuttlefish boot.
Phase F: allocator tests + Android smoke tests.
Phase G: SELinux/AVB/CTS/VTS/security regression.
Phase H: only then promote to platform baseline.

## Evidence state
RESEARCH/SOURCE: VERIFIED
ARCHITECTURE: SOURCE-INTEGRATED
CODE PORT: NOT EXECUTED
COMPILED: NOT VERIFIED
BOOT: NOT VERIFIED
FUNCTION: NOT VERIFIED
SECURITY: NOT VERIFIED
DEVICE: NOT VERIFIED
ENTERPRISE CONFORMANCE: NOT VERIFIED

## Blocker
The repository currently contains the Buipui overlay and gate documentation, not a synchronized AOSP checkout. Therefore a real ROM compilation/boot cannot honestly be claimed from GitHub-only execution.

## Next executable action
On a Linux AOSP build host, execute the candidate in isolation before integrating any other ROM-family feature. Preserve all logs and test artifacts in the federation evidence chain.
