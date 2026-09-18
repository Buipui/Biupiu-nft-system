# Biupiu Professional Rendering Stack v1.0

**Status:** Integrated reference architecture
**Date:** 18 September 2026
**Repository role:** Personal R&D / computational-engineering / visualization track

## Purpose

Define the Biupiu professional visualization stack as a cross-engine orchestration layer. Rendering engines remain replaceable adapters; source CAD/geometry, engineering models, material records and provenance remain authoritative.

## OctaneRender integration

Primary upstream reference:

- OTOY-NZ/OctaneBlender — official OctaneBlender source repository.
- OctaneRender supports GPU-accelerated production rendering and Blender integration.
- The repository must reference, not redistribute, proprietary Octane binaries, SDKs, licenses or protected assets.

Octane adapter role:

- Blender high-quality product stills
- photorealistic material/lighting studies
- automotive, marine, aerospace/eVTOL and turbine visualization
- digital-twin presentation renders
- cinematic/showreel output
- research visualization
- AOV/pass-based compositing where supported by the installed Octane version

## Material-library track

Community Octane/Blender helper repositories may be evaluated as optional tooling for:

- material-library generation
- texture-to-material workflows
- Asset Browser organization
- reusable Biupiu material presets

Third-party repositories remain dependency candidates until license, maintenance, compatibility and provenance checks are completed.

## Cross-engine architecture

SOURCE MODEL
→ BLENDER / CAD IMPORT
→ MATERIAL + PROVENANCE
→ ENGINEERING VALIDATION
→ RENDER ADAPTER
→ OUTPUT / AOV
→ EDITORIAL / COMPOSITING
→ REVIEW
→ RELEASE

Supported/planned rendering adapters:

- Blender Cycles — baseline/open renderer
- OctaneRender — GPU/photorealistic rendering adapter
- V-Ray — comparison/production-render adapter
- Unreal Engine 5 — real-time/virtual-production adapter
- Twinmotion — rapid environment/visualization adapter
- Lumion — architectural/environment visualization adapter
- KeyShot — product visualization adapter
- Adobe media pipeline — editorial/compositing/output layer

The stack does not claim feature parity between engines.

## Unreal / Octane relationship

Render Network documentation records an OctaneRender-for-Blender integration proposal and describes Blender → OctaneRender → Unreal Engine virtual-production workflows, including USD/MaterialX and Hydra-related interoperability.

Biupiu therefore treats:

- Blender as a modelling/scene-authoring hub
- Octane as a high-end rendering adapter
- Unreal Engine 5 as a real-time/interactive/digital-twin/virtual-production adapter

This is an interoperability target, not a claim that every asset or material is automatically portable without conversion or validation.

## Distributed rendering

Render Network RNP-017 is indexed as an external infrastructure reference for OctaneRender-for-Blender distributed GPU rendering. Its status must be checked again before any production dependency is declared.

## Biupiu use cases

### Engineering
- Biupiu blade micro-turbines
- marine propulsion concepts
- automotive concepts
- eVTOL and helicopter concepts
- advanced materials and composites
- robotics and manufacturing

### Scientific/research visualization
- materials genome
- plant-based composites
- bio-adhesives/resins
- photonics
- crystal/optical research
- digital-twin scenes

### Presentation
- investor/funder visuals
- product stills
- cinematic showreels
- concept variants
- research evidence videos

## Evidence and IP controls

A render is a visualization output, not engineering validation.

Every production asset should retain:

- source model ID/version
- render engine/version
- material source/provenance
- texture/license status
- scene version
- camera/lighting preset
- render settings
- output checksum where appropriate
- evidence/claim classification
- reviewer status

Speculative concepts remain labelled as concepts/hypotheses.

## Dependency policy

Do not copy proprietary Octane source, SDK files, binaries, licensed assets or credentials into the Biupiu repository.

Store:

1. adapter interfaces;
2. version/compatibility records;
3. installation requirements;
4. external repository references;
5. license/provenance metadata;
6. reproducible scene specifications where legally distributable.

## Gate RENDER-01

**Executed:** OctaneRender added as a first-class rendering adapter in the Biupiu professional visualization architecture.

**Next validation gate:** install/version compatibility test on a workstation, followed by a controlled Blender scene rendered through Octane and compared against Cycles/V-Ray/Unreal outputs using the same source geometry and documented material assumptions.

## External references

- https://github.com/OTOY-NZ/OctaneBlender
- https://github.com/rendernetwork/RNPs/blob/main/RNP-017.md
- https://github.com/rendernetwork/RNPs/blob/main/RNP-014.md

