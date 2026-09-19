# Biupiu Assassin's Creed Shadows Rendering Resource Index v1.0

**Status:** Integrated reference architecture  
**Date:** 19 September 2026  
**Track:** R&D OS → Computational Engineering → CG-3D → Unreal Engine 5 → World Development Lab → Cinematic Rendering

## Purpose

This package captures publicly accessible technical research associated with *Assassin's Creed Shadows* as a **reference/technique study**, not as a source of Ubisoft proprietary game assets, code, textures, characters, maps, or binaries.

The target is to reproduce useful rendering characteristics through original Biupiu implementations in Unreal Engine 5 and the provider-neutral rendering stack.

## Reference findings

### 1. Ray tracing and global illumination
The GitHub GPU-Book indexes the SIGGRAPH 2025 presentation **“Ray Tracing the World of Assassin's Creed Shadows”** alongside other real-time-rendering research.

Reference:
- https://github.com/Gforcex/GPU-Book
- https://github.com/ttaekgeun/PIKA

Use in Biupiu:
- RTGI research
- ray-traced reflections
- dynamic indirect lighting
- lighting quality/performance experiments
- comparison against Lumen/DDGI/other open implementations

### 2. Hybrid dynamic-GI research
The PIKA repository links DDGI research and the Assassin's Creed Shadows ray-tracing presentation.

Use in Biupiu:
- probe-based GI fallback
- mobile/performance-oriented GI experiments
- RT/GT/SSGI/DDGI comparison
- scalability tests for large environments

### 3. Open ray-tracing validation
Khronos' Vulkan ray-tracing tutorial provides an independent open implementation path for ray-query shadows, acceleration structures and reflections.

Reference:
- https://github.com/KhronosGroup/Vulkan-Tutorial

Use in Biupiu:
- low-level validation experiments
- BLAS/TLAS concepts
- ray-query shadow/reflection tests
- RenderDoc/Nsight debugging workflow references

### 4. Neural/global-illumination research
Microsoft RenderFormer provides an open neural-rendering implementation with global illumination, reflections, indirect lighting and complex shadowing.

Reference:
- https://github.com/microsoft/renderformer

Use in Biupiu:
- research-only neural-rendering benchmark
- offline/hero-render comparison
- future AI-assisted material/light transport research

### 5. Radiance-cache research
NVIDIA SHARC provides an open radiance-cache integration reference for accelerating path tracing.

Reference:
- https://github.com/NVIDIA-RTX/SHARC

Use in Biupiu:
- radiance-cache experiments
- large-world indirect-lighting research
- cache occupancy/debug instrumentation
- performance/quality trade-off studies

## Unreal Engine 5 mapping

The resource package feeds the existing:

Biupiu R&D OS
→ Unreal Engine 5 integration
→ World Development Lab
→ World/Environment Pipeline
→ Rendering Adapter
→ Cinematic / Digital Twin / Showcase

### Rendering stack

1. **Primary real-time renderer:** Unreal Engine 5
2. **Scene construction:** original Biupiu geometry + procedural generation
3. **World:** World Partition / PCG where appropriate
4. **Lighting:** Lumen baseline + RT experiments where supported
5. **Reflections:** Lumen/RT comparison
6. **GI research:** DDGI / radiance-cache / open research adapters
7. **Materials:** PBR / MaterialX-compatible asset descriptions where applicable
8. **Atmospherics:** original fog, volumetrics, weather and environmental systems
9. **Cinematics:** Sequencer / Movie Render Graph
10. **Interchange:** OpenUSD / glTF / FBX through existing RED-05/RED-06 contracts
11. **Validation:** render benchmark + provenance + licence/IP gates

## Japan environment implementation target

Create an original **Biupiu Japan World** environment with:

- mountain and forest terrain
- villages and urban districts
- shrines/temples and period-inspired architecture
- roads, bridges and water systems
- bamboo, grasses, trees and seasonal foliage
- rain, wind, mist and snow variants
- wet materials and puddle response
- dawn/day/sunset/night lighting
- volumetric atmosphere
- original characters and clothing
- original props and vehicles
- cinematic camera paths

These are **original Biupiu production targets**, not extracted Assassin's Creed assets.

## Performance tiers

### Tier A — baseline
Raster/Lumen-friendly scene with scalable foliage, materials and lighting.

### Tier B — enhanced
Selective hardware RT, higher-quality reflections and denser environmental effects.

### Tier C — cinematic
High-quality RT/path-tracing experiments, high-resolution output and Movie Render Graph.

### Tier D — research
Experimental neural rendering, radiance caching and alternative GI implementations.

Every tier must record:
- engine/version
- renderer mode
- GPU/CPU
- resolution
- frame time/FPS
- memory
- scene version
- asset manifest
- output hash
- visual-quality observations
- licence/IP state

## Rights gate

**Allowed:** technical papers, publicly accessible research descriptions, open-source implementations under their stated licences, and original Biupiu recreations.

**Blocked by default:** Ubisoft game binaries, extracted game files, proprietary source code, ripped textures/materials, characters, maps, meshes, animations, audio, or other copyrighted game assets unless separately licensed.

External research is converted into:
**SOURCE → TECHNIQUE → COMPATIBILITY TEST → ORIGINAL IMPLEMENTATION → VALIDATION → PROVENANCE**

## Acceptance criteria

- No proprietary Assassin's Creed asset is copied into the repository.
- Every external code dependency has a licence record.
- Every Biupiu implementation is original or appropriately licensed.
- Rendering experiments are reproducible and benchmarked.
- UE5 remains the production integration endpoint.
- The Japan World remains visually inspired by the desired quality characteristics without becoming a derivative asset copy.

## Gate status

**ACS-01 — Research indexing:** EXECUTED  
**ACS-02 — UE5 architecture mapping:** EXECUTED  
**ACS-03 — Rights/provenance boundary:** EXECUTED  
**ACS-04 — Japan environment target specification:** EXECUTED  
**ACS-05 — Live UE5 render validation:** GATED until a connected UE5 workstation/editor is available  
**ACS-06 — Cross-renderer benchmark:** GATED until connected renderer hosts are available
