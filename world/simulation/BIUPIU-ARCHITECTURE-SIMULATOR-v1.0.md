# Biupiu Architecture Simulator v1.0

Status: INTEGRATED — architecture/data layer
Date: 2026-09-21

## Purpose
A digital architect simulator for Biupiu World. It combines parametric building design, GIS terrain, LiDAR/point clouds, procedural world generation, shared 3D assets, architectural rules, simulation, provenance and federation.

## Core boundary
INPUTS -> GIS/LiDAR -> WORLD MATRIX -> SITE ANALYSIS -> PARAMETRIC ARCHITECTURE -> ASSET RESOLUTION -> CONSTRUCTION/SYSTEM SIMULATION -> VISUALIZATION -> VALIDATION -> PROVENANCE

Simulation state is authoritative and remains separate from the renderer. GLB/glTF 2.0 is the preferred runtime interchange format; upstream DCC formats remain permitted.

## Modules
1. Site + GIS: CRS, terrain, roads, parcels, zoning, hydrology, vegetation.
2. LiDAR/photogrammetry: LAZ/LAS/GeoTIFF/mesh/point-cloud ingestion and decimation.
3. World-building matrix: biome, climate, culture, infrastructure, land-use, historical period and architectural grammar.
4. Architect: footprints, levels, grids, structural bays, circulation, daylight, orientation, passive systems.
5. Procedural city/world: roads, parcels, blocks, buildings, vegetation and infrastructure.
6. Asset federation: rights-aware discovery, metadata, dependency resolution, hashing and source tracking.
7. Country packs: country/region-specific architectural vocabulary, materials, vegetation, roads, signage and GIS adapters.
8. Simulation: solar/daylight, wind exposure, water, energy, occupancy, access, construction sequencing and basic structural constraints.
9. Unreal/Blender bridge: export/import adapters and digital-twin metadata.
10. QA/trust: licence gate, provenance, geometry validation, unit/CRS validation, performance budgets and regression tests.

## Existing Biupiu integration
- world/BIUPIU-WORLD-ASSET-PIPELINE-v1.0.md
- world/BIUPIU-WORLD-OPEN-SOURCE-INTEGRATION-REGISTRY-v1.0.md
- world/BIUPIU-WORLD-SHARED-ASSET-CONTRACT-v1.json
- world/simulation/BIUPIU-CIVILISATION-FARMING-ENGINE-v1.py
- world/simulation/BIUPIU-HISTORICAL-EVIDENCE-METADATA-SCHEMA-v1.json
- research/twinmotion-github-index-v1.md
- research/simulators/
- research/visual-assets/
- tools/blender-windows/
- tools/blender-android/

## External research adapters
- Poly Haven CC0 asset library.
- Adobe Substance 3D/community assets: use only within Adobe licence scope; never redistribute standalone source assets.
- OpenAI Shap-E: candidate text/image-to-3D generation module; MIT-licensed repository.
- WorldGrow: research/reference for hierarchical infinite 3D world generation.
- WorldGen: Apache-2.0 research/code reference for text/image-to-scene generation.
- OpenAssetImporter/Assimp: multi-format import boundary.
- UE GIS adapters such as UE-GeoViewer/UnrealGIS: reference/integration candidates subject to their licences.
- OpenStreetMap/GIS and public-domain/open government elevation datasets where licence permits.

## Runtime rule
No external asset becomes a distributable Biupiu asset merely because it is downloadable. Each item receives:
GREEN = rights verified for intended use
BLUE = open/free but scope requires review
YELLOW = permission/licence required
ORANGE = chain-of-title investigation
RED = prohibited/not approved
GREY = reference/research only

## Architecture workflow
SITE -> TERRAIN -> PARCEL -> PROGRAM -> MASSING -> STRUCTURE -> ENVELOPE -> MATERIAL -> SERVICES -> LANDSCAPE -> SIMULATE -> OPTIMIZE -> VALIDATE -> EXPORT

## Immediate simulator capabilities
- Generate a site from coordinates or imported GIS.
- Fit terrain and parcels.
- Generate architectural massing from parameters.
- Populate scenes from a rights-aware asset manifest.
- Apply country/biome packs.
- Preserve source, licence, hash, CRS, units and generation seed.
- Export engine-neutral scene manifests for Unreal/Blender/other renderers.

## Not falsely claimed complete
Actual Unreal/Android runtime compilation, large-scale LiDAR ingestion, physics accuracy, and commercial asset licensing are runtime/asset-specific gates and remain OPEN until executed and verified in the target environment.
