# Biupiu Professional Rendering Stack v1.1

**Status:** Integrated reference architecture  
**Date:** 18 September 2026  
**Repository role:** Personal R&D / computational-engineering / visualization track

## Maxon / Cinema 4D integration

Maxon Cinema 4D is now a first-class professional visualization and procedural-content adapter.

Official upstream GitHub references:
- Maxon-Computer/Cinema-4D-Python-API-Examples
- Maxon-Computer/Cinema-4D-Cpp-API-Examples
- Maxon-Computer/Cinema-4D-Visual-Studio-Code-Extension
- Maxon-Computer/Redshift-OSL-Shaders
- Maxon-Computer/Redshift-OCIO-Configs
- Maxon-Computer/ZBrush-Python-API-Examples

Adapter roles:
- procedural/parametric modelling
- Cinema 4D Python and C++ automation
- plugin development
- MoGraph/fields/generator workflows
- Redshift production rendering
- OSL/shader experimentation
- ZBrush sculpting/asset preparation
- engineering, marine, automotive, aerospace/eVTOL and turbine visualization
- digital-twin presentation assets

## Redshift integration

Redshift is a production-rendering sub-adapter under the Maxon route. The repository indexes OSL shaders, OCIO configuration, node/material automation and Cinema 4D → Redshift workflows.

Maxon documentation provides Python workflows using `c4d` and `maxon` for Redshift material node graphs. These are references only; proprietary binaries, SDK packages and licensed assets are not redistributed.

## Cross-engine architecture

SOURCE MODEL
→ CAD / BLENDER / CINEMA 4D
→ PROCEDURAL + MATERIAL + PROVENANCE
→ ENGINEERING VALIDATION
→ RENDER ADAPTER (CYCLES / OCTANE / V-RAY / REDSHIFT)
→ REAL-TIME ADAPTER (UNREAL / TWINMOTION / LUMION)
→ OUTPUT / AOV
→ EDITORIAL / COMPOSITING
→ REVIEW
→ RELEASE

Existing adapters remain active: Blender/Cycles, Octane, V-Ray, Unreal Engine 5, Twinmotion, Lumion, KeyShot and Adobe media pipeline.

## Biupiu use cases

- blade micro-turbines
- marine propulsion
- automotive, eVTOL and helicopter concepts
- plant-based composites and bio-resins
- photonics/crystal research
- robotics and manufacturing
- digital twins
- investor/funder visuals
- research evidence videos

## Evidence/IP boundary

A render is a visualization artifact, not engineering validation. Production assets retain source-model version, renderer/version, material provenance, licence state, scene version, render settings, output identity, evidence classification and reviewer status.

Do not copy proprietary Maxon/Cinema 4D/Redshift/ZBrush source, binaries, licences or protected assets into Biupiu. Store adapter contracts, compatibility records, external references, provenance metadata and legally distributable scene specifications.

## Gate RENDER-02

**Executed:** Maxon Cinema 4D + Redshift integrated as first-class adapters and cross-linked with the existing professional rendering stack.

**Next gate:** controlled workstation test using common Biupiu geometry/material inputs and comparison across Cinema 4D/Redshift, Blender/Cycles, Octane, V-Ray and Unreal.

## External references

- https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples
- https://github.com/Maxon-Computer/Cinema-4D-Cpp-API-Examples
- https://github.com/Maxon-Computer/Cinema-4D-Visual-Studio-Code-Extension
- https://github.com/Maxon-Computer/Redshift-OSL-Shaders
- https://github.com/Maxon-Computer/Redshift-OCIO-Configs
- https://github.com/Maxon-Computer/ZBrush-Python-API-Examples
- https://developers.maxon.net/docs/py/
