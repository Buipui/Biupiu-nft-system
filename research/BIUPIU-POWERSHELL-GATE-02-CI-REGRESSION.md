# Biupiu PowerShell Gateway Gate 02 — CI Regression and Digital Twin Validation

Date: 20 September 2026
Status: IMPLEMENTED / CI EXECUTION PENDING

## Executed
- Added Windows GitHub Actions regression workflow.
- Runs the deterministic gateway policy test under PowerShell.
- Exercises the gateway in dry-run mode.
- Checks for forbidden Invoke-Expression/iex primitives.
- Parses and validates the Digital Twin gateway schema.
- Preserves the rule that unverified host state remains unverified in CI.

## Separation of evidence
- Repository source validation: IMPLEMENTED.
- CI workflow definition: COMMITTED.
- Actual workflow execution result: PENDING until GitHub Actions produces a run.
- Physical Windows development-host verification: PENDING.
- GPU/driver/Unity/UE5/Visual Studio/VS Code discovery: PENDING.
- Android remote-control bridge: NOT IMPLEMENTED.

## Promotion rule
Passing repository/CI tests does not promote host-dependent capabilities to VERIFIED. Host evidence must still come from the actual Windows development machine.