# Biupiu Closed-Loop Digital Twin Calibration & Active Learning v1.0

Gate: BM-11
Status: EXECUTED / architecture stage

## Purpose
BM-11 closes the loop between simulation, physical evidence and candidate generation.

Pipeline:
SIMULATION -> PREDICTION -> PHYSICAL TEST -> QC -> CALIBRATION -> ERROR/UNCERTAINTY UPDATE -> DIGITAL TWIN VERSION -> ACTIVE LEARNING -> NEXT CANDIDATES

## Calibration rules
- Raw experimental data remain immutable references.
- Calibration uses traceable measured data only.
- Calibration datasets and independent validation datasets remain separate.
- Each calibration creates a new model version; previous versions remain reproducible.
- Parameter updates record prior value, posterior/update value, method and uncertainty.
- Failed tests are retained and classified.
- Literature data can inform priors/candidate ranges but cannot silently overwrite measured data.

## Active-learning loop
The engine identifies the next experiment or simulation based on:
- predictive uncertainty;
- model sensitivity;
- expected information gain;
- disagreement between competing model assumptions;
- Pareto relevance;
- manufacturability and test feasibility.

The objective is to reduce uncertainty and improve model fidelity, not to force a predetermined material choice.

## Validation split
Required dataset roles:
- calibration/training;
- independent validation;
- optional hold-out/replication.

No validation sample may be used for calibration without creating a new documented model version.

## Model-drift controls
Trigger review when:
- prediction error exceeds a documented threshold;
- new material batch differs materially from calibration population;
- manufacturing route changes;
- environmental range expands;
- new physical mechanism is introduced;
- sensor/test method changes.

## Outputs
Each loop records:
LOOP_ID, candidate/test references, prior model version, calibrated model version, data references, error metrics, uncertainty update, active-learning rationale, validation status and next-action queue.

## Evidence boundary
BM-11 improves research-model fidelity. It does not constitute certification, qualification or a safety case.

Next: BM-12 — Reproducible Simulation/Experiment Orchestrator & Research Data Lake.
