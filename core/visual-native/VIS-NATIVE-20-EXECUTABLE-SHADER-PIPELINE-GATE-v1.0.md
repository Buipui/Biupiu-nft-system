# VIS-NATIVE-20 — Executable Shader Pipeline Gate v1.0

## Purpose
Turn the native shader contract into a binary-safe executable pipeline boundary.

## Implemented in this gate
- Explicit byte length for shader input; no strlen-based binary handling.
- SPIR-V 32-bit word validation.
- SPIR-V magic/version/bound/schema checks.
- Instruction-stream word-count and bounds validation.
- Deterministic SPIR-V passthrough compilation into owned native memory.
- Malformed-module rejection tests.
- HLSL/GLSL remain explicit compiler-provider paths; this gate does not pretend that source compilation is available when DXC/glslang is absent.

## Evidence protocol
The Khronos SPIR-V specification defines the module magic number 0x07230203, 32-bit word layout, version field, bound and instruction stream. citeturn0search0
Microsoft documents DXC as the reference compiler for HLSL and its SPIR-V generation path for Vulkan. citeturn0search6
Khronos documents glslang as the reference GLSL/ESSL front end and SPIR-V generator; its HLSL front end is deprecated as of April 2026, so HLSL remains assigned to DXC rather than glslang. citeturn0search4

## Gate state
- REGISTERED: yes
- IMPLEMENTED: yes
- HOST_VERIFIED: pending CI
- VERIFIED: pending CI + executable compiler/provider evidence

## Remaining dependency
Real HLSL/GLSL source compilation requires a discovered and executable DXC/glslang provider. Provider discovery alone is not promotion evidence.
