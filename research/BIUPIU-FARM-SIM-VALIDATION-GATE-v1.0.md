# FARM-SIM Validation Gate v1.0

## Gate objective
Validate the Farming Simulator resource integration without falsely claiming live simulator execution.

### G1 — Resource identity
Source repository, project/version and commit/tag recorded.

### G2 — Licence
Licence identified and compatible with intended use. Unclear/restricted resources remain reference-only.

### G3 — Schema mapping
External telemetry/actions map to canonical Biupiu farm-state fields.

### G4 — Unit/range validation
Mass, distance, area, volume, speed, energy, time and agricultural units are normalised.

### G5 — Simulation replay
A recorded scenario can be replayed deterministically through the adapter.

### G6 — Digital Twin
Validated state enters the Digital Twin with provenance and transformation version.

### G7 — World promotion
Only validated scenario outputs become World missions/assets.

## Current state
G1–G3: architecture/resource mapping registered.
G4–G7: pending connected-host execution and measured validation.

**Gate state: OPEN — implementation architecture complete; runtime validation required.**
