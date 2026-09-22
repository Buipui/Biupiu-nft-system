# Biupiu Adapter Gate State Ledger v1.1

Status: UPDATED — validator root-path bug corrected; CI evidence capture strengthened.

## Extermination record
- Removed incorrect repository-root calculation from validator.
- Added explicit Python and runner evidence capture to CI.
- Preserved separation between repository validation and third-party runtime execution.

## Smoke-test contract
The validator must be invoked from the repository root by CI.
Expected result: exit code 0 when manifests and fixtures satisfy the deterministic checks.

## Verification boundary
A GitHub workflow definition is not execution evidence. CI remains PENDING until an actual run is observed.
