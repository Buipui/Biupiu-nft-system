# Biupiu World Engine Resource Integration v1.0

**Date:** 19 September 2026  
**Status:** RESEARCH INTEGRATION REGISTERED — no proprietary engine code or game assets copied

## Purpose

This document integrates reusable ideas, open-source tools and learning references associated with Rockstar RAGE, Unity 6 and Guerrilla/Kojima Decima into the Biupiu World modular framework. These engines are treated as architectural reference points and adapter targets, not as redistributable dependencies.

## Key legal and technical boundary

- **RAGE:** proprietary Rockstar technology. Public modding utilities and reverse-engineering tools may be useful for format research only; they do not grant rights to RAGE source code, Rockstar game assets or proprietary formats.
- **Decima:** proprietary engine technology. Open-source projects such as Decima Workshop, DecimaTools and ProjectDecima are research/modding tools, not the Decima engine itself. Do not import game assets, keys, encrypted data or proprietary code into Biupiu World.
- **Unity 6:** commercial engine with its own licensing and package terms. Open-source Unity packages can be evaluated individually, but Unity runtime/editor redistribution and package compatibility must be checked separately.
- **Open books:** use legally accessible documentation, open licences and educational references. Do not mirror or redistribute copyrighted books merely because a repository links to them.

## Integration model

Biupiu World remains engine-agnostic at the authoritative layer:

`Biupiu OS authoritative state → World Adapter Contract → renderer/physics/navigation provider → telemetry → validation → provenance record`

The initial implementation target remains a safe modular prototype, not a claim that Biupiu has embedded RAGE, Unity or Decima.

## Registered resource groups

### RAGE reference stream

1. **SparkAll** — open-source RAGE archive editor; useful only for studying archive-tool architecture and format-handling boundaries.
2. **RAGE Console Resource Converter** — research utility for selected RAGE console formats; use only for lawful personal research and never as a source of Rockstar assets.
3. **Public RAGE architecture notes** — conceptual reference for modular engine services and cross-platform abstraction. Treat community notes as unverified unless corroborated.

**Biupiu use:** derive generic interfaces for archive inspection, asset metadata, importer isolation, version detection and read-only sandboxing. No RAGE runtime or proprietary asset dependency is introduced.

### Unity 6 reference stream

1. **Unity open-source package ecosystem / OpenUPM** — package discovery and versioned dependency metadata.
2. **Unity Standard Assets compatibility projects** — educational reference for modernising legacy controllers and vehicle/FPS patterns; compatibility must be tested against the exact Unity 6 project configuration.
3. **Unity UI Extensions** — reusable UI controls with published licences; evaluate as optional presentation-layer dependency.
4. **Curated awesome-Unity lists** — discovery only; every selected package requires independent licence, maintenance, security and Unity-version validation.

**Biupiu use:** define a Unity 6 adapter for scene import/export, input, UI, navigation, physics provider selection and build profiles. Keep the authoritative simulation contracts outside Unity-specific scripts.

### Decima reference stream

1. **ShadelessFox/decima-workshop** — open-source GUI tool for browsing, previewing, exporting and repacking selected Decima game resources.
2. **Wunkolo/DecimaTools** — reverse-engineering notes and tools.
3. **REDxEYE/ProjectDecima** — archived research tool; not the preferred current reference.
4. **Jayveer/Decima-Explorer** — archive packing/unpacking research with stated caveats and third-party components.

**Biupiu use:** study resource-browser UX, typed object metadata, import/export pipeline separation, archive integrity checks and read-only analysis. Do not create a Decima runtime adapter that depends on proprietary game data.

### Open-book and educational stream

- Game Engine Architecture — subsystem decomposition, tools, profiling, asset databases and world-object models.
- Foundations of Game Engine Development — mathematics, rendering, models/materials and physics.
- Scratchapixel, LearnOpenGL and open educational graphics resources — rendering and mathematics study references.
- Open-source game-engine development lists — discovery index for ECS, rendering, physics, geometry, shaders and asset pipelines.

Educational material is linked as learning input, not copied into production code without rights review.

## Biupiu World subsystem mapping

| Biupiu subsystem | Reusable lesson | Integration rule |
|---|---|---|
| WORLD-CORE | Engine-agnostic world object model | Authoritative schemas stay provider-neutral |
| ASSET-PIPELINE | Typed resources, archives, import/export | Read-only inspection first; hash every source |
| RENDER | Renderer abstraction and LOD/streaming concepts | Provider adapters only; no proprietary shader/code import |
| PHYS-SYS | Fixed timestep, collision, rigid-body contracts | Reuse existing Biupiu physics adapter boundary |
| NAVIGATION | World partition, terrain and navigation data | Validate deterministic transforms and provenance |
| UI/HMI | Editor and runtime tooling patterns | Optional Unity 6 presentation adapter |
| PROVENANCE | Source identity, licence and dependency records | Fail closed on unknown or incompatible licences |
| TESTING | Round-trip, equivalence and regression checks | Promotion requires measurable validation |

## Proposed repository additions

- `research/BIUPIU-WORLD-ENGINE-RESOURCE-MANIFEST-v1.0.json`
- `research/BIUPIU-WORLD-ENGINE-RESOURCE-INTEGRATION-v1.0.md`
- Future: `world/adapters/unity6/` for optional Unity 6 adapter contracts only
- Future: `world/tools/decima-rage-research/` for isolated, read-only research utilities if needed

## Acceptance gates

1. Confirm source URL, commit/tag and licence.
2. Classify as reference, optional dependency, adapter, or prohibited proprietary input.
3. Check compatibility with the current Biupiu OS / World contracts.
4. Run static checks and deterministic fixtures before runtime promotion.
5. Preserve hashes, provenance and dependency versions.
6. Keep human release authority; no automatic promotion from external repositories.

## Result

The resource families are integrated at the **architecture and registry level**. No claim is made that RAGE, Unity 6 or Decima has been embedded, and no proprietary engine source or game assets are imported. Runtime adapter implementation remains a separate, host-based validation gate.
