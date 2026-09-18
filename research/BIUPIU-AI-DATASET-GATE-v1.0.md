# AI-08 — Experiment Dataset & Time-Series Intelligence

## Objective
Connect physical sensor ingestion to durable experiment datasets and a controlled AI feedback loop.

## Flow
SENSOR READINGS → RAW DATASET → VALIDATION → TIME-SERIES SUMMARY → EXPERIMENT RESULT → EVIDENCE UPDATE → NEXT TEST

## Implemented foundation
- experiment dataset schema
- raw measurement preservation at the dataset-object level
- data validation
- time-series summary statistics
- AI feedback object for next-test review
- automated tests

## Data integrity
Each dataset is linked to an experiment and sensor. Timestamps, units and quality state are retained. Derived summaries do not replace raw measurements.

## AI boundary
The feedback service recommends review/actions; it does not silently modify experimental conclusions or promote measurements to scientific fact.

## Next gate
AI-09: durable experiment storage, dataset versioning and richer statistical analysis.
