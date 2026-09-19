# Biupiu Bevy Resource Registry v1.0

**Date:** 19 September 2026  
**Status:** EXECUTED — research registry + reusable adapter scaffold added

## Purpose

Register Bevy as an open-source Rust runtime/reference for Biupiu simulation, digital-twin visualization, interactive tooling, procedural geometry, ECS orchestration and cross-platform rendering experiments.

## Primary sources

| Resource | Role | Licence / boundary | Biupiu use |
|---|---|---|---|
| bevyengine/bevy | Core engine, ECS, rendering, assets, input, application runtime | Apache-2.0 / MIT; verify dependency and asset notices before redistribution | Reference + dependency candidate |
| Bevy official examples | Runnable ECS, rendering, shader, headless and tooling patterns | Follow upstream repository notices | Implementation patterns |
| Bevy Book / official learning material | Open learning/documentation source | Documentation provenance retained | Architecture and onboarding reference |
| bevy-website learning-code-examples | Tested learning examples | Upstream licence/provenance applies | Example validation patterns |
| bevy-cheatbook/bevy-cheatbook | Community reference | External documentation; verify current version before use | Secondary reference only |
| Bevy Assets | Community ecosystem index | Each dependency must pass individual licence review | Discovery only |

## High-value capabilities identified

- ECS architecture for modular simulation entities and systems.
- Plugin architecture for department-specific runtime modules.
- 2D/3D rendering and PBR.
- glTF asset loading.
- Render-world extraction for GPU-facing data.
- Custom render phases and shaders.
- Headless operation for server/CI-style simulation.
- Diagnostics, logging and system stepping.
- Hierarchical entity transforms.
- UI/input systems.
- GPU compute and procedural rendering examples.
- Cross-platform Rust runtime suitable for a dedicated simulation adapter.

## Biupiu routing

- AERO / MARINE / AUTO — interactive vehicle and hangar/vehicle visualization.
- DIGITAL-TWIN — ECS entities as runtime representations of approved twin records.
- CG-3D / GEOMETRY — procedural geometry and scene inspection.
- ROBOTICS / PHYS-SYS — simulation orchestration and visualization.
- ADV-MFG / MAN — factory/workcell visualization.
- AGRI / WATER — terrain, farm and infrastructure visualization.
- AI / COMPUTE — deterministic system scheduling and GPU/CPU workload experiments.
- VIDEO-SERIES — controlled scene/showreel rendering.
- CODEX — reusable Rust/Bevy implementation patterns.

## Integration rule

Third-party Bevy source, examples, assets and plugins are not automatically copied into Biupiu. The repository stores provenance, interfaces and original adapter code. Any dependency promoted into a distributable product must pass version, licence, security and compatibility checks.

## Version pinning

The current official release checked for this integration is Bevy 0.19. The adapter is therefore pinned to the 0.19 crate line rather than the development main branch. Upgrades require a migration/compile gate.

## Verification boundary

This registry does not claim that a Bevy runtime has executed on a connected host. Runtime build, rendering, GPU, asset-loading and platform tests remain explicit validation gates.
