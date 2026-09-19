# Biupiu Automated Pareto Frontier & Test-Selection Engine v1.0

Gate: BM-10
Status: EXECUTED / architecture stage

## Purpose
BM-10 converts valid BM-09 multi-physics evaluations into a reproducible multi-objective Pareto set and a traceable physical-test queue.

Pipeline:
BM-09 RESULTS -> QUALITY FILTER -> OBJECTIVE NORMALISATION -> DOMINANCE ANALYSIS -> PARETO SET -> UNCERTAINTY/VALUE-OF-INFORMATION FILTER -> TEST SELECTION -> BM-06 CALIBRATION

## Core rules
- Objective directions are explicit: minimise, maximise, or target-range.
- Conflicting objectives remain visible; no unexplained composite score is used.
- Invalid, blocked or incomplete evaluations are excluded from Pareto extraction and retained with their reason.
- Uncertainty is retained alongside every objective.
- A Pareto candidate is a research candidate, not a certification result.
- Test selection may prioritise information gain and uncertainty reduction without deleting lower-priority candidates.

## Pareto procedure
1. Validate candidate/result provenance.
2. Validate objective completeness and direction.
3. Apply hard engineering/data constraints.
4. Convert objectives to a common comparison representation without changing their physical meaning.
5. Perform non-dominated sorting.
6. Record Pareto-front membership and dominance relationships.
7. Preserve the full objective vector and uncertainty envelope.
8. Route selected candidates to the experiment queue.

## Test-selection logic
Selection inputs:
- Pareto-front relevance
- uncertainty reduction potential
- model sensitivity
- operating-condition relevance
- manufacturing feasibility
- hypothesis discrimination
- expected information gain
- estimated test cost/time

The queue records why each test was selected. Priority is operational queue metadata, not a claim that one material or formulation is universally superior.

## Reproducibility
Every extraction records:
- PARETO_RUN_ID
- source evaluation run IDs
- objective schema/version
- constraint schema/version
- algorithm/version
- tie-handling rule
- missing-data policy
- timestamp

## Integration
BM-10 links:
BM-08 candidate ID -> BM-09 evaluation -> Pareto record -> BM-08 experiment queue -> BM-06 physical test -> calibration -> new Digital Twin version.

## Safety/evidence boundary
This is an R&D decision-support layer. It does not certify a material, blade, rotor, vehicle, vessel or aircraft.

Next: BM-11 — Closed-Loop Digital Twin Calibration & Active Learning.
