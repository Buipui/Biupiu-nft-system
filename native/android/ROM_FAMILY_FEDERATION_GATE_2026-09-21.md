# Buipui Native Android — ROM Family Multi-AI Federation Gate 2026-09-21

## Gate
ROM-FED-02: LineageOS + crDroid + GrapheneOS + CalyxOS harvest and optimisation.

## Multi-AI task lanes
- RESEARCHER: canonical source, foreign-language and XDA discovery.
- SECURITY: license/provenance/security-boundary review.
- BUILDER: AOSP/Soong compatibility and port feasibility.
- VALIDATOR: compile, boot, CTS/VTS and feature tests.
- HOUSEKEEPER: deduplicate, pin commits, remove stale references.
- ORCHESTRATOR: merge evidence; never override security authority.

## Evidence required for promotion
SOURCE -> exact repository/commit -> license -> dependency graph -> patch/port -> build result -> runtime test -> security test -> promotion decision.

## Executed harvest findings
- LineageOS: support/release discipline and reproducible device-tree/extraction practices are reusable.
- crDroid: modular customization and Settings/SystemUI architecture are reusable; attestation-spoofing mechanisms are excluded.
- GrapheneOS: hardened_malloc is the highest-priority security engineering candidate; Vanadium is a reference architecture rather than a blind transplant.
- CalyxOS: SeedVault and Datura are reusable architectural candidates, subject to Android 17 porting and tests.
- XDA/foreign-language/OpenBooks inputs remain corroboration/discovery unless canonical source and license are established.

## Promotion status
ROM-FAMILY HARVEST: SOURCE-VERIFIED
OPTIMISATION PLAN: SOURCE-INTEGRATED
CODE PORTS: NOT YET COMPILED
BOOT: NOT VERIFIED
FUNCTION: NOT VERIFIED
SECURITY: NOT VERIFIED
DEVICE: NOT VERIFIED
ENTERPRISE-CONFORMANCE: NOT VERIFIED

## Next executable build gate
On a real AOSP host:
1. sync android-latest-release/android17-release.
2. verify locked Android 17 6.18 GKI r3.
3. build clean baseline.
4. apply Buipui overlay.
5. prototype each candidate module one at a time.
6. build/boot Cuttlefish after each security-sensitive change.
7. run SELinux/AVB/CTS/VTS and module-specific tests.
8. retain failed candidates without silently removing evidence.
