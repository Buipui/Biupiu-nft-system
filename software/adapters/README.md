# Biupiu External Adapter Boundary v0.1

This directory contains original, provider-neutral adapter contracts and manifests.

## Rules
- No vendor SDK headers or proprietary samples are copied into Biupiu Core.
- External projects remain optional dependencies or research references until licence, security, compatibility and build checks pass.
- Adapters must report capability and evidence state rather than assuming availability.
- Host execution, GPU detection and physical device validation remain separate gates.

## Initial candidates
- NVIDIA NVRHI: MIT-licensed external rendering abstraction candidate.
- NVIDIA RTXDI / OptiX: isolated research candidates with separate SDK/dependency review.
- DirectX 12/DXR and Vulkan: host backend targets.

The adapter layer is not an engine replacement. It is a stable Biupiu contract between the OS/Intelligence layer and specialist rendering, audio and display systems.
