# VIS-NATIVE-14 — Provider Runtime Fixture Expansion Gate v1.0

Status: SOURCE IMPLEMENTATION COMPLETE / HOST EXECUTION PENDING

## Implemented
- MaterialX runtime fixture: creates a real MaterialX document and constant color node when the SDK is linked.
- OpenColorIO runtime fixture: creates a real Config object when the SDK is linked.
- OpenImageIO runtime fixture: creates and validates a real ImageSpec when the SDK is linked.
- OpenEXR runtime fixture: creates and validates a real 2x2 Header when the SDK is linked.
- Provider state promotion remains conditional on actual CMake SDK linkage.
- Runtime smoke coverage now exercises the expanded providers when their corresponding compile/link definitions exist.
- Unknown providers remain fail-closed.
- Canonical output remains Biupiu-controlled rather than depending on unstable third-party serialization.

## Evidence rules
HOST_READY requires successful compilation and runtime fixture execution against the linked SDK.
REGRESSION_PASS requires repeated deterministic execution with identical canonical output.
VERIFIED requires captured host/CI evidence from an actual workflow run.

## Current evidence
- Source implementation: IMPLEMENTED.
- MaterialX/OpenColorIO/OpenImageIO/OpenEXR fixtures: IMPLEMENTED, host execution pending.
- OpenUSD fixture: IMPLEMENTED, host execution pending.
- OpenTimelineIO/OpenSubdiv: runtime fixtures still pending.
- CI/CTest: no workflow evidence currently returned for the latest gate commits.
- VERIFIED: not claimed.

## Research basis
MaterialX documents define node/document structures and node creation semantics. OpenColorIO's current tests demonstrate Config creation and processor APIs. OpenSubdiv remains isolated behind its adapter boundary pending a verified fixture API. 

## Next gate
VIS-NATIVE-15 — implement verified OpenTimelineIO and OpenSubdiv runtime fixtures, add repeated-run provider evidence records, and extend CI dependency installation without making unavailable SDKs mandatory.
