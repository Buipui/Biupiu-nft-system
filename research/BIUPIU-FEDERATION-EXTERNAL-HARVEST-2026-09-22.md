# Biupiu Federation External Harvest — 2026-09-22

## Purpose
Identify missing federation capabilities and integrate only architecture/contracts compatible with Biupiu's fail-closed, provenance-first native architecture.

## Harvested patterns

### OpenUSD
OpenUSD separates scene foundations, composition, imaging and plugins, with extension points for asset resolution and file-format plugins. Biupiu rule: core contracts remain stable; World/renderer/import/export integrations are adapters.

### Eclipse Ditto
Ditto separates stable twin protocols from transport bindings and distinguishes persisted twin communication from live device communication. Biupiu requires transport-neutral envelopes, twin/live separation, correlation IDs, payload mapping and delivery policy.

### OPC UA PubSub
Used as an industrial adapter/reference pattern for site/DMS federation. It does not become authoritative over Biupiu OS.

### AUTOSAR Adaptive
Communication, storage, security, safety, diagnostics, cryptography, health, execution, state and update/configuration are treated as reference concerns only. No proprietary implementation or restricted material is copied.

### OpenTelemetry
Biupiu adopts the pattern of immutable propagated context and common event attributes without importing an OTel SDK into the core.

## Foreign-language/OEM lane
Discovery across Chinese, Japanese, Korean, German, French, Italian, Spanish, Portuguese and Russian sources remains subject to provenance, licence, security and testing gates. Translation is discovery assistance, never evidence or permission.

Adapter/reference candidates include CAN/CAN-FD, SOME/IP, AUTOSAR Adaptive, OPC UA, MQTT, Modbus, FMI, DDS/ROS 2 and STEP/AP242/PLM interoperability.

## Missing federation modules
1. Capability discovery/version negotiation
2. Health/readiness and queue-depth telemetry
3. Trace/correlation context
4. Schema/content-type/hash references
5. Delivery/retry/TTL policy
6. Twin-vs-live boundary
7. Security/authorization boundary
8. Clock-skew/time-quality observation
9. Backpressure/dead-letter handling
10. Adapter lifecycle and graceful close
11. Cross-simulator observation schema
12. Placement/provenance registry

## Native integration
Existing federation contracts and gates F17–F22 remain in place. The following hard implementation has now been added:

- `packages/biupiu-rnd-os/src/federation-harvest-gate.ts`
- `research/BIUPIU-EXTERNAL-HARVEST-HARD-IMPLEMENTATION-v1.0.md`

The native validator provides:
- immutable identity/version/evidence record shape;
- fail-closed promotion evaluation;
- mandatory provenance and licence/IP review flags;
- static, build, security, regression and runtime evidence requirements;
- test-reference requirements;
- explicit quarantine with a mandatory reason;
- status support for candidate, repository-verified-untested, verified-working, quarantined and superseded records.

## Hard promotion rule
`INVENTORY -> VERSION-COMPARE -> PROVENANCE -> LICENCE/IP -> NORMALISE -> STATIC TEST -> BUILD -> SECURITY -> REGRESSION -> RUNTIME -> LEARNING RECORD -> INDEX UPDATE -> HUMAN PROMOTION`

A candidate is not `VERIFIED_WORKING` unless all required evidence flags pass. Existing modules must be checked first, and an update is allowed only when it is demonstrably newer and compatibility impact is recorded.

## Learning and blockchain boundary
Bug fixes, conflicts, test outcomes and remediation must preserve old/new lineage. Approved release identities and hashes may later be anchored through the Biupiu registry. Raw learning data, secrets, confidential research and unpublished IP remain off-chain. No autonomous training or blockchain transaction is claimed by this protocol update.

## Verification status
**NATIVE VALIDATION LOGIC: IMPLEMENTED.**  
**FULL REPOSITORY BUILD, TEST EXECUTION, SECURITY SCAN AND RUNTIME ADAPTER VERIFICATION: PENDING.**

External patterns never become authoritative merely because they are popular, OEM-derived, foreign-language or open-source.
