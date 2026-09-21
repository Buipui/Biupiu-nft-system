# Biupiu Multi-AI Native Build Framework v1.0

## Purpose
This thread is the **Native Build + Initial Task Framework** for a controlled mini-OS build. It is a parallel experimental build surface and must not silently replace or modify Main OS authority.

## Architecture
`INTAKE -> CLASSIFY -> DECOMPOSE -> TASK GRAPH -> RETRIEVE -> CROSS-LINK -> PROVENANCE -> SPECIALISTS -> SANDBOX -> SIMULATE/EXPERIMENT -> CROSS-CHECK -> TEST -> REVIEW -> INTEGRATE -> REGRESS -> LEARN -> PROMOTE/REJECT -> LOG`

## Multi-AI team
- **ARCHITECT** — decomposes requirements and owns architecture proposals.
- **RESEARCH/HARVEST** — retrieves reusable patterns, dependencies and evidence.
- **CODE** — implements isolated changes.
- **SIMULATION/MATH** — challenges assumptions and produces deterministic checks.
- **SECURITY** — checks trust, permissions, secrets, attack surface and provenance.
- **INTEGRATION** — checks contracts, dependency direction and merge compatibility.
- **VERIFICATION** — runs tests and distinguishes source implementation from runtime evidence.
- **RED-TEAM/FAILURE** — injects contradictions, malformed inputs and failure paths.
- **GOVERNANCE/RELEASE** — records evidence and controls promotion.
- **HUMAN GATE** — required for irreversible or authority-changing promotion.

## Authority
AI agents may propose, retrieve, implement in sandbox scope, test and cross-check. They may not silently promote code into Main OS authority, bypass security, erase rejected evidence, or convert inference/simulation into observed fact.

## Task contract
Every task carries:
`task_id, parent_id, owner_role, scope, inputs, dependencies, expected_output, evidence_required, risk, licence, status, attempts, failure_fingerprint, rollback, promotion_state`.

Allowed status:
`NEW, READY, EXECUTING, BLOCKED, COMPLETE, FAILED, INCOMPLETE, STALE, FLAGGED_HUMAN, PROMOTED, REJECTED`.

## Conflict protocol
1. Detect contradiction.
2. Freeze promotion.
3. Preserve both claims/evidence.
4. Independent specialist review.
5. Reproduce.
6. Prefer deterministic evidence over assertion.
7. Patch only the smallest affected boundary.
8. Re-test.
9. Record the conflict and outcome.

## Harvest protocol
`DISCOVER -> TRANSLATE -> SOURCE/AUTHORITY CHECK -> LICENSE -> EXTRACT PATTERN -> MAP CONTRACT -> IMPLEMENT INDEPENDENTLY -> TEST -> VERIFY`.

Language is a discovery axis, never a trust score. XDA/community material remains discovery/reference; official OEM/AOSP/licensed upstream material outranks it for authoritative contracts.

## Mini-OS boundary
Mini-OS may experiment with:
- native C ABI/HAL
- Rust core services
- C++ scientific/graphics services
- AI federation/orchestration
- deterministic math/verification
- Digital Twin interfaces
- hardware capability contracts
- DMS/event/provenance
- security and recovery

Mini-OS must consume or fork **concepts/contracts**, not silently become a second authority.

## Evolution loop
`OBSERVE -> PROPOSE -> SANDBOX -> INDEPENDENT VERIFY -> VERSION -> REGRESS -> PROMOTE/REJECT -> LEARN`.

## Promotion classes
- **P0 Core:** requires human gate + deterministic tests + security + provenance + regression.
- **P1 Service:** requires contract, tests, provenance and rollback.
- **P2 Experimental:** sandbox only until promoted.
- **REJECTED:** retained as learning evidence; not executable authority.

## Definition of done
A native module is not "done" merely because source exists. It requires:
1. contract defined;
2. implementation present;
3. static/unit test;
4. integration test where applicable;
5. failure path tested;
6. provenance/licence recorded;
7. rollback path recorded;
8. promotion state explicitly logged.

## Main OS separation
Main OS remains authoritative. Mini-OS results become candidates for later comparison/evaluation. No automatic promotion crosses the boundary.
