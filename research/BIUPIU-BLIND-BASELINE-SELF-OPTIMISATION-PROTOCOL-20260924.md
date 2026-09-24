# Biupiu Blind-Baseline Self-Optimisation Protocol — 2026-09-24

**Status:** IMPLEMENTED AS GOVERNED PROTOCOL / EXECUTION VERIFICATION OPEN

## Purpose
Use the verified native-only Baseline A as the control condition for assisted AI/ML optimisation. The optimiser may propose routing, scheduling, module selection, dependency reductions, representation changes or test improvements, but it cannot redefine the baseline or promote its own proposal.

## Blind-test rule
- Baseline A remains unchanged.
- Assisted analysis is enabled only in the candidate arm.
- Candidate arm receives no access to the expected outcome beyond the same declared inputs and baseline contract.
- Compare identical workloads, iteration counts, checks and thresholds.
- Record overhead, output deltas, failures, regressions and evidence.
- An optimisation is retained only when independently reproducible and regression-safe.

## Baseline A
L0 10,000 iterations; L1 5,000; L2 3,000; L3 2,000; L4 1,000.
Current recorded failures: 0.
Geometry checks: polygon-area invariance, pairwise-distance invariance and finite-centroid.
Quantum policy: SIMULATOR_VALIDATE; QPU disabled.
This baseline is a deterministic software-model harness, not physical hardware evidence.

## Self-optimisation loop
DISCOVER → CANDIDATE → BLIND EXECUTE → MEASURE → COMPARE → FAULT/DELTA CLASSIFY → REPRODUCE → REGRESSION → PROVENANCE → PROMOTE/RETAIN/QUARANTINE.

## Promotion boundary
No AI/ML system may self-authorise executable promotion. OS/DMS validation, provenance/licence/security/compatibility gates, regression evidence and human release authority remain required.

## Learning value
The baseline is a control, not a target to be gamed. Improvement claims must identify the measured metric and preserve the unchanged control result.
