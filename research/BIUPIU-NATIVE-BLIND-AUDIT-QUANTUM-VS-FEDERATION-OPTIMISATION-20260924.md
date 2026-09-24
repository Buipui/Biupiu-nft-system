# Biupiu Native Blind Audit — Quantum vs Federation + Optimisation Modules — 2026-09-24

**Status:** SOURCE-LEVEL BLIND AUDIT COMPLETED / MATCHED OPTIMISATION EXECUTION OPEN

## Objective
Repeat the native Quantum-vs-Federation blind audit with the repository's existing optimisation modules included as a common controlled layer.

The optimisation layer is **not** treated as a third authority or automatic winner. It is evaluated as a set of candidate transformations that must preserve correctness, provenance, failure behaviour and promotion boundaries.

## Blind design
Architecture identities are hidden during test definition:
- ARM-A = one architecture path
- ARM-B = the other architecture path

Optimisation candidates are also treated as blinded candidate transformations:
- O1 compute scheduling/routing
- O2 SIMD/NEON/accelerator selection
- O3 sparse/geometry optimisation
- O4 numerical/alignment optimisation
- O5 model/hyperparameter optimisation
- O6 representation/resource optimisation

The same optimisation candidate must be applied under the same eligibility conditions to both architecture arms where technically applicable. A candidate that is not applicable is recorded as **NOT_APPLICABLE**, not scored as a failure.

## Native optimisation modules located

### Compute/Federation
- `software/rnd-os-ai/src/biupiu_ai/compute_federation.py`
- Capability-driven CPU/GPU/NPU/vector selection.
- Preferred-class ordering and capacity fallback are already represented.
- Existing scheduler fault correction is retained as prior evidence.

### ML
- `software/rnd-os-ai/src/biupiu_ai/ml/engine.py`
- Includes hyperparameter-optimisation and search capability vocabulary, plus portable inference and federated-learning boundaries.

### Scientific optimisation
- Eigen/GSL federation records identify ARM NEON/SIMD, sparse linear algebra, geometry, alignment, optimised numerical functions, numeric types and thread-safety as candidates.
- These remain provider/reference candidates until their runtime gates pass.

### Domain optimisation
- Smart-farming optimisation protocol uses Observe -> Validate -> Compare -> Recommend -> Human review -> Implement -> Measure -> Learn -> Version.
- Digital-Twin optimisation and computational-geometry optimisation are represented as domain candidates.

## Common blind test matrix

| Test | Requirement | Required evidence |
|---|---|---|
| B1 | Capability equivalence | same target function / missing-function map |
| B2 | Correctness | invariant/output comparison |
| B3 | Optimisation delta | before/after metric under same workload |
| B4 | Overhead | CPU/memory/time/dispatch overhead |
| B5 | Determinism | seed/replay/hash where applicable |
| B6 | Failure injection | matched fault and recovery evidence |
| B7 | Regression | dependent-system delta |
| B8 | Numerical/geometry invariants | area, distance, centroid and domain invariants |
| B9 | Resource scaling | workload-size curve |
| B10 | Provenance | version/commit/licence/evidence class |
| B11 | Promotion safety | OS/DMS/human authority preserved |
| B12 | Optimisation reversibility | rollback/supersession record |

## Control
Baseline A remains unchanged:
- L0: 10,000 iterations
- L1: 5,000
- L2: 3,000
- L3: 2,000
- L4: 1,000
- recorded failures: 0
- geometry checks: polygon-area invariance, pairwise-distance invariance, finite centroid
- quantum policy: SIMULATOR_VALIDATE
- QPU: DISABLED

No optimiser may rewrite the control condition.

## Source-level audit findings

1. **Federation optimisation fit:** The Federation contracts already provide a natural location for capability-aware optimisation because scheduling, provider selection, health, evidence and trace data are explicit.
2. **Quantum optimisation fit:** The Quantum path already exposes candidate selection using classical score, simulator score, uncertainty and resource pressure. This is a routing decision, not a proof of advantage.
3. **Shared optimisation contract:** Both paths can be tested through the same before/after metrics and evidence schema without making either path authoritative.
4. **Existing scheduler learning:** The repository contains a prior scheduler fault where preferred compute classes were treated as unordered. The corrected implementation now preserves declared preference order. This is a useful regression case for O1.
5. **SIMD/NEON:** Capability detection exists at the architecture level, but physical instruction-set performance is not established by source registration.
6. **Sparse/geometry optimisation:** Existing scientific/geometry references provide candidate optimisation surfaces, but numerical runtime correlation remains open.
7. **ML optimisation:** Hyperparameter/search vocabulary exists, but candidate selection does not automatically establish improved generalisation or production performance.
8. **Domain optimisation:** Farming and Digital-Twin optimisation protocols require measurement and human review before implementation, consistent with the native promotion boundary.
9. **No silent substitution:** Optimisation candidates must not replace existing implementations merely because they appear faster or smaller in source inspection.
10. **No optimisation authority leakage:** Quantum, Federation and optimisation modules remain subordinate to OS/DMS validation and human release authority.

## Blind result classification

**ARM-A:** source-compatible / optimisation-compatible candidate / runtime unverified.

**ARM-B:** source-compatible / optimisation-compatible candidate / runtime unverified.

**Optimisation candidates:** REGISTERED / CANDIDATE; no candidate is promoted by this audit.

**Comparative winner:** NOT ASSIGNED.

**Quantum advantage:** NOT CLAIMED.

**Optimisation improvement:** NOT CLAIMED until matched execution evidence exists.

## Required execution sequence

FREEZE INPUT → BLIND ARM EXECUTION → APPLY MATCHED OPTIMISATION → MEASURE → VERIFY CORRECTNESS → INJECT FAULTS → REPLAY → REGRESSION → UNBLIND → FILE RAW EVIDENCE → PROMOTION GATE.

Optimisation may only be retained where the measured improvement is reproducible and does not introduce correctness, security, provenance, compatibility or regression loss.

## Learning disposition

The audit strengthens the repository architecture toward:

**OS/DMS authority**
→ **Federation orchestration/evidence**
→ **domain/provider modules**
→ **Quantum specialised capability**
→ **optimisation candidates**
→ **validated implementation**

This is a governance/data-flow model, not a claim that any layer is computationally superior.

## Verification boundary

- Source audit: **COMPLETE**
- Optimisation candidate inventory: **COMPLETE**
- Blind execution: **OPEN**
- Runtime benchmark: **OPEN**
- Hardware SIMD/GPU/NPU: **OPEN**
- QPU: **DISABLED**
- Android/UE5 runtime: **OPEN**
- Promotion: **NOT PERFORMED**
