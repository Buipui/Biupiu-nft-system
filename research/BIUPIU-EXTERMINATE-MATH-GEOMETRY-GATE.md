# BIUPIU EXTERMINATE PROTOCOL — MATH/GEOMETRY GATE

**Date:** 19 September 2026
**Scope:** recent MATH, computational geometry, AI/robotics/digital-twin integration work.

## Gate actions
1. Re-read recently added source files.
2. Check for obvious syntax/import hazards.
3. Check that optional dependencies remain optional.
4. Preserve third-party provenance boundaries.
5. Add automated compilation and dependency-light test execution.
6. Record that runtime tests require an actual GitHub Actions run.

## Findings and fixes
- Geometry primitives are dependency-light and compile without external packages.
- OR-Tools remains optional and is only imported inside the adapter call.
- MoveIt 2 remains an adapter contract; no physical actuator path is present.
- AI outputs retain explicit evidence states and cannot silently become proofs.
- Digital-twin interface records provenance/version information.
- Geometry tests are routed through repository-root PYTHONPATH in CI.
- No third-party source was copied into Biupiu core during this gate.

## Next gate
GitHub Actions must execute the new Math Geometry Gate. Only an actual successful workflow run may promote the code from adapter/test-pending to validated.

## Promotion rule
DISCOVERED → ISOLATED → REVIEWED → TESTED → SIMULATED → VALIDATED → INCORPORATED

No physical deployment or autonomous actuator control is enabled by this gate.
