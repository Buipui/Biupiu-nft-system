# AI-04 — Evidence-Aware Results Gate

## Objective
Add provenance, contradictory-evidence handling and replication tracking to the AI layer.

## Evidence states
- insufficient-evidence
- supported-by-current-evidence
- replicated-support
- conflicted

These are repository evidence states, not universal truth labels.

## Provenance
Important transitions should record object ID, event type, actor, timestamp, source and note.

## Replication
Replication records preserve environment, outcome, dataset and deviations. The system reports replication counts and independent environments.

## Contradiction rule
Supporting and contradicting evidence must remain visible. The engine must not silently collapse disagreement into a single conclusion.

## Boundary
AI-04 remains read/analysis oriented. It does not independently certify scientific validity.
