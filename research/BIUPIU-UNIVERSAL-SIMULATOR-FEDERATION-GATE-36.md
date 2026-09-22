# Biupiu Universal Simulator Federation — Gate 36

Status: SOURCE CONTRACT VERIFIED / ARCHITECTURE INTEGRATED / RUNTIME FEDERATION PENDING

## Universal contract
Every simulator is a provider of versioned state transitions, not an authority over the whole system.

UNIVERSAL SIMULATOR:
INPUT -> VALIDATE -> NORMALIZE -> STEP -> OBSERVE -> TWIN UPDATE -> EVENT LOG -> LEARNING RECORD -> PROVENANCE -> FEDERATION

Domains:
AUTOMOTIVE / MARINE / AEROSPACE / SPACE / FARMING / ROBOTICS / MATERIALS / PHYSICS / MATH / QUANTUM / MANUFACTURING

## Federation
Federation is a discovery and orchestration layer. It may run multiple simulators against the same scenario, compare outputs, detect contradictions, and preserve each simulator's model/version/assumption boundary.

Required identifiers:
simulation_id, simulator_id, domain, model_version, source_commit, input_hash, output_hash, timestamp, seed, units, assumptions, evidence_class, licence_state.

## Cross-simulator learning
A result may become learning evidence only after:
1. schema validation;
2. provenance capture;
3. deterministic/reproducible replay where possible;
4. numerical/unit sanity checks;
5. cross-model comparison;
6. explicit classification as observed, computed, simulated, inferred, or unresolved.

## Hard default repository protocol
EVERY SEARCH / FETCH / INGEST / SIMULATION / TEST / FAILURE / UPDATE MUST emit a LearningEvent.
No silent ingestion.
No silent overwrite.
No automatic promotion from discovered to validated.
No private secrets in learning events.

## Blockchain boundary
LearningEvent records remain off-chain by default. A cryptographic digest/manifest may be anchored to a blockchain later. Private datasets, source code and secrets remain off-chain. Blockchain anchoring is a provenance integrity mechanism, not a substitute for scientific validation.


## Gate 36 execution record — 2026-09-22
- Cross-checked the universal required identifier contract against the canonical TypeScript federation boundary.
- Found a contract gap: timestamp and licence state were specified by Gate 36 but absent from FederationObservation; evidence was represented as `evidence` rather than the contract's required `evidenceClass`.
- Corrected `packages/biupiu-rnd-os/src/federation-contracts.ts` with timestamp, evidenceClass and licenceState.
- Added a typed smoke assertion for the new provenance fields in `federation-contracts.test.ts`.
- Local TypeScript compiler check of the corrected contract: **PASS** (TypeScript 5.8.3, strict, ES2022, NodeNext).
- Full package build, fresh CI, simulator-host runtime, Android/UE runtime and cross-simulator execution remain open.

### Status transition
**CONTRACT GAP FOUND → PATCH IMPLEMENTED → STATIC TYPE CHECK PASS → RUNTIME FEDERATION OPEN.**
