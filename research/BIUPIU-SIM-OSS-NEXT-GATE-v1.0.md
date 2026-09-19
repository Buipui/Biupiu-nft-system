# Biupiu SIM-OSS Next Gate v1.0

## Gate objective
Move from adapter implementation to controlled backend validation and integration planning.

## Required validation pipeline
1. Repository provenance and licence verification.
2. Dependency and security review.
3. Local backend availability probe.
4. Minimal smoke test in an isolated environment.
5. Simulator adapter contract test.
6. Digital Twin interface compatibility test.
7. Telemetry/provenance recording.
8. Regression test before promotion.

## Promotion states
discovered-reference
-> licence-reviewed
-> dependency-reviewed
-> adapter-tested
-> smoke-tested
-> digital-twin-compatible
-> validated
-> production-approved

## Current Biupiu status
- Repository registry: implemented.
- Simulator adapter: implemented.
- Fail-safe command construction: implemented.
- Regression tests: implemented.
- External backend installation: NOT performed automatically.
- Production promotion: BLOCKED until environment-specific validation passes.

## Backend priorities
1. Gazebo / gz-sim
2. ros_gz
3. MuJoCo / DISCOVERSE
4. OpenUSD integration
5. Gaussian Splatting / Real2Sim
6. DLR OAISYS / Blender research
7. rbot / AMR navigation

## Safety
External code is never executed merely because it appears in the repository registry. Installation, execution, model loading and production promotion require explicit validation gates. The Core OS remains authoritative; AI and simulator suggestions are non-authoritative until OS validation.

## Gate result
SIM-OSS-02: VALIDATION PIPELINE REGISTERED
