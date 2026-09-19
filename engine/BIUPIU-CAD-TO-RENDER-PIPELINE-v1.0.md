# Biupiu CAD-to-Render Pipeline v1.0

## Objective

Create a controlled pipeline that preserves lower-level CAD geometry as the engineering source while generating high-fidelity render assets for Biupiu World, advertising, product films and immersive experiences.

## Asset Lineage

`CAD_SOURCE -> ARCHIVE -> CONVERT -> CLEAN -> VALIDATE -> MATERIALIZE -> OPTIMIZE -> LOD/COLLISION -> RENDER -> EXPORT`

## Required Records

- Asset ID and product ID.
- Original file format and source location.
- Units, scale and coordinate system.
- Assembly and part hierarchy.
- Revision, author and source date where available.
- Geometry validation result.
- Materials, textures and shader assignments.
- Derived mesh identifiers.
- LOD levels and triangle budgets.
- Collision and simulation status.
- Render profile and camera/capture settings.
- License, ownership and provenance status.

## Asset Separation

1. Engineering source: retained and never overwritten by optimization.
2. Master visualization asset: high-detail geometry and materials for close-up renders.
3. Runtime asset: optimized geometry for interactive use.
4. Simulation asset: collision, mass, material and physical parameters where validated.
5. Marketing asset: controlled camera, lighting, branding and output settings.

A runtime or marketing asset must not be treated as manufacturing-ready CAD. Manufacturing and engineering release require separate validation.

## Visual Quality Requirements

- Physically based materials.
- Correct scale and proportions.
- High-resolution texture and normal workflows.
- Controlled lighting and color management.
- Product-focused camera presets.
- Close-up detail tests for surfaces, seams, edges and interfaces.
- Clean background and environment variants for advertising.
- Cinematic sequence and still-image export profiles.

## Acceptance Tests

- Source geometry can be recovered.
- Unit and orientation checks pass.
- No unintended geometry loss during conversion.
- Materials and texture references resolve.
- Render asset opens in the target toolchain.
- LOD and collision status is recorded.
- Provenance and license fields are complete.
- Sample still and video capture passes visual review.
