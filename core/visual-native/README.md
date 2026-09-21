# Biupiu Native Visual System v1.0
**Gate:** VIS-NATIVE-01
**Status:** ARCHITECTURE + SOURCE-LEVEL CONTRACT IMPLEMENTED
**Runtime status:** NOT YET VERIFIED on host hardware

## Purpose
Provide one Biupiu-native API boundary for rendering, animation and video/media jobs. Unity, Unreal Engine 5, Blender, V-Ray, Lumion and future native renderers are providers/adapters; none is the authoritative visual state.

## Architecture
Biupiu OS/DMS -> Native Visual API -> Render/Animation/Video providers -> output manifest -> validation/provenance -> Intelligence

The API uses the existing C ABI/HAL boundary. C++ may implement high-performance graphics services; Rust may implement memory/concurrency/security-sensitive services. Durable boundaries use C-compatible types and opaque handles.

## Core capabilities
- GPU/API capability discovery
- canonical scene/asset submission
- material/environment/camera state
- animation timelines, clips and deterministic sampling
- render jobs and frame/sequence outputs
- video encode/export jobs
- thumbnails/previews
- hashes and provenance
- provider selection and fallback
- cancellation, health and diagnostics
- deterministic test hooks

## Non-goals
This gate does not claim a proprietary renderer, encoder or animation solver has been implemented. It creates the native contract and adapter boundary.

## Next runtime gate
VIS-NATIVE-02: implement a minimal host provider and execute render -> animation sample -> video encode smoke tests.
