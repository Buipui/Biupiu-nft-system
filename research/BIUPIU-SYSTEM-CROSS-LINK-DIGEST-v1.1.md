# BIUPIU SYSTEM CROSS-LINK + LIBRARY DIGEST v1.1

Date: 2026-09-22
Repository: Buipui/Biupiu-nft-system
Base commit reviewed: de10eb1fd0f673f3d294d0f0333cb01075b48f61

## Purpose
Single cross-link map for the current Biupiu OS, Intelligence/AI, Digital Twin, federation, simulators, NFT/EVM and Biupiu World boundaries. This digest is an index/architecture record; it does not create a second authority.

## Canonical system chain
RESEARCH / EVIDENCE
-> BIUPIU INTELLIGENCE
-> AI/ML PROPOSAL
-> CORE OS/DMS VALIDATION
-> DIGITAL TWIN
-> FEDERATION CONTRACT
-> DOMAIN SIMULATOR / ADAPTER
-> OBSERVATION
-> LEARNING EVIDENCE
-> REGRESSION
-> RELEASE / HUMAN GATE

## Cross-system ownership
| System | Owns | May consume | Must not become |
|---|---|---|---|
| R&D / Research | evidence, hypotheses, provenance, research records | all validated system observations | executable authority by publication alone |
| Intelligence / AI | classification, retrieval, learning proposals, routing | research + runtime evidence | authoritative OS writer |
| Core OS / DMS | validated execution/state authority | governed proposals/contracts | uncontrolled AI target |
| Digital Twin | state representation and twin events | OS/simulator/federation observations | physical truth |
| Federation | discovery, transport-neutral contracts, health, trace, delivery, reconciliation | all approved adapters | authority bypass |
| Simulators | domain models and numerical results | versioned inputs/contracts | physical certification without correlation |
| Biupiu World | visualization/runtime presentation and World-only state | versioned simulator/twin/federation outputs | simulator or OS authority |
| NFT/EVM | token/provenance/accounting adapters | approved identity/provenance data | simulator/OS authority |

## Federation modules now linked
F17 capability discovery/version negotiation
F18 observability: trace, correlation, health, queue depth, clock skew
F19 schema governance: schema/version/content type/hash
F20 delivery resilience: retry, TTL, backpressure, dead-letter
F21 industrial adapters: OPC UA/MQTT/OEM boundary/transport neutrality
F22 World repository boundary and migration plan

Shared contract: packages/biupiu-rnd-os/src/federation-contracts.ts
Smoke contract: packages/biupiu-rnd-os/src/federation-contracts.test.ts

## External library/pattern digest
- OpenUSD -> World composition/plugin/adapter boundary pattern.
- Eclipse Ditto -> twin protocol versus transport separation.
- OPC UA PubSub -> industrial publish/subscribe and information-model adapter pattern.
- AUTOSAR Adaptive -> service, health, security, diagnostics, state/update concern map; reference only.
- OpenTelemetry -> propagated trace/context and semantic-event pattern; core remains dependency-light.
- MQTT, Kafka, AMQP, DDS/ROS 2, Modbus, FMI/co-simulation, CAN/CAN-FD, SOME/IP -> adapter/reference lane.
- Foreign-language repositories -> discovery/translation assistance only; evidence, licence and provenance remain independent gates.
- OEM material -> adapter/reference only; no proprietary implementation or restricted material.

## Coding/governance cross-link
All native modules are governed by:
research/BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0.md

Verification ladder:
L0 syntax/import/schema
L1 unit
L2 integration/contract
L3 static/type/lint/security
L4 clean build
L5 smoke
L6 regression
L7 cross-platform/runtime
L8 hardware/device/physical correlation
L9 release

## Evidence and learning rule
External research, harvested modules, simulator outputs and AI-generated code remain non-authoritative until provenance, licence/IP, security, compatibility, build, smoke and regression requirements are satisfied.

Learning remains append-only evidence first:
input -> prior state -> outcome -> expected -> residual/error -> uncertainty -> failure class -> changed components -> regression -> model/code version -> provenance -> promotion decision.

## Repository placement rule
NFT/core repository:
- contracts, evidence, shared interfaces, provenance, adapters, research manifests.

Biupiu World repository:
- World runtime, UE5 project, World-only assets, World deployment/tests once the destination repository is initialized.

No duplicate authoritative implementation is created during migration.

## Current gate chain
STATIC_SOURCE_AUDIT: complete
EXTERNAL_HARVEST_PROVENANCE: complete at architecture/registry level
REPOSITORY_PLACEMENT_AUDIT: complete
CONTRACT_SMOKE: executed at source-contract inspection level; runtime CI evidence still open
PACKAGE_BUILD: open
ANDROID_BUILD: open
UNIT_TEST: open for fresh current-head execution
EMULATOR_OR_DEVICE: open
CROSS_SYSTEM_RUNTIME: open
REGRESSION: open
VERIFIED: open

## Housekeeping rule
Dead/duplicate/unreachable/obsolete executable code is removed only when lineage is unambiguous. Historical failures, research hypotheses, unverified assets and external references are classified/quarantined rather than silently deleted.

Status: INTEGRATED DIGEST v1.1
