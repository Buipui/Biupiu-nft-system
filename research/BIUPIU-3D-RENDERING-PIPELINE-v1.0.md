# Biupiu 3D Rendering Pipeline v1.0

**Updated:** 18 September 2026

## Objective

Create a renderer-agnostic Biupiu 3D pipeline capable of moving canonical assets between modelling, simulation, look-development and professional rendering systems.

## Core principle

**Canonical asset first; renderer second.**

Geometry, scene structure, metadata, materials and provenance should remain portable wherever practical. Renderer-specific files are treated as downstream representations.

## Master scene strategy

1. Create/model the canonical asset.
2. Assign stable Biupiu asset ID.
3. Preserve units, transforms, hierarchy and material IDs.
4. Export/import through OpenUSD where appropriate.
5. Apply renderer-specific materials, lighting and camera settings.
6. Render diagnostic passes/AOVs.
7. Validate visual and technical output.
8. Record software/version/commit and source asset.
9. Store final render and provenance record.

## Arnold track

Primary upstream:
- Autodesk/arnold-usd
- Autodesk/standard-surface

Reference:
- LumaPictures/usd-arnold
- Autodesk/sitoa

Candidate extensions:
- MtoA tooling
- Blender/Arnold integrations
- OSL shader repositories

## Integration with existing Biupiu rendering research

This pipeline is designed to sit alongside:
- KeyShot resources
- V-Ray resources
- Lumion resources
- Maxon/Cinema 4D resources
- Runway/video resources
- other approved professional visualization tools

The goal is interoperability rather than locking Biupiu assets to a single renderer.

## Asset classes

- Vehicles
- Marine concepts
- Aircraft/eVTOL concepts
- Microturbines
- Machinery and robotics
- Smart-farming infrastructure
- Buildings and eco-estates
- Biupiu World environments
- Characters
- Textiles
- composites/material samples
- product packaging
- scientific/engineering visualization
- computational-art objects

## Material library direction

Develop a shared material taxonomy covering:
- metals
- glass
- ceramics
- polymers
- carbon/hemp composites
- natural fibres/textiles
- wood
- stone
- soil
- vegetation
- water
- coatings/paint
- translucent biological materials
- photovoltaic/photonic surfaces

Use Autodesk Standard Surface as one important reference, while keeping the material catalogue concept renderer-neutral.

## Quality gates

### Gate R1 — Asset integrity
Geometry, scale, normals, transforms and naming validated.

### Gate R2 — Material integrity
Material IDs and physical parameters recorded.

### Gate R3 — USD/interchange validation
Scene survives round-trip/interchange tests where supported.

### Gate R4 — Renderer validation
Arnold and other selected renderers produce expected geometry/material results.

### Gate R5 — Provenance
Software versions, repository references, source commit/tag and licences recorded.

### Gate R6 — Release
Only validated assets enter showcase, Biupiu World, NFT artwork or public-release packages.

## Current status

Architecture registered. Arnold resources are integrated as research dependencies/references; no third-party source has been copied into the repository.
