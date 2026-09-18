# PROP-15 — Test Dataset & Digital-Twin Ingestion v1.0

## Executed
Added:
- `digital-twin/datasets/prop15_test_points_v1.json`
- `digital-twin/schemas/microturbine_test_data_v1.json`
- `simulators/biupiu_test_dataset_builder_v0_1.py`

The builder creates application-linked records for AUTO, MARINE, EVTOL, HELI and UAV across BT-70/140/200/300.

## Data integrity
Every record includes:
- unique test ID
- module
- application
- altitude
- pressure ratio
- recuperator effectiveness
- target electrical power
- uncertainty fraction
- validation status

The dataset is deliberately created with `planned` status. No generated value is represented as measured or validated hardware performance.

## PROP-16
Next gate should add:
1. uncertainty propagation from component maps to mission outputs;
2. mission-linked test prioritisation;
3. automated comparison of planned vs measured data;
4. digital-twin state update rules;
5. anomaly/out-of-envelope flags;
6. exportable experiment report structure.

Status: research/test-data infrastructure only.
