# MATH Problem-Solving & Formal Verification Layer v1.0

**Status:** IMPLEMENTED — architecture and deterministic core registered
**Date:** 19 September 2026

## Purpose
Provide a repository-wide mathematical reasoning boundary for classification, decomposition, symbolic/numerical solving, optimisation, geometry checks, uncertainty handling and proof/verification workflows.

## Pipeline
PROBLEM -> CLASSIFY -> RETRIEVE -> DECOMPOSE -> SOLVE -> VERIFY -> SIMULATE -> SENSITIVITY -> DIGITAL-TWIN -> VALIDATE -> RECORD

## Verification levels
1. FORMAL — proof accepted by an external/formal checker.
2. DETERMINISTIC — reproducible calculation with invariant checks.
3. NUMERICAL — solver result with residual/tolerance checks.
4. SIMULATION — result reproduced under a defined simulation scenario.
5. HEURISTIC — candidate solution requiring stronger validation.

A weaker verification level must never be represented as a formal proof.

## Core interfaces
- Problem classification and domain tags.
- Constraint extraction and invariant registration.
- Candidate solution generation.
- Deterministic verification hooks.
- Formal-proof adapter boundary for Lean/Mathlib and similar systems.
- Simulation hand-off to Digital Twin / physics / robotics engines.
- Provenance and learning-event recording.
- Fail-closed behaviour when verification requirements are not met.

## External research references
- Lean/mathlib provides a mature theorem-proving and mathematical-library foundation.
- Google DeepMind's Formal Conjectures provides formalised mathematical statements and benchmark material for automated theorem proving/formalisation.

Third-party repositories remain references/dependencies until licence, security, compatibility and reproducibility review. No external source code is copied or represented as Biupiu-owned by this integration.

## Safety and architecture boundary
The solver may propose calculations, proofs, algorithms and parameter sets. It does not directly promote a mathematical result into physical deployment. Engineering, robotics, aerospace, biomedical and manufacturing outputs still require their applicable simulation, domain, safety and human-review gates.

## Initial implementation
software/rnd-os-ai/src/biupiu_ai/math_problem_solver.py provides dependency-light deterministic primitives for problem records, constraint/invariant registration, bounded candidate evaluation, residual/tolerance verification, verification-level classification and provenance-ready result records.
software/rnd-os-ai/tests/test_math_problem_solver.py validates the core primitives without requiring an external theorem prover.

## Integration routing
MATH is cross-linked to AI / Biupiu Intelligence, COMPUTE / algorithms, GEOMETRY / computational geometry, ROBOTICS / PHYS-SYS, DIGITAL-TWIN, AERO / MARINE, ENERGY / MATERIALS / ADV-MFG, PHOTONICS / ELECTROMAG, AGRI / WATER, BIOMED and NFT-ART / NFT-PROV where mathematical provenance is relevant.

## Acceptance rule
No automatic physical deployment, repository self-modification or irreversible blockchain action is authorized solely by a solver result. Results must pass the relevant downstream gates.

## MATH-02 — Verification Harness / Formal-Prover Adapter Gate

**Status:** REGISTERED — implementation validation pending CI execution
**Date:** 19 September 2026

### Gate objective
Turn MATH-01 from a deterministic verification layer into a controlled multi-backend verification pipeline without allowing unverified solver output to become authoritative.

### Required sequence
1. Normalize problem statement and constraints.
2. Generate candidate solution(s).
3. Run deterministic invariant/residual checks.
4. Route theorem-shaped claims to a formal-prover adapter.
5. Route numerical/engineering claims to simulation or domain solvers.
6. Compare evidence and detect contradictions.
7. Record verification level, provenance and failure reason.
8. Fail closed when required evidence is missing.

### Acceptance criteria
- CI test run observed and passing.
- Formal-prover adapter remains optional until its toolchain is actually available.
- Numerical verification never masquerades as formal proof.
- Solver output cannot directly modify authoritative OS state.
- Every accepted result has reproducible evidence metadata.

### Current gate result
The repository contains the MATH-01 implementation and validation workflow. This connector session can verify file presence, but no GitHub Actions run is currently reported for the latest MATH commits. Therefore MATH-02 is **REGISTERED / WAITING FOR CI EXECUTION**, not falsely marked passed.

### Next action
Trigger or observe the GitHub Actions validation run, inspect its job logs, then promote MATH-02 only if the tests pass. After that, integrate a real formal-prover backend under the adapter boundary and add domain-specific solver contracts.
