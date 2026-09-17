# BIUPIU EXPERIMENTAL CONTROL CENTRE v1.0

**Status:** Active architecture
**Date:** 17 September 2026
**Purpose:** Central orchestration layer for research, hypotheses, simulation, experiments, validation, prototypes, evidence, IP and commercialisation.

## 1. Mission

The Experimental Control Centre converts repository knowledge into controlled, traceable research activity:

`SOURCE → CLAIM → HYPOTHESIS → MODEL → SIMULATION → EXPERIMENT → MEASUREMENT → VALIDATION → REPLICATION → IP/PRODUCT PATH`

It does not treat speculative material as established fact. Every important claim must have an evidence state and, where practical, a falsifiable test path.

## 2. Control Centre modules

- **Research Intake:** capture sources, provenance, licence status and evidence class.
- **Hypothesis Register:** convert claims into explicit, testable propositions.
- **Simulation Lab:** computational models, CAD, CFD/FEA/FEM, multiphysics and parameter sweeps.
- **Experimental Workshop:** physical test plans, controls, equipment, instrumentation and safety gates.
- **Measurement & Data:** raw measurements, uncertainty, calibration and reproducible analysis.
- **Replication Gate:** repeat tests and independent confirmation where practical.
- **Failure Register:** negative results, failed designs, anomalies and lessons learned.
- **Prototype Queue:** prioritised concepts moving toward physical demonstrators.
- **Materials & Instrumentation:** material properties, sensors, controllers and reusable test infrastructure.
- **AI/R&D Analytics:** model assistance, anomaly detection, optimisation and hypothesis generation; AI output remains subject to human verification.
- **IP & Prior Art:** invention records, prior-art searches, FTO considerations and disclosure boundaries.
- **Commercialisation Gate:** engineering maturity, cost, manufacturability, market/application pathway and funding relevance.
- **Repository Sync:** update the master index, experiment records, algorithm registry and related departmental records after execution.

## 3. Evidence states

`ESTABLISHED` — supported by strong, independently accepted evidence.

`SUPPORTED` — evidence currently supports the claim but further validation is useful.

`PRELIMINARY` — limited or early evidence.

`HYPOTHESIS` — testable proposition awaiting validation.

`SPECULATIVE` — idea or claim with insufficient evidence; retained for controlled investigation.

`CONTRADICTED` — available evidence conflicts with the claim.

`INCONCLUSIVE` — test performed but evidence does not resolve the question.

## 4. Experiment record standard

Every formal experiment should record:

- Experiment ID
- Department/stream
- Research source(s)
- Claim and hypothesis
- Prediction
- Independent/dependent variables
- Controls and baseline
- Equipment and calibration status
- Materials
- Method/procedure
- Safety and regulatory gates
- Simulation/model reference
- Raw data location
- Analysis method
- Measurement uncertainty/error sources
- Result
- Evidence state
- Reproducibility/replication status
- Failure modes
- Next action
- Related IP/invention record

## 5. Research maturity ladder

`R0 IDEA`
→ `R1 SOURCE IDENTIFIED`
→ `R2 HYPOTHESIS`
→ `R3 COMPUTATIONAL MODEL`
→ `R4 BENCH EXPERIMENT`
→ `R5 PROTOTYPE`
→ `R6 REPLICATED RESULT`
→ `R7 ENGINEERING DEMONSTRATOR`
→ `R8 COMMERCIAL FEASIBILITY`
→ `R9 PRODUCT/TECHNOLOGY`

A project may move backward when new evidence invalidates an assumption.

## 6. Execution gates

### Gate A — Research integrity
Source, attribution, evidence class and licensing recorded.

### Gate B — Testability
A measurable hypothesis, prediction and control are defined.

### Gate C — Simulation
Where appropriate, computational predictions are produced before physical testing.

### Gate D — Safety
Hazards, operating limits, applicable standards and regulatory constraints reviewed.

### Gate E — Experiment
Measurements collected with calibration and uncertainty recorded.

### Gate F — Validation
Result compared with prediction/control; alternative explanations documented.

### Gate G — Replication
Repeatability assessed before stronger technical claims are made.

### Gate H — Engineering/IP
Prior art, manufacturability, cost and IP position reviewed before commercial claims.

## 7. Cross-department routing

The Control Centre connects:

`BIO ↔ AGRI ↔ HEMP ↔ BIOCARBON ↔ MATERIALS ↔ COMPOSITES ↔ TEXTILES`

`ENERGY ↔ ELECTROMAG ↔ PHOTONICS ↔ FSO-CPT ↔ MM ↔ GEOMETRY ↔ AI`

`COMPUTE ↔ DIGITAL-TWIN ↔ ROBOTICS ↔ ADV-MFG`

`AERO ↔ MARINE ↔ MATERIALS ↔ COMPOSITES ↔ GEOMETRY`

`AAT ↔ GEOARCH ↔ LAND-GIS ↔ SPEC ↔ ENG-VALIDATION`

`RESEARCH ↔ EXPERIMENT ↔ IP ↔ PRODUCT ↔ FUNDING`

## 8. Control Centre dashboard fields

Each active project should expose:

`PROJECT ID | TITLE | DEPARTMENT | OWNER | EVIDENCE STATE | R-MATURITY | CURRENT GATE | NEXT TEST | BLOCKER | DATA LOCATION | IP STATUS | COMMERCIAL PATH | LAST UPDATED`

## 9. Negative-result policy

Failed or inconclusive experiments are retained. They must not be silently deleted or converted into positive findings. Negative results become reusable engineering knowledge and may prevent duplicate work.

## 10. Speculative research policy

Unconventional, historical, video-derived or speculative material may enter the Control Centre as an investigation input. It must be clearly labelled and separated from validated findings. Commercial projections must not depend on unverified performance claims.

## 11. Repository execution rule

When an experiment, simulation or major research task is completed, the result should update the relevant research stream, experiment record, algorithm/version lineage, IP register and/or prototype queue as applicable. The Control Centre remains the orchestration layer rather than replacing departmental records.

## 12. Initial implementation queue

1. Establish master experiment ID convention.
2. Create machine-readable hypothesis/experiment templates.
3. Create failure/negative-results register.
4. Create prototype queue and maturity tracking.
5. Connect CODEX computational tests to experiment records.
6. Connect Cape Town FSO/GIS work to digital-twin and AI routing experiments.
7. Connect metamaterials/structured-light research to controlled simulation tracks.
8. Connect regenerative-agriculture and hemp-material research to physical material-test tracks.
9. Establish repository-wide execution/change log.
10. Add automated consistency checks as the repository tooling matures.

## Status

**Biupiu Experimental Control Centre v1.0 is an active repository architecture.** It is not a claim that all modules or physical laboratory capabilities are already implemented.
