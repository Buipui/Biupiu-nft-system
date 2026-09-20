# BIUPIU AI-31 — MULTI-AI COLLABORATIVE EXECUTION HARNESS

Status: IMPLEMENTED AS REPOSITORY-LEVEL ORCHESTRATION CONTRACT
Date: 20 September 2026

## Execution pipeline
TASK -> TASK PACKET -> EVIDENCE SET -> PARALLEL SPECIALISTS -> CHALLENGE/REVIEW -> CONTRADICTION RESOLUTION -> MATH/PHYSICS VALIDATION -> SIMULATION/DIGITAL-TWIN CHECK -> SECURITY/LICENCE -> REGRESSION -> PROMOTION RECORD

## Task packet schema
- task_id
- parent_task_id
- objective
- scope
- constraints
- evidence_set_id
- required_capabilities
- assigned_teams
- provider_candidates
- acceptance_tests
- risk_class
- reversible_or_irreversible
- status
- provenance

## Shared state
Every team result must carry:
- task_id
- evidence_set_id
- provider/model/version
- source references
- assumptions
- result
- uncertainty
- conflicts
- test evidence
- licence state

## Challenge protocol
At least one independent specialist challenge is required for high-risk engineering tasks. A challenge may:
1. reproduce calculations;
2. vary assumptions;
3. inspect code;
4. attempt a counterexample;
5. compare alternative models;
6. identify missing evidence.

A disagreement is retained, not averaged away.

## Resolver
CONFLICT -> classify (data/model/code/assumption/licence) -> request targeted evidence -> re-test -> resolve or preserve as OPEN.

## Promotion states
DISCOVERED -> ASSIGNED -> EXECUTING -> CHALLENGED -> VALIDATED -> REGRESSION-PASS -> PROMOTION-READY -> PROMOTED.

## Hard boundaries
- No automatic import of proprietary/private code.
- No automatic secrets/API-key acquisition.
- No unrestricted shell execution.
- No autonomous production deployment.
- No physical actuation without explicit host-level gate.
- External models remain replaceable provider adapters.

## Failure learning
Failures are recorded with:
task_id, failed_gate, cause_class, evidence, remediation, regression_test, affected_modules.

A failure can only be marked learned after the regression test reproduces the original failure and passes after remediation.

## Initial team routing
- Orchestrator: all tasks
- Math/Physics: quantitative tasks
- Code/Systems: software architecture
- Research/Evidence: external knowledge
- Simulation/Digital Twin: model coupling
- Security/Exterminate: dependencies and attack surface
- Blockchain/Provenance: lineage and integrity
- Multimodal/Configuration: HMI/configuration/rendering

## Acceptance
AI-31 is considered implemented when the schema, routing rules, conflict protocol, promotion states and failure-learning contract are versioned in the repository. Runtime execution remains a separate host/provider verification gate.
