# Biupiu Formulation Optimisation Specification v1.0

Gate: BM-07 — Formulation Optimisation
Status: EXECUTED / research-design stage

## 1. Optimisation objective
BM-07 converts calibrated physical-test data and literature-qualified candidates into a constrained candidate-generation loop:

MATERIAL GENOME + RESIN GENOME + TEST DATA + DIGITAL TWIN -> DESIGN SPACE -> CANDIDATES -> SIMULATION -> PARETO SET -> TEST QUEUE -> CALIBRATION

The gate does not declare a universal best formulation. It identifies non-dominated candidates against explicitly recorded objectives and constraints.

## 2. Design variables
- Fibre: hemp, flax, hemp/flax, basalt hybrid; must reference MATERIAL-ID.
- Fibre volume fraction: sourced/measured range; no invented property values.
- Fibre treatment: untreated, alkali, silane, bio-based, physical; process must be recorded.
- Resin family: existing H01-H05, F01, HF01, HFB01 families; reference formulation.
- Bio-content: measured/sourced; unknown remains unknown.
- Hardener/cure: documented formulation and cure profile.
- Architecture: UD, biaxial, hybrid, sandwich; geometry and ply sequence required.
- Basalt fraction, core, manufacturing route and conditioning are explicit variables.

## 3. Objectives
Where evidence exists, the optimiser may minimise/maximise:
- mass
- structural deflection
- peak stress/strain
- fatigue damage indicator
- vibration/modal response
- moisture sensitivity
- thermal sensitivity
- manufacturing complexity
- material/process cost
- embodied-impact indicator

Every quantitative output retains units, source, model version and uncertainty.

## 4. Hard constraints
Candidates are excluded from simulation/test queues when required inputs are absent or an explicitly defined engineering constraint is violated. Controls include load-case compatibility, validated strength/stiffness limits, fatigue requirements where data exist, moisture/thermal envelope, manufacturing feasibility, dynamic-balance constraints and explicit safety factors.

Unknown is not equivalent to pass. Missing data route to data acquisition.

## 5. Candidate-generation strategy
A. Evidence filter: require traceable material/formulation records and manufacturing route.
B. Design of experiments: generate bounded combinations over fibre, treatment, matrix, fraction, architecture and cure/process variables; record generator version and seed.
C. Digital-twin screening: use the existing BM-04 runner with identical geometry, loads and boundary conditions.
D. Uncertainty screening: propagate material, manufacturing and environmental uncertainty.
E. Pareto extraction: retain non-dominated candidates across selected objectives; do not hide trade-offs in an unexplained single score.
F. Experiment queue: prioritise Pareto-relevant, uncertainty-reducing, manufacturable and hypothesis-discriminating candidates.

## 6. Experimental feedback
CANDIDATE-ID -> TEST-ID -> RAW DATA -> QC -> UNCERTAINTY -> MATERIAL/FORMULATION RECORD -> DIGITAL TWIN VERSION

Measured values may replace estimates only when traceable to specimen, batch, method, equipment/calibration and conditioning records. Failed candidates remain in the dataset.

## 7. Candidate status
GENERATED; SIMULATION-READY; SIMULATED; UNCERTAINTY-REVIEW; PARETO-CANDIDATE; TEST-QUEUED; TESTED; CALIBRATED; REPLICATION-REQUIRED; DISQUALIFIED-DATA; DISQUALIFIED-CONSTRAINT.

These are research workflow states, not certification claims.

## 8. Gate exit criteria
- machine-readable design space
- candidate provenance
- explicit objectives and constraints
- unknown values preserved
- simulation-to-candidate traceability
- physical-test-to-calibration traceability
- multi-objective Pareto outputs
- reproducibility metadata

## 9. Next gate
BM-08 — Automated Candidate Runner & Experiment Queue: implement deterministic candidate generation, validation, result ingestion and experiment-priority queue while preserving evidence and uncertainty rules.
