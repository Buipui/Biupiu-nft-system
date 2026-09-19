# Biupiu Reproducible Simulation/Experiment Orchestrator & Research Data Lake v1.0

Gate: BM-12
Status: EXECUTED / architecture stage

## Purpose
BM-12 provides the provenance and orchestration layer connecting candidate generation, simulation, experiments, calibration and Digital Twin releases.

Pipeline:
SOURCE -> DATASET -> CANDIDATE -> RUN -> RESULT -> TEST -> CALIBRATION -> MODEL VERSION -> RELEASE

## Orchestrator responsibilities
- resolve versioned inputs;
- validate dependencies before execution;
- create immutable run manifests;
- route simulation and experiment jobs;
- capture stdout/log/error references;
- ingest result records;
- preserve failed runs;
- trigger downstream calibration/active-learning events;
- prevent execution when required provenance is missing.

## Research Data Lake logical zones
1. RAW: immutable source data, sensor files, original test files.
2. PROCESSED: reproducible transformations with code/version references.
3. MODELS: material, resin, geometry, simulation and Digital Twin records.
4. RESULTS: simulation and experimental result records.
5. CALIBRATION: calibration datasets, parameter updates and model versions.
6. RELEASES: frozen reproducible research snapshots.

Raw data are never overwritten by processed data.

## Run manifest
Every run records:
RUN_ID, parent_run_id, workflow_version, code/version references, input dataset IDs, material/resin/geometry/model versions, environment, parameters, seed, execution status, output references, logs, error references, timestamp and operator/process identity.

## Dependency controls
A downstream step may execute only when required upstream records are complete and provenance-resolved.

Blocked states are explicit:
WAITING-INPUT, BLOCKED-PROVENANCE, BLOCKED-DATA, READY, RUNNING, COMPLETE, FAILED, CANCELLED.

## Reproducibility
A released run must be reconstructable from its frozen input references, code/model versions, configuration, seed and environment metadata.

## Release rule
Research releases are immutable snapshots. Corrections create a new release/version rather than rewriting history.

## Security/data integrity
Access control belongs to the surrounding repository/system layer. This research schema records ownership and provenance metadata but does not itself implement authentication or authorization.

## Exit criteria
Machine-readable run manifest, workflow schema, data-lake catalog and release manifest are defined.

Next: BM-13 — Automated Research Release, Regression Testing & Evidence Ledger.
