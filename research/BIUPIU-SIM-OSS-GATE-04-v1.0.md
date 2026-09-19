# Biupiu SIM-OSS Gate 04 — CI Regression and Smoke Boundary v1.0

## Objective
Make SIM-OSS validation reproducible in CI while preserving the no-auto-execution boundary.

## Implemented
- Added a GitHub Actions regression workflow for the simulator adapter and validation harness.
- The workflow runs the adapter contract tests and deterministic local validation probe.
- No third-party simulator is installed or launched by this workflow.

## Gate boundary
CI evidence establishes adapter/harness integrity only. It does **not** establish that Gazebo, MuJoCo, OpenUSD, 3DGS, or any other external backend is production-ready.

## Required later evidence
- Environment-specific simulator installation and smoke tests.
- Dependency/security review.
- Digital Twin compatibility.
- Telemetry/provenance integration.
- Cross-department regression.

## Result
**SIM-OSS-04: CI REGRESSION BOUNDARY REGISTERED**

Production approval remains blocked until backend-specific evidence is collected.
