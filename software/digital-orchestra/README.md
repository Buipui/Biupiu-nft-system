# Biupiu Digital Orchestra v1.0

Status: IMPLEMENTED — native source seed; runtime verification pending.

Digital Orchestra is a separate but interlinked orchestration layer for Biupiu. It coordinates work, evidence, repositories, modules, validation gates and cross-system events without becoming an authority bypass.

## Design
- Native, dependency-light core.
- Declarative workflow definitions.
- Explicit state transitions.
- Event journal with correlation IDs.
- Evidence/provenance attached to every work item.
- Fail-closed authority boundaries.
- Reversible execution and resumable handoffs.
- Pluggable adapters for GitHub, files, CI, simulators, DMS, Digital Twin and future OS services.
- Filing is metadata-first: source, language, licence, provenance, evidence state, module role and integration status are retained.

## Execution chain
DISCOVER -> CLASSIFY -> PLAN -> ROUTE -> EXECUTE -> OBSERVE -> VERIFY -> DIGEST -> FILE -> LEARN -> PROMOTE

## Authority
The Orchestra may route and coordinate. It may not promote unverified external code, overwrite authoritative state, or convert research/hypotheses into facts.

## Initial modules
- conductor: workflow routing
- registry: module/source/capability registry
- filing: canonical digital filing metadata
- journal: append-only event records
- gates: verification-state transitions
- harvest: external-source intake and provenance classification
- adapters: replaceable integration boundaries

## Verification boundary
SOURCE_IMPLEMENTED / BUILD_PENDING / RUNTIME_PENDING until executed in the target host environment.
