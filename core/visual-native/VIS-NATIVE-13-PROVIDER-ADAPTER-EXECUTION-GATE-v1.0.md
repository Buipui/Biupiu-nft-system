# VIS-NATIVE-13 — Real Provider Adapter Execution & Deterministic Fixture Gate v1.0

Status: PARTIAL SOURCE IMPLEMENTATION / HOST EXECUTION PENDING

## Implemented
- OpenUSD adapter now executes a real in-memory USD stage when the OpenUSD SDK is actually discovered and linked.
- The runtime fixture defines a deterministic sphere prim at `/Biupiu/VisualFixture`, validates its type and radius, and produces a canonical Biupiu-owned hash.
- OpenUSD is promoted to `HOST_READY` only after the runtime fixture succeeds.
- Repeated OpenUSD fixture execution is checked for identical canonical output hashes.
- CMake links `pxr::usdGeom` when that exported target is available.
- When OpenUSD is unavailable, the adapter remains fail-closed and reports CONTRACT_ONLY; no simulated HOST_READY state is produced.

## Evidence boundary
The source can now perform genuine OpenUSD runtime execution, but this branch has not yet produced a successful CI/host run proving that OpenUSD is installed and linked. Therefore HOST_TESTED and VERIFIED remain unclaimed.

## Provider matrix
- OpenUSD: REAL RUNTIME FIXTURE IMPLEMENTED; HOST_TESTED pending.
- OpenTimelineIO: CONTRACT_ONLY; runtime fixture pending.
- OpenSubdiv: CONTRACT_ONLY; runtime fixture pending.
- MaterialX: REAL RUNTIME FIXTURE IMPLEMENTED; HOST_TESTED pending.
- OpenColorIO: validation boundary only; runtime fixture pending.
- OpenImageIO: validation boundary only; runtime fixture pending.
- OpenEXR: validation boundary only; runtime fixture pending.

## VIS-NATIVE-14 incremental execution
- MaterialX now creates a real in-memory Document, adds a deterministic node, validates the document, and hashes a Biupiu-controlled canonical representation when the SDK is linked.
- Repeated MaterialX fixture execution is checked for identical hashes.
- MaterialX remains CONTRACT_ONLY until host/CI evidence proves the SDK-linked path actually executed.

## Promotion requirements
1. SDK discovered and linked.
2. Runtime fixture succeeds.
3. Canonical output is non-zero.
4. Repeated runs produce identical hashes.
5. CI/host evidence is recorded.
6. Provider/version/platform evidence is retained.

## Current state
REGISTERED: yes.
IMPLEMENTED: yes.
HOST_TESTED: pending external CI/host execution.
REGRESSION_PASS: pending successful provider runtime execution.
VERIFIED: not claimed.

## Reference
OpenUSD documents `UsdStage::CreateInMemory` and schema definition APIs used by this gate. See official OpenUSD API/tutorial documentation. 
