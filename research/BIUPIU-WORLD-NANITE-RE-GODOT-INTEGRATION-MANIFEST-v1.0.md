# Biupiu World — Nanite / RE Engine / Godot Integration Manifest v1.0

**Date:** 2026-09-19  
**Purpose:** Record selected open-source rendering, engine-interoperability and research resources for Biupiu World without misrepresenting external code as already embedded.

## Godot baseline

Godot Engine is free and open source under the MIT license. Godot is the proposed cross-platform orchestration and application/runtime baseline for Biupiu World, subject to platform-specific performance testing. Godot's own third-party dependencies and any imported assets retain their applicable licence obligations.

## Resource routing

| Resource | Department | Intended treatment | Current state |
|---|---|---|---|
| Godot Engine | Core runtime / application layer | Baseline engine, scene system, input, UI, export and orchestration | Architecture target; engine source not vendored by this commit |
| Nyx | Advanced geometry / rendering R&D | Study and selectively adapt Nanite-style meshlet hierarchy, GPU-driven rendering, visibility buffers, streaming and compressed geometry | Registered for integration study |
| Nano | Vulkan rendering R&D | Study meshlet/LOD/HZB/BVH techniques and cross-platform Vulkan path | Registered for integration study |
| SealLOD | Rendering / upscaling / shadows R&D | Study work graphs, virtualized geometry, shadowing, clustered lighting and upscaling interfaces | Registered for integration study |
| REFramework | Engine interoperability R&D | Study plugin, scripting, runtime inspection and modding architecture; do not embed Capcom game code | Reference-only research |
| RE Engine Modding Documentation | Asset interoperability R&D | Use as format/tooling reference; no proprietary game assets imported | Reference-only research |
| RE-Engine-Lib | Asset conversion R&D | Investigate resource-format reading and conversion workflows | Reference-only research |
| RE Engine MCP | AI testing R&D | Study agent-assisted runtime inspection/testing patterns | Reference-only research |

## Godot versus Nanite-style renderers

Godot is the general-purpose engine and application framework. Nyx, Nano and SealLOD are focused rendering implementations or research projects. They are not automatic drop-in replacements for Godot. The integration strategy is therefore:

1. Keep Godot as the application/orchestration baseline.
2. Use Godot's native renderer where it meets requirements.
3. Prototype advanced geometry techniques as separate renderer modules, extensions, or standalone R&D executables.
4. Prefer interoperable asset formats such as glTF/GLB where supported.
5. Promote a renderer into production only after platform, performance, stability and licence checks.

## Licence and provenance rules

- Record upstream URL, commit/tag, licence and dependency notices for each adopted component.
- MIT source code may be modified and used commercially when the licence notice is retained.
- Third-party dependencies, models, textures, sounds, fonts and datasets may have separate terms.
- RE Engine research must not be treated as permission to redistribute Capcom-owned game assets, binaries or proprietary content.
- External code remains externally attributed; incorporation does not make it Biupiu-owned.

## Next implementation gates

- [ ] Confirm upstream repository URLs and exact commits/tags.
- [ ] Record SPDX licence and dependency inventory for each candidate.
- [ ] Create isolated prototype branches/projects for Nyx, Nano and SealLOD.
- [ ] Define Godot interoperability boundary: asset import, scene handoff, renderer API, telemetry and fallback path.
- [ ] Benchmark against Godot baseline on Windows and Android targets.
- [ ] Add regression tests and safe fallback to the baseline renderer.
- [ ] Promote only tested modules into the production Biupiu World build.

## Status declaration

This manifest records and routes the resources. It does **not** claim that the external rendering engines or RE Engine tools have already been compiled, embedded or production-validated inside Biupiu World. Those implementation steps require a separate build environment and test evidence.
