# Quantum Algorithms × Computational Biology / Geometry Controlled Experiment
Date: 2026-09-23
Status: EXPERIMENT BRANCH — runtime verification pending

## Objective
Create a computational-biology implementation with the same small, deterministic,
typed primitive architecture as the existing computational-geometry module, then
cross-reference quantum-algorithm literature and update the learning taxonomy.
A common optimisation harness is added so geometry and biology can be measured
under identical search budgets.

## Internal baseline
Existing geometry module: codex/geometry/biupiu_geometry.py
Existing geometry tests: codex/geometry/tests/test_biupiu_geometry.py
Existing native AI classification boundary: software/rnd-os-ai/src/biupiu_ai/math_problem_solver.py

The geometry module provides Point2, distance, orientation, collinear, Segment2 and
polygon_area. The biology analogue provides BioPoint, distance, orientation,
collinear, BioSegment, sequence_span plus sequence normalization, Hamming distance,
and GC fraction.

## External quantum harvest
1. Nature npj Genomic Medicine (2025): quantum computing is being investigated for
multi-omics integration, molecular simulation, protein folding, biomarker selection,
gene-network inference and drug discovery; the review also stresses present hardware
and scaling limitations.
2. Nature npj Digital Medicine (2025): a systematic review found no consistent
empirical trend establishing QML superiority for digital-health tasks under realistic
conditions; idealised simulations dominate much of the literature.
3. ACS Journal of Chemical Theory and Computation (2024): hybrid quantum-classical
workflows, including QAOA/VQE-style formulations, have been explored for protein
structure prediction, with a small Zika NS3 helicase loop used as a proof of concept.
4. Scientific Reports (2026): quantum annealing protein-folding studies remain
proof-of-concept and are constrained by embedding and hardware limitations.
5. Nature Reviews Molecular Cell Biology (2026): quantum computing is being explored
alongside single-cell and spatial/multi-omics analysis, with integration of classical
AI and quantum methods identified as an important research direction.

## Learning update
- Add BIOLOGY / GENOMICS / PROTEIN / MOLECULAR / MULTI-OMICS as first-class semantic
  problem domains.
- Keep QUANTUM_ALGORITHM distinct from quantum-inspired classical computation.
- Preserve the evidence boundary: external literature informs candidate algorithms;
  it does not become runtime authority without implementation and verification.
- Optimisation records must include objective, constraints, budget, hardware/runtime,
  baseline comparator, and verification result.
- Do not label a result "quantum advantage" unless an actual quantum execution and
  appropriate classical comparison support that claim.

## Controlled comparison
Pass A: common deterministic optimiser, geometry encoding.
Pass B: same optimiser, biology encoding.
Metrics: evaluations, best objective residual, convergence/verification, runtime when
the host runner is available.
Pass C (future): actual QAOA/VQE/annealing provider, same problem family and budget
normalisation, with noise/error/resource accounting.

## Evidence state
IMPLEMENTED IN EXPERIMENT BRANCH / RUNTIME TEST OPEN
