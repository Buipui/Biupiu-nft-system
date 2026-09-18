# Biupiu Automated Candidate Runner & Experiment Queue v1.0

Gate: BM-08
Status: EXECUTED / architecture + validation stage

## Purpose
BM-08 turns the BM-07 design space into a deterministic, provenance-preserving candidate workflow.

Pipeline:
DESIGN SPACE -> VALIDATE -> GENERATE -> DEDUPLICATE -> SIMULATION QUEUE -> RESULT INGESTION -> UNCERTAINTY REVIEW -> PARETO SET -> EXPERIMENT QUEUE -> BM-06 CALIBRATION

## 1. Deterministic generation
Every run records RUN_ID, generator version, generation seed, design-space version, material/resin record versions, geometry/load-case versions, timestamp, candidate count, rejected count and rejection reasons.

The same inputs and seed must reproduce the same candidate set.

## 2. Validation gates
A candidate is SIMULATION-READY only when required references resolve; required variables are populated or explicitly marked unknown; geometry, load cases and boundary conditions are compatible; safety factor is explicitly recorded; manufacturing route is defined; and provenance is complete.

Unknown required engineering data blocks execution rather than becoming a default value.

## 3. Candidate identity
Candidate IDs are immutable. A changed material, resin, geometry, process, model or load case creates a new candidate/version relationship rather than overwriting history.

Duplicate candidates are detected from a canonicalised design signature.

## 4. Queue states
GENERATED -> VALIDATED -> SIMULATION-QUEUED -> SIMULATED -> UNCERTAINTY-REVIEW -> PARETO-CANDIDATE -> TEST-QUEUED -> TESTED -> CALIBRATED

Failure states: REJECTED-DATA, REJECTED-CONSTRAINT, SIMULATION-FAILED, TEST-FAILED.

Failures remain auditable.

## 5. Result ingestion
Results reference the BM-04 result record schema and retain solver/model version, mesh version, boundary conditions, material/formulation versions, outputs, uncertainty and provenance.

No result may be ingested without its candidate ID.

## 6. Pareto extraction
Use explicit objective direction (minimise/maximise) and exclude candidates with invalid or missing required outputs.

Do not convert conflicting objectives into an unexplained single score. Preserve the complete objective vector.

## 7. Experiment prioritisation
Test priority considers Pareto relevance, uncertainty reduction, feasibility/manufacturability, operating-condition relevance, novelty of the tested hypothesis and information gained relative to cost/time.

Priority is a queue-management value, not an engineering certification or universal ranking.

## 8. BM-06 integration
A tested candidate creates TEST_ID links into the physical-test schema. Traceable measured data can update material/resin records and create a new Digital Twin model version. Independent validation remains separate from calibration data.

## 9. Evidence boundary
This runner is an R&D workflow. It does not certify blades, materials, structures or operating safety. Certification/qualification requires applicable standards, qualified testing and independent review.

## 10. Exit criteria
BM-08 is implemented when deterministic generation, validation, candidate identity, queue states, result ingestion, Pareto extraction and experiment prioritisation are machine-readable and provenance-preserving.

Next: BM-09 — Multi-Physics Candidate Evaluation & Uncertainty Engine.
