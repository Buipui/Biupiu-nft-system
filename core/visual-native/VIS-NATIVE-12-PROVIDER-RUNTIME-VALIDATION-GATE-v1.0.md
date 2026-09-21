# VIS-NATIVE-12 — Provider Runtime & Deterministic Cross-Validation Gate v1.0

Status: SOURCE IMPLEMENTATION COMPLETE / HOST PROVIDER EXECUTION PENDING

## Implemented
- Added a fail-closed provider validation boundary for OpenUSD, OpenTimelineIO, OpenSubdiv, MaterialX, OpenColorIO, OpenImageIO and OpenEXR.
- Canonical input/output hashes are recorded for deterministic fixture comparison.
- Provider state cannot become HOST_READY from compile-time discovery alone.
- Unsupported providers are rejected.
- Validation records explicitly separate discovery, linkage, runtime probe and deterministic-pass evidence.

## Required promotion evidence
1. SDK discovered.
2. SDK linked into the native target.
3. Provider runtime fixture executes successfully.
4. Canonical output hash matches the approved fixture.
5. Repeated execution is deterministic.
6. Provider/version/platform evidence is recorded.

## State
REGISTERED: validation boundary.
IMPLEMENTED: source API + smoke test.
HOST_TESTED: pending CI/host execution.
REGRESSION_PASS: pending real provider fixture execution.
VERIFIED: not claimed.
