# AI-03 — Automated Experiment Generation Gate

## Objective
Connect the AI layer to the Experimental Control Centre by producing structured, falsifiable experiment plans.

## Pipeline
CLAIM → HYPOTHESIS → VARIABLES → CONTROLS → PROCEDURE → EXPECTED OBSERVATIONS → FALSIFICATION CRITERIA → EXECUTION → RAW DATA → RESULT → NEXT TEST

## Required properties
Every generated plan must identify the hypothesis, variables, controls, procedure, expected observations and falsification criteria. Safety review is required by default.

## Result states
- supported: observed effect is directionally consistent with the predefined prediction, subject to uncertainty and replication.
- unsupported: observed effect does not match the prediction.
- inconclusive: available measurements do not distinguish the prediction from uncertainty.

These states are experimental classifications, not claims of universal truth.

## Boundary
AI-03 creates experiment plans and result classifications. It does not autonomously operate physical equipment, certify scientific claims or bypass human safety review.

## Next gate
AI-04: evidence-aware result analysis, provenance and contradiction handling.
