# VIS-NATIVE-09 — Runtime Integration & Deterministic Validation Gate v1.0

Status: SOURCE IMPLEMENTATION COMPLETE / HOST EXECUTION PENDING

## Scope
This gate integrates the first-party native visual source set into one CMake target, hardens animation input handling, adds deterministic regression records, and establishes explicit adapter contracts for OpenUSD, OpenTimelineIO and OpenSubdiv.

## Implemented
- C++20 is now the canonical native build standard for the visual library.
- CMake wires the scene, provider, manifest, renderer, shader/material, asset, GPU-pipeline, animation, geometry, subdivision, scheduler, acceleration, provider-runtime, regression and provider-adapter modules.
- Regression fixtures use a deterministic non-cryptographic FNV-1a hash. This is suitable for repeatability checks, not security/provenance integrity.
- Regression records compare fixture identity, frame, input hash and output hash.
- OpenUSD, OpenTimelineIO and OpenSubdiv have explicit first-party adapter boundaries.
- External-provider adapters are deliberately marked CONTRACT_ONLY until their real SDKs are linked and exercised on the host.
- Animation rejects non-finite keyframes, non-finite sample times and duplicate timestamps, preventing zero-span interpolation.
- Existing smoke targets are registered with CTest and a new regression/provider smoke target is included.

## Evidence state
REGISTERED: native modules and provider boundaries.
IMPLEMENTED: source-level APIs and CMake integration.
HOST_TESTED: pending. A GitHub-hosted CMake/CTest workflow was added in VIS-NATIVE-10; connector status currently reports no workflow run/status for the gate commit.
REGRESSION_PASS: pending actual CMake/CTest evidence.
VERIFIED: not claimed until host regression evidence is returned.

## Next gate
VIS-NATIVE-10 should perform real host execution: CMake configure, C++20 compile, CTest, platform GPU probe, and provider SDK discovery/link tests. Only successful host evidence may promote providers from CONTRACT_ONLY to HOST_READY.
