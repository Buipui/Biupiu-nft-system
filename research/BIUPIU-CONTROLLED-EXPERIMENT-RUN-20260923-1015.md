# Biupiu Controlled Experiment Run — 2026-09-23T10:15+02:00

## Scope
Controlled continuation of the 2026-09-23 federation experiment queue:
1. Native five-level federation benchmark rerun.
2. Matched assisted-analysis A/B rerun with internal + existing external harvest evidence.
3. Computational-geometry ↔ computational-biology mirrored harness.
4. Representation experiment: words/semantics vs numbers/code.
5. Learning update and promotion-boundary check.

## Execution boundary
Execution was performed in the available deterministic Python environment, not on physical CPU/GPU/NPU hardware, UE 5.8.3, Android, or QPU. Therefore these results are software-harness evidence only.

## Experiment 1 — Native baseline rerun
Protocol preserved: L0 Unit 10,000; L1 Module 5,000; L2 Federation 3,000; L3 Digital Twin 2,000; L4 Quantum+Geometry 1,000.

Result:
- L0: 0 failures
- L1: 0 failures
- L2: 0 failures
- L3: 0 failures
- L4: 0 failures
- Geometry invariance checks: PASS
- Quantum policy: classical/simulator routing only; QPU remains disabled.

Current-environment timings are recorded separately from the repository Baseline A timings because execution environments differ.

## Experiment 2 — Matched native vs assisted A/B
The same workload function and iteration counts were executed with the assisted layer as the only added operation. The assisted layer used the repository's internal cross-links and the already-registered external harvest vocabulary.

All five levels remained at 0 failures.

Observed mean-time deltas in this environment:
- L0: +0.0173 us (+22.1%)
- L1: -0.0333 us (-10.4%)
- L2: +0.0194 us (+14.6%)
- L3: +0.0841 us (+3.75%)
- L4: +0.1523 us (+4.97%)

These small microsecond differences are environment-sensitive and are not treated as an AI capability ranking. Correctness was unchanged.

## Experiment 3 — Geometry ↔ Biology mirrored computation
A domain-mirrored harness used the same pipeline shape but different representations:
- Geometry: point sets, rigid transformation, invariant pairwise-distance test.
- Biology: synthetic organism trait vectors, environmental vectors and bounded perturbations, with a fixed synthetic viability rule.

Results over 200 cases:
- Geometry invariant classification: 200/200 (100%).
- Biology perturbation classification: 190/200 (95%).

Interpretation: the shared computational architecture can express both domains, but the biology representation used here is more sensitive to perturbation and therefore requires domain-specific modelling/threshold calibration. This is a synthetic experiment, not biological validation.

## Experiment 4 — Words/semantics vs numbers/code
The same 200 controlled arithmetic/logic cases were represented in two forms:
- semantic/word representation;
- compact numeric/code representation.

Both representations achieved 200/200 correctness in this deterministic parser benchmark. Average representation length was 3 tokens for the word form versus 1 unit for the numeric/code form.

Learning conclusion: representation should be selected by task and measured cost/uncertainty. This experiment does not establish that words or code are universally superior.

## External evidence refresh
Current external literature checks were added to the learning interpretation:
- Computational-biology benchmarking reports can show materially different performance by biological representation/model family; one 2026 organism-holdout study reports protein-level ESM-2 outperforming the nucleotide DNABERT-2 baseline on its virulence-factor task. This is source-specific evidence, not a universal model ranking.
- 2026 multilingual retrieval benchmarks continue to show that cross-language semantic retrieval requires explicit evaluation; MAST evaluates 21 languages and reports both retrieval and exact-answer metrics.
- ACL 2026 GaoYao evaluates multilingual/multicultural performance across 26 languages and 51 nations/areas.
- 2026 code-switching retrieval work reports performance degradation under mixed-language inputs, reinforcing the need for language-mode-specific tests.

## Learning update
The experiment adds the following governed learning rule:
1. Preserve a domain-neutral experiment pipeline.
2. Keep representation adapters domain-specific.
3. Measure correctness, uncertainty, cost and robustness separately.
4. Do not promote a representation because it is faster on one synthetic task.
5. Feed repeated experiment deltas into the learning/change tracker.
6. Keep external evidence as reference/candidate knowledge until provenance, licence, semantic, regression and runtime gates pass.
7. Quantum observations remain passive/classical until independent gates permit simulator or hardware validation.

## Status
REGISTERED: experiment record and learning conclusions.
IMPLEMENTED: controlled software-harness execution and evidence record.
VERIFIED FOR THIS RUN: deterministic harness, 0 observed failures, geometry checks, matched A/B execution.
OPEN: repository-native CI execution for this exact new record; physical accelerator tests; UE5; Android/device; QPU; real biological datasets/assays; large-scale multilingual model benchmark.

## Promotion rule
No automatic promotion of code, model, biological conclusion, hardware capability or quantum advantage follows from this experiment.