# Biupiu Redshift Rendering Resources — v1.0

**Status:** INTEGRATED — GitHub resource index / renderer architecture layer
**Date:** 18 September 2026

## Purpose

Track Redshift resources that can strengthen the Biupiu professional-rendering and digital-twin pipeline without redistributing proprietary Redshift software, binaries or SDKs.

## Core GitHub resources

### 1. Official Maxon Redshift OSL Shaders
Repository: `Maxon-Computer/Redshift-OSL-Shaders`
URL: https://github.com/Maxon-Computer/Redshift-OSL-Shaders

Priority: CORE / OFFICIAL

Use cases:
- procedural and physically based shader development
- thin-film interference and iridescent material studies
- diffraction and optical visualisation
- procedural textures and surface effects
- advanced material experiments for Biupiu composites, coatings and concept surfaces

### 2. Redshift OCIO configurations
Repository: `Maxon-Computer/Redshift-OCIO-Configs`
URL: https://github.com/Maxon-Computer/Redshift-OCIO-Configs

Priority: CORE / OFFICIAL

Use cases:
- colour-management consistency
- render-to-post-production pipeline consistency
- reproducible colour transforms across professional visualisation stages

### 3. Cinema 4D renderer abstraction
Repository: `DunHouGo/renderEngine`
URL: https://github.com/DunHouGo/renderEngine

Priority: REFERENCE / AUTOMATION

Use cases:
- renderer abstraction
- Cinema 4D pipeline automation
- cross-renderer orchestration concepts

### 4. Custom Redshift API examples
Repository: `DunHouGo/Custom_Redshift_API`
URL: https://github.com/DunHouGo/Custom_Redshift_API

Priority: REFERENCE / AUTOMATION

Use cases:
- Redshift node automation
- material construction
- procedural scene setup
- Cinema 4D Redshift scripting patterns

### 5. Redshift material builder
Repository: `abrasic/redshift-material-builder`
URL: https://github.com/abrasic/redshift-material-builder

Priority: LEGACY REFERENCE

Status: Archived. Use for implementation ideas only; do not make it a production dependency.

### 6. Houdini + Redshift references

Repositories:
- `yanzezhu/houdini_redshift_basic`
- `noelvenus24/houdini_auto_redshift_material`

Priority: REFERENCE

Use cases:
- procedural Houdini → Redshift material workflows
- automated material generation
- procedural engineering visualisation

## Biupiu integration map

Redshift is registered as a renderer adapter rather than a replacement for the existing provider-neutral architecture.

Target flows:
- PRODUCT_STILL
- DIGITAL_TWIN
- CINEMATIC_SHOWREEL
- CONCEPT_VARIATION
- RESEARCH_VISUALIZATION

Primary Biupiu applications:
- automotive / marine / aerospace concept visualisation
- microturbine and blade visualisation
- advanced bio-composite material appearance studies
- photonics and optical-material visualisation
- engineering showcase renders
- research visualisation

## Evidence and licensing rule

GitHub resources are research/reference inputs. Proprietary Redshift software, binaries, SDKs and licensed assets must not be copied into the Biupiu repository. Resource links, documented interfaces and original Biupiu integration code may be indexed subject to each repository's licence.

## Next validation gate

Validate Redshift adapter contracts against an installed Redshift-capable workstation/environment before claiming live rendering, material compilation or production render execution.
