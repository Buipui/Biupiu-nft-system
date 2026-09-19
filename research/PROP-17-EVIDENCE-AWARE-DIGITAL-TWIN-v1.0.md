# PROP-17 — Evidence-Aware Digital-Twin State Engine v1.0

## Executed
Added `simulators/biupiu_evidence_state_engine_v0_1.py`.

### Functions
- planned-versus-measured comparison
- missing-data detection
- anomaly screening
- evidence-aware validation state transitions

### State discipline
The engine preserves the distinction between:
`planned` → `bench_tested` → `validated` → `certified`.

It does not automatically promote a concept because a simulation matches a target. Validation requires evidence completeness and review.

### Cross-discipline use
The same data-governance layer can be attached to:
AUTO / MARINE / EVTOL / HELI / UAV.

### PROP-18
Next gate should connect this engine to the PROP-15 dataset and digital-twin schema, generate structured anomaly/evidence records, and add automated regression checks so repository changes cannot silently turn planned or simulated values into validated claims.

Status: research/data-governance infrastructure only.
