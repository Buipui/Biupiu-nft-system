# Biupiu Gate-Learning Architecture v1.0

**Date:** 19 September 2026
**Status:** IMPLEMENTED architecture update

## Purpose
Convert repeated execute → diagnose → fix → retest cycles into structured learning evidence. A gate is not counted as learning merely because it passes; the system records what changed, what failed, why, what fixed it, what regressions were checked, and which dependent systems were affected.

## Canonical loop
RESEARCH → PLAN → EXECUTE → OBSERVE → DIAGNOSE → CONFLICT CLASSIFY → PATCH → UNIT/CONTRACT TEST → CROSS-SYSTEM REGRESSION → PROVENANCE RECORD → LEARNING CHECKPOINT → INDEX → NEXT GATE

## Learning event contract
Each gate should capture:
- gate_id and parent_gate_id
- subsystem and affected departments
- input/state signature
- intended change
- expected outcome
- observed outcome
- conflict/error class
- root-cause hypothesis and evidence
- patch/version/commit
- tests executed
- regression scope and results
- dependencies impacted
- resource/licence provenance
- confidence/status
- unresolved follow-up gates

## Anti-loop rule
A repeated gate must change state or produce new evidence. If the same failure repeats without new evidence, mark it as a stalled loop rather than treating repetition as learning.

## Promotion rule
A fix becomes reusable architecture only after:
1. local test,
2. cross-system regression,
3. provenance record,
4. compatibility/licence review where external resources are involved,
5. explicit promotion into the relevant architecture/index.

## Failure memory
Failures are retained as first-class records. A successful fix must not erase the failure because the failure pattern is future diagnostic knowledge.

## Cross-system propagation
Dependency closure is used to identify affected departments. Typical routing includes AI, OS, COMPUTE, MATH, GEOMETRY, ROBOTICS, PHYS-SYS, DIGITAL-TWIN, CG-3D, AERO, MARINE, ADV-MFG, MATERIALS, BLOCKCHAIN, NFT/IP and domain systems where applicable.

## Safety and authority
AI may propose fixes and tests. Authoritative state, release, spending, deployment, publication and physical-world actions remain gated. Third-party code remains reference-only until licence, security and compatibility review.

## Learning maturity
L0 = event logged
L1 = failure classified
L2 = fix verified
L3 = regression coverage added
L4 = reusable pattern promoted
L5 = pattern generates preventative tests

L5 is an architectural goal, not a claim that every current subsystem has reached it.


## External Harvest Learning Extension — 22 September 2026

External-resource learning is now explicitly a comparison-first process rather than an import-first process.

### Harvest learning loop
`EXTERNAL DISCOVERY -> INTERNAL MATCH -> VERSION/COMMIT CAPTURE -> LICENCE/IP -> DEPENDENCY -> STATIC -> UNIT -> INTEGRATION -> REGRESSION -> RUNTIME -> COMPARE -> PROMOTE/RETAIN/QUARANTINE -> INDEX -> CHECKPOINT -> OPTIONAL BLOCKCHAIN ANCHOR`

### Comparison evidence
Each candidate must preserve:
- internal module tested or considered;
- external exact version/commit;
- contract/API equivalence or mismatch;
- measured performance/behaviour where relevant;
- failure signature and compatibility impact;
- licence/security/dependency state;
- promotion or rejection reason;
- rollback/supersession lineage.

### Preventative-learning rule
A promoted fix or adapter should generate a regression fixture or preventative test where practical. Repeated failures without new evidence remain a stalled loop.

### Blockchain checkpoint
Approved checkpoint hashes may be anchored through the existing registry boundary. Blockchain anchoring records integrity commitments only; it does not convert a candidate into verified code or scientific truth.

New checkpoint: `FED-HARVEST-20260922-01`.



## 2026-09-24 — Cross-Federation Optimisation / Hardware / Learning Allocation
The learning gate now consumes module-allocation evidence from Native Intelligence, including legacy optimisers, OEM/hardware adapters, Android platform candidates and foreign-language evidence. A learning record may recommend a candidate, but execution remains with the owning subsystem and promotion remains OS/DMS/human controlled.

External Android 17 findings added to the candidate graph: NPU scheduling, Motion Context, Secure Execution Environment, wrapfd protected-memory boundary, Berberis heavy/lite translation optimisation and AutoFDO profile-guided optimisation. All remain reference/candidate until local evidence gates close.

Repeated harvests must retain source identity, language, version/tag, licence state and evidence class; translation cannot collapse into authority.
