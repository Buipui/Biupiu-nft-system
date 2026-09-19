# Biupiu Graphics / Physics / Upscaling GitHub Resource Registry v1.0

**Date:** 19 September 2026  
**Status:** EXECUTED — research/dependency integration
**Scope:** Biupiu World + private Biupiu World R&D Centre + Unreal/desktop graphics pipeline

## Integration rule
Third-party projects remain external dependencies/references unless their licences and redistribution terms are explicitly reviewed. This registry records source URLs, release targets, intended adapters and validation status; it does not claim third-party ownership.

## Graphics / rendering
- SaschaWillems/Vulkan — Vulkan examples, compute, ray tracing, PBR, GPU particles and synchronization reference.
- nvpro-samples/vk_gltf_renderer — glTF/Vulkan renderer and asset-pipeline reference.
- haasn/libplacebo — shader/video processing, high-quality scaling, HDR/tone mapping and colour management.
- GPUOpen WorkGraphs DirectX samples — DirectX 12 work-graph/GPU scheduling research.
- Microsoft DirectX-Graphics-Samples — DX12/DXR graphics and GPU programming reference.

## Physics / simulation
- jrouwe/JoltPhysics — v5.6.0; primary candidate for high-performance rigid/soft-body/vehicle-style runtime physics.
- jrouwe/JoltPhysics.js — v1.1.0; browser/JS simulation parity experiments, updated for Jolt 5.6.0.
- NVIDIA-Omniverse/PhysX — PhysX 5.x; alternate/reference solver, destruction/flow extensions and Omniverse interoperability.
- bulletphysics/bullet3 — PyBullet 3.2.5; robotics, learning, rapid prototyping and Python validation reference.
- JSBSim — current project; flight dynamics adapter already registered under FLIGHT-SIM-01.

## Upscaling / reconstruction / frame generation
- GPUOpen-LibrariesAndSDKs/FidelityFX-SDK — FSR SDK v2.3.0; documentation includes FSR Upscaling 4.1.1 and Frame Generation 4.0.1.
- intel/xess — XeSS SDK 3.0.1; XeSS-SR, XeSS-FG and XeLL.
- optiscaler/OptiScaler — active 0.9.x line; interoperability research for DLSS/FSR/XeSS inputs; not a default runtime dependency.
- pmndrs/upscaler — feature-complete WebGPU spatial/temporal upscaling reference.
- cashcon57/open-supersampling — active pre-alpha vendor-neutral SR/temporal reconstruction research; not production dependency.

## Selection policy
1. Prefer official upstream repositories for production SDKs.
2. Pin exact versions/commits before a reproducible build.
3. Keep renderer, physics and upscaler interfaces behind Biupiu adapter contracts.
4. Never bundle proprietary DLLs, game assets, models or redistributables without licence review.
5. Never treat a GitHub project as production-ready merely because it is active.
6. Runtime validation happens on the local Windows/UE5 environment; repository integration alone does not claim a working GPU runtime.

## Proposed adapter stack
UE5 / Biupiu World -> Biupiu Graphics Adapter -> DX12/Vulkan -> Jolt or PhysX adapter -> Biupiu Reconstruction Adapter -> FSR/XeSS/native path -> telemetry/provenance.

Private experimental path: private-rd-centre -> physics solver adapters -> renderer experiments -> reconstruction experiments -> benchmark results -> explicit promotion gate.

## Licence notes
- JoltPhysics: MIT.
- NVIDIA PhysX: BSD-3-Clause.
- Bullet: Bullet/zlib-style licence.
- libplacebo: LGPL-2.1-or-later.
- XeSS SDK: Intel licence; review redistribution terms before shipping.
- AMD FidelityFX SDK: AMD licence; review component-specific terms before redistribution.
- OptiScaler: GPL-3.0; do not embed into proprietary Biupiu binaries without dedicated licence/compliance review.
- OpenSuperSampling: Apache-2.0 repository; model weights/future components may have different terms.

## Validation state
Repository integration: complete.
Dependency download/build: not claimed.
GPU runtime benchmark: pending local Windows/UE5 environment.
Automatic third-party code copying: intentionally disabled.