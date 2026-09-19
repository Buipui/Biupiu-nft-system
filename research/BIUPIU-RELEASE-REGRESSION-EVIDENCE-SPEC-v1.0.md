# Biupiu Automated Research Release, Regression Testing & Evidence Ledger v1.0

Gate: BM-13
Status: EXECUTED / architecture stage

## Purpose
BM-13 prevents repository releases from silently changing research behaviour or evidence status. It creates a reproducible validation gate between completed workflows and frozen releases.

Pipeline:
RUNS -> REGRESSION TESTS -> EVIDENCE LEDGER -> RELEASE VALIDATION -> FROZEN RELEASE

## Regression layers
1. Schema regression: validate JSON structures and required fields.
2. Reference regression: resolve referenced material, resin, geometry, dataset, run and model IDs.
3. Determinism regression: repeat deterministic workflows with the same frozen inputs/seed and compare outputs within documented tolerance.
4. Numerical regression: compare approved baseline outputs using explicit tolerances.
5. Data-integrity regression: verify hashes/references and detect unexpected mutation.
6. Evidence regression: ensure evidence states and source provenance have not been silently upgraded.
7. Calibration regression: verify independent validation remains separate from calibration.
8. Pipeline regression: verify required dependency order and blocked-state behaviour.

## Evidence ledger
Every material claim or quantitative result should be traceable through:
CLAIM_ID -> SOURCE_ID -> DATASET_ID -> RUN_ID -> RESULT_ID -> TEST_ID -> MODEL_VERSION -> RELEASE_ID

Evidence states remain explicit. A new source can strengthen or contradict a claim; the ledger records both rather than silently replacing history.

## Release gate
A release may become FROZEN only when:
- required regression tests pass;
- failed tests have documented dispositions;
- provenance is complete;
- evidence status is internally consistent;
- release manifest is complete;
- independent validation records remain separated;
- content hashes/reference integrity are valid.

## Failure policy
Regression failures block release unless a documented waiver/exception record exists. Failed tests are retained and visible.

## Auditability
Each regression run records code/schema versions, baseline reference, current reference, tolerance, observed result, pass/fail state and timestamp.

## Safety/evidence boundary
BM-13 is a research reproducibility and evidence-control mechanism. Passing regression tests does not establish engineering certification or operational safety.

Next: BM-14 — Cross-Department Research Graph & Knowledge Routing Layer.
