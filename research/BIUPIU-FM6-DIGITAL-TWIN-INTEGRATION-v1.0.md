# Biupiu FM6 Digital Twin Integration v1.0

**Gate:** FM6-03  
**Status:** EXECUTED — contract layer

## Objective
Connect the FM6-derived presentation preset layer to Biupiu's authoritative Universal Asset Manifest and Digital Twin lineage without importing proprietary Forza content.

## Contract
SOURCE ASSET → UNIVERSAL MANIFEST → DIGITAL TWIN BINDING → FM6 REFERENCE PRESET → PROVIDER PACKAGE → RENDER OUTPUT

The binding carries:
- source asset identity and model version;
- Digital Twin ID;
- department classification;
- licence and IP state;
- provider targets;
- explicit FM6 reference-only state.

## Safety and provenance controls
- Restricted assets are blocked from renderer packaging.
- The FM6 layer cannot become an asset source.
- Presentation presets do not modify authoritative geometry or engineering allowables.
- Provider derivatives remain downstream of the authoritative asset.
- Live provider conversion remains environment-gated.

## Department mapping
Automotive: vehicle design/showcase.
Aerospace: eVTOL, UAV, helicopter, jet and drone visualisation.
World: road, environment and virtual-hangar presentation.

## Acceptance
The TypeScript validation contract must pass for a cleared internal asset and reject restricted or incomplete bindings.
