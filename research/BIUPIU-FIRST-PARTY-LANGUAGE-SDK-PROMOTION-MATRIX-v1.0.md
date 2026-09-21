# Biupiu First-Party Language & SDK Promotion Matrix v1.0
Date: 2026-09-21
Priority: P0
Status: AUDITED / NATIVE-FIRST

## First-party language allocation
- C11: durable ABI/HAL, boot-facing primitives, portable FFI.
- C++17+: native visual renderer, geometry, simulation, numerical kernels, robotics and high-performance AI.
- Rust: memory-safe services, concurrency, security, device/embedded services and selected AI infrastructure.
- Python 3: orchestration, research tooling, Blender automation, data pipelines and test generation; never the authoritative native ABI.
- TypeScript/JavaScript: UI/DMS/gateway tooling only; not native rendering truth.
- HLSL/GLSL: shader programs compiled through validated toolchains; shader source is a first-party asset, not a general-purpose systems language.
- CMake: canonical native build orchestration.
- PowerShell/Bash: host automation only.

## Native visual SDK stack
Core: C/C++ + C ABI + CMake
Scene/interchange: OpenUSD
Geometry: OpenSubdiv
Materials: MaterialX
Images: OpenImageIO + OpenEXR
Colour: OpenColorIO
Editorial: OpenTimelineIO
Shaders: HLSL/GLSL + DXC/SPIR-V toolchain
GPU: Direct3D 12 and Vulkan adapters
Media: FFmpeg libraries behind Biupiu video API
Authoring/provider: Blender Python API, UE5 C++ adapter, Unity adapter later

## Promotion rule
No external SDK becomes first-party core merely by being indexed. It must pass licence, ABI, build, smoke, security, regression and provenance gates.

## OEM / foreign-language search
Search source classes include official OEM SDKs, vendor developer portals, public Git repositories, standards bodies, and foreign-language research indexes. Preserve original-language identifiers and source provenance. Translation is never evidence of implementation.

## Native-first priority
1. Biupiu ABI and memory ownership
2. Native scene graph
3. Native geometry/material interfaces
4. DX12/Vulkan backend
5. shader compilation
6. image/colour pipeline
7. animation/timeline
8. frame/video pipeline
9. deterministic regression
10. external engine adapters

## Verified-vs-open policy
Architecture and source integration are not host execution evidence. Runtime promotion requires actual build/test artifacts.
