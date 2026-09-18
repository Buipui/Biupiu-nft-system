# Biupiu Arnold Rendering Resource Register v1.0

**Updated:** 18 September 2026

## Purpose

This register integrates publicly available GitHub resources identified for Autodesk Arnold into the Biupiu 3D / rendering research pipeline. It is a research and integration register, not a declaration that third-party code is licensed for redistribution.

## Priority resources

### 1. Autodesk/arnold-usd
Repository: https://github.com/Autodesk/arnold-usd
Category: Official Autodesk / Arnold + OpenUSD
Priority: P1

Use:
- Arnold render delegate and USD integration research
- USD scene interchange and pipeline architecture
- Arnold schemas/material relationships
- procedural, instancing, volume, motion-blur and AOV workflow research
- foundation for a Biupiu USD master-scene strategy

Biupiu integration target:
- Establish USD as a neutral interchange layer where practical.
- Cross-reference Arnold scenes/materials with Maya, Blender, Houdini and other DCC/rendering resources.
- Keep renderer-specific implementations separated from canonical asset definitions.

### 2. Autodesk/standard-surface
Repository: https://github.com/Autodesk/standard-surface
Category: Official Autodesk shader specification/reference
Priority: P1

Use:
- physically based material reference
- consistent surface definitions
- cross-renderer material research
- vehicle paint, carbon/hemp composite, textile, ceramic, glass, metal, soil, vegetation and architectural-material studies

Biupiu integration target:
- Build a renderer-neutral material taxonomy around Standard Surface concepts.
- Record material parameters independently from any single renderer.

### 3. LumaPictures/usd-arnold
Repository: https://github.com/LumaPictures/usd-arnold
Category: Production/VFX USD + Arnold reference
Priority: P2

Use:
- USD schemas and Arnold integration patterns
- exporter/importer research
- production-pipeline interoperability reference

Biupiu integration target:
- Study architecture and interoperability patterns.
- Do not copy or redistribute code until its applicable licence and dependencies are reviewed.

### 4. Autodesk/sitoa
Repository: https://github.com/Autodesk/sitoa
Category: Official Autodesk / historical Arnold integration
Priority: P3 / legacy research

Use:
- historical Arnold plugin architecture
- renderer integration patterns
- legacy shader/driver concepts

Biupiu integration target:
- Reference only unless a specific legacy interoperability requirement emerges.

## Additional GitHub candidates

Search results also identified:
- mtoatools
- Auto-Texture-File-Assigner-MtoA
- mtoa_extensions
- Arnold-For-Blender
- btoa
- SeExprArnold
- oslShaders / osl_shaders
- OpenWalter

These remain candidate resources pending repository-by-repository licence, maintenance, compatibility and dependency review.

## Biupiu rendering architecture

Recommended pipeline:

Research / CAD / procedural generation
        |
        v
Canonical geometry + metadata
        |
        v
OpenUSD interchange layer
        |
   +----+----+----------------+
   |         |                |
   v         v                v
 Arnold     V-Ray          KeyShot/Lumion/
            pipeline        other renderers
   |
   v
AOVs / materials / lighting / final renders
   |
   v
Biupiu World / vehicle / product / environment assets

## Department applications

Arnold resources are relevant to:
- Biupiu World environments and characters
- automotive and marine concept visualization
- microturbine and advanced-engineering renders
- regenerative agriculture environments
- architecture and eco-estate visualization
- textiles and composite-material visualization
- product packaging
- advanced-material research visualization
- photonics/optical-system visualization
- computational-geometry artwork

## Licensing and provenance rule

Do not vendor third-party repositories into production merely because they are public on GitHub. For each dependency record:
1. repository URL
2. commit/tag/version used
3. licence
4. upstream owner
5. dependency requirements
6. intended Biupiu use
7. modifications, if any
8. redistribution/commercial-use status

Official Autodesk repositories remain upstream references unless their individual licence permits the exact intended use.

## Status

Integrated into the Biupiu rendering research track. No third-party repository has been copied into the codebase by this register alone.
