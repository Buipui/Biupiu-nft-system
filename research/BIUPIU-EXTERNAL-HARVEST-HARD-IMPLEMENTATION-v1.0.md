# Biupiu External Harvest — Hard Implementation Specification v1.0

**Date:** 2026-09-22  
**Status:** NATIVE CONTRACT IMPLEMENTED / EXECUTION VERIFICATION PENDING  
**Scope:** Federation, DMS, Core OS, Digital Twin, simulators, Biupiu World and research tooling

## Objective

Convert the external-harvest protocol from documentation-only guidance into enforceable native repository contracts. External patterns remain adapters and references; they do not become authoritative over Biupiu OS controls.

## Hard implementation rules

1. Every harvested resource requires an immutable identity, source, version and repository placement.
2. Existing repository modules must be checked before any update is proposed.
3. Updates are permitted only when the candidate is demonstrably newer and compatibility impact is recorded.
4. No resource can reach `VERIFIED_WORKING` without static, build, security, regression and runtime evidence.
5. `REPOSITORY_VERIFIED_UNTESTED` is never treated as production-ready.
6. Failed, unsafe, incompatible or licence-blocked resources must be moved to `QUARANTINED` with a reason and evidence reference.
7. Superseded versions remain available for lineage and rollback; they are not silently overwritten.
8. Learning records must preserve old state, new state, test evidence, failure signatures, remediation and promotion decision.
9. Blockchain records may anchor hashes and release identities only; confidential data, secrets and unpublished IP remain off-chain.
10. Runtime authority remains with the Core OS/DMS policy boundary and requires human-approved promotion.

## Native implementation

- `packages/biupiu-rnd-os/src/federation-harvest-gate.ts`
- `HarvestRecord` captures identity, version, placement, status and evidence.
- `evaluateHarvestPromotion()` fails closed when any required gate is incomplete.
- `quarantineHarvest()` requires a non-empty quarantine reason.

## Required execution gates

`INVENTORY -> VERSION-COMPARE -> PROVENANCE -> LICENCE/IP -> NORMALISE -> STATIC TEST -> BUILD -> SECURITY -> REGRESSION -> RUNTIME -> LEARNING RECORD -> INDEX UPDATE -> HUMAN PROMOTION`

## Cross-system placement

- Federation: transport, capability, telemetry and lifecycle adapters.
- Core OS/DMS: authorization, entitlement, audit and authoritative state.
- Digital Twin: twin/live separation, correlation and delivery metadata.
- Simulators/World: engine-neutral manifests, compatibility and sandbox boundaries.
- NFT/IP: provenance, algorithm/version lineage, hashes and rights classification.
- Learning: failure/remediation records and regression-test generation inputs.

## Verification boundary

This commit adds native validation logic and the implementation specification. It does not claim that the complete repository has been compiled, that all tests have executed, that external adapters are runtime-safe, or that blockchain anchoring has occurred. Those remain explicit execution gates.
