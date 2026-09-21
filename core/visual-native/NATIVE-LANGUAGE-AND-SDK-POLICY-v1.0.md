# Biupiu Native Language and SDK Policy v1.0

**Priority:** P0 / first-party visual systems

## Language allocation
- **C++20:** primary first-party visual/runtime implementation language. Scene graph, renderer, animation, materials, asset IO, provider ABI implementation, GPU abstraction, video pipeline orchestration and high-performance simulation.
- **C:** stable C ABI/HAL boundary for OS, plugins, FFI and long-term binary compatibility.
- **Rust:** security-sensitive tooling, isolated asset ingestion, parsers, sandboxed workers and concurrency-heavy services where memory safety materially improves the component. Rust is not forced into hot rendering paths.
- **Python:** research, offline asset processing, dataset tooling, test orchestration and DCC adapters. Not the authoritative runtime.
- **HLSL/GLSL/SPIR-V:** GPU shader layer. Shader source remains platform-specific; Biupiu owns shader/material contracts.
- **CMake:** canonical native build orchestration.
- **C#:** Unity adapter only; not first-party core.
- **Unreal C++:** UE5 adapter only; not first-party core.

## SDK/provider policy
Preferred open standards/providers: OpenUSD, OpenSubdiv, OpenTimelineIO, MaterialX, OpenColorIO, OpenImageIO, OpenEXR, Vulkan SDK, DXC and FFmpeg libraries where licence/use requirements permit.

Every SDK must pass:
licence -> version -> ABI/platform -> security -> capability -> deterministic fixture -> provenance -> regression -> promotion.

OEM binaries/dumps are evidence for interface discovery, not code to copy. Proprietary APIs are integrated only through lawful documented interfaces or clean-room-compatible adapter boundaries.

## Foreign-language protocol
Repository searches may include German, Japanese, Chinese, Korean and Russian terminology for equivalent SDKs, drivers, codecs, renderers and technical specifications. A foreign-language result is retained only with source URL, translated technical summary, licence/provenance and reproducible relevance.

## Authority rule
Biupiu-native contracts are authoritative. External engines and SDKs are dependencies/providers, never the system-of-record for canonical visual state.
