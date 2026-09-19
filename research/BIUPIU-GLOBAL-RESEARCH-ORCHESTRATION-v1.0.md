# Biupiu Global Research Orchestration Protocol v1.0

**Date:** 19 September 2026  
**Status:** IMPLEMENTED — development orchestration contract

## Purpose
Provide a deterministic orchestration layer for the Biupiu Intelligence Layer using the existing Biupiu search/evidence protocols as its governing basis. The protocol converts a research request into a traceable sequence of discovery, source qualification, cross-checking, evidence classification, cross-disciplinary routing, validation planning and repository registration.

This is an orchestration contract, not a claim that every external search provider or simulator is automatically connected.

## Governing search strategy
1. Primary / archaeological / official source material where applicable.
2. University, museum, government, standards and institutional sources.
3. Peer-reviewed / scholarly discovery layers including JSTOR, AnthroSource, ResearchGate and Emerald Insight where relevant.
4. Patents, prior art and declassified/public technical records.
5. High-quality technical repositories and GitHub for implementation references.
6. Secondary commentary and discovery sources only as contextual leads.
7. Speculative material is retained as hypothesis/inspiration and never promoted to established fact without independent evidence.

## Orchestration pipeline
REQUEST → DECOMPOSE → SOURCE-PLAN → DISCOVER → QUALIFY → CROSS-CHECK → EXTRACT-CLAIMS → CLASSIFY-EVIDENCE → LINK-KNOWLEDGE-GRAPH → CROSS-DISCIPLINE-ROUTE → GAP/CONTRADICTION ANALYSIS → HYPOTHESIS → TEST PLAN → VALIDATE → LEARN → REPOSITORY REGISTER → NEXT ACTION

## Required controls
- Every research object receives a stable identifier.
- Every external source is recorded with provenance and licence/use status where relevant.
- Claims retain source references.
- Conflicting evidence remains visible.
- Search discovery is not equivalent to verification.
- Simulation is not physical validation.
- A repository write is not a successful runtime test.
- Third-party code/assets remain external until licence, security and validation gates pass.
- Human approval is required for durable promotion, deletion, public release, IP transitions and blockchain anchoring.
- Failed, inconclusive and superseded work remains queryable.

## Search expansion rules
For each research question, generate independent search lanes where applicable: official/primary; academic/scholarly; technical implementation; patents/prior art; open-source implementation; historical/archaeological; standards/regulatory; contradictory/falsification; application-domain; cross-disciplinary transfer.

Evidence states: DOCUMENTED, RECONSTRUCTED, EXPERIMENTAL, HYPOTHESIS, SPECULATIVE, CONFLICTED, UNVERIFIED.

## Cross-disciplinary routing
A discovery is routed when its tags, mechanisms, materials, algorithms, controls or measurable variables overlap. Routing creates a candidate link; it does not automatically promote the discovery.

Examples:
- turbine/blade → AERO + MARINE + EVTOL/HELICOPTER + ENERGY + MATERIALS
- AI/algorithm → AI + COMPUTE + ROBOTICS + DIGITAL-TWIN
- materials → MATERIALS + ADV-MFG + AUTOMOTIVE + MARINE + AERO
- regenerative systems → AGRICULTURE + WATER + BIOLOGY + CONSERVATION
- 3D/physics → CG-3D + GEOMETRY + DIGITAL-TWIN + SIMULATION

## Evidence decision
The orchestrator outputs known, unknown, disputed/contradictory, source gaps, candidate hypotheses, candidate experiments/simulations, affected departments, IP/licence review flags, validation requirements and a next-action queue.

## Learning integration
Every material orchestration cycle may emit a learning event describing research input, source set, evidence changes, discovered relationships, failed or inconclusive searches/tests, repository changes, validation state and unresolved risks. Learning preserves old/new lineage and never silently rewrites historical records.

## AI-27 gate
AI-27 requires the orchestration contract, machine-readable schema, deterministic reference implementation, tests for source ranking/evidence classification/routing/fail-closed behaviour, repository registration, and explicit separation between verified connectivity and planned connectivity.

**AI-27 status: IMPLEMENTED — orchestration contract registered. External provider connectivity remains an environment-specific validation gate.**

## Next gate
AI-28: connect the orchestration contract to the live Intelligence Gateway with authenticated retrieval, provenance persistence, result deduplication and end-to-end integration tests.
