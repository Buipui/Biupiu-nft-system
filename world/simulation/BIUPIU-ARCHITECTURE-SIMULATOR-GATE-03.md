# Biupiu Architecture Simulator — Gate 03

Status: IMPLEMENTED — repository-level smoke-test gate
Date: 2026-09-22

## Objective
Turn Gate 02's validation specification into executable regression tests for the architecture simulator before any engine/runtime claim is made.

## Tests implemented
- CRS is mandatory for GIS site import.
- GREEN assets are eligible for build candidates.
- RED assets are blocked.
- Country filtering is deterministic.
- Architectural massing is deterministic for valid inputs.
- Validation fails closed when no site is imported.
- A valid GIS site plus GREEN assets passes repository validation.

## Verification boundary
This gate verifies the simulator's Python architecture layer and its fail-closed rules. It does **not** verify:
- Unreal Engine execution.
- Blender import/export round-trip.
- Real GIS/LiDAR/LAZ ingestion.
- Android runtime.
- GPU/VR performance.
- External asset licence ownership beyond the manifest classifications.

Those remain OPEN runtime/integration gates.

## Required next gate
Execute the same contract against a real GIS/LiDAR fixture and establish the Blender/Unreal interchange path. Runtime results must be captured before marking those gates VERIFIED.
