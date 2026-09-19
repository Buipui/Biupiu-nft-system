# PROP-18 — Evidence Dataset Integration & Regression Guards v1.0

## Executed
Integrated the PROP-17 evidence-state rules into a repository-level validation layer.

### Added
- `simulators/biupiu_evidence_state_engine_v0_1.py` — canonical evidence/state rules.
- `simulators/biupiu_prop18_dataset_validator_v0_1.py` — dataset validator.
- `digital-twin/datasets/prop18_validation_records_v1.json` — structured evidence/anomaly records.
- `tests/test_validation_state_guards.py` — regression tests.

### State protection
A record may remain **planned** until measured evidence exists. A record cannot enter **validated** or **certified** solely because a simulation reaches a target. Those states require explicit measured-evidence completeness and review.

### Current PROP-15 status
The repository's PROP-15 dataset is currently an empty measurement container. Therefore PROP-18 records remain `planned` / `NO_MEASURED_DATA` and do not claim physical validation.

### Scope
This gate is data-governance and computational infrastructure only. It does not constitute hardware testing, certification, flight approval, marine classification, road approval, or production validation.

### Next gate
PROP-19 can add CI execution, schema cross-validation and signed evidence/provenance records once the repository's measured-data ingestion path is established.
