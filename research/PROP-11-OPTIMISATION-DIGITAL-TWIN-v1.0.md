# PROP-11 — Optimisation & Digital-Twin Gate v1.0

## Executed
Added a parameter-sweep scaffold and the first microturbine digital-twin schema.

### Optimisation dimensions
- BT-70 / BT-140 / BT-200 / BT-300
- battery energy capacity
- compressor pressure ratio
- turbine inlet temperature
- recuperator effectiveness
- altitude

### Feasibility flags
Each point is marked for:
- screened power retention
- minimum battery capacity
- thermal parameter bounds
- overall screened feasibility

### Digital twin
Added:
`digital-twin/schemas/microturbine_system_v0_1.json`

The schema distinguishes:
concept → screened → bench_tested → validated → certified.

This prevents simulation outputs from being represented as experimentally validated hardware.

## Important model status
The optimiser currently uses deliberately simple screening factors. These are not compressor/turbine maps and must not be interpreted as measured performance. The next engineering upgrade should replace the screening factors with component maps and measured test data.

## PROP-12
Next gate:
- replace heuristic factors with cycle-map interfaces;
- connect real mission profiles;
- add thermal-rejection limits;
- add component-level mass models;
- produce Pareto-style candidate sets without ranking them as a universal winner;
- generate machine-readable results for the Biupiu digital twin.
