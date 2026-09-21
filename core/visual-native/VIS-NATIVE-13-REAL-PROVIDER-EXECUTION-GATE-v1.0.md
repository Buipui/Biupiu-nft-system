# VIS-NATIVE-13 — Real Provider Execution & Deterministic Fixture Gate v1.0

Status: SOURCE IMPLEMENTATION COMPLETE / HOST EXECUTION PENDING

## Implemented
- Added a real provider execution entry point with fail-closed behavior.
- OpenUSD executes an in-memory stage fixture when the OpenUSD CMake target is actually linked.
- The fixture creates a real /Biupiu prim through the OpenUSD API and emits a Biupiu-controlled canonical representation.
- Repeated OpenUSD executions are compared byte-for-byte and by the native deterministic regression hash.
- Providers without a linked/validated SDK remain CONTRACT_ONLY; no provider is promoted from compile-time discovery alone.
- Unknown providers are rejected.

## Evidence rules
HOST_READY requires successful compilation against the SDK and successful runtime fixture execution.
REGRESSION_PASS requires repeated execution with identical canonical output.
VERIFIED additionally requires host/CI evidence captured from an actual workflow run.

## Current evidence
- Source implementation: IMPLEMENTED.
- OpenUSD runtime: conditional on host SDK availability; not yet evidenced by a CI run.
- OTIO/OpenSubdiv/MaterialX/OpenColorIO/OpenImageIO/OpenEXR: adapter execution remains pending.
- CI/CTest: pending actual workflow execution.
- VERIFIED: not claimed.

## Next gate
VIS-NATIVE-14 — extend runtime fixtures to OTIO/OpenSubdiv and the material/color/image providers, capture versioned runtime evidence, and promote only providers that pass host execution plus deterministic repeat tests.
