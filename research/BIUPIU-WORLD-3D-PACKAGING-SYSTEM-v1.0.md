# Biupiu World — 3D Packaging & Modelling System v1.0

## Objective
Reusable 3D asset pipeline across every Biupiu World department: environments, buildings, workshops, machinery, vehicles, characters, props, research objects and UI portals.

## Package architecture
WORLD CORE → MAIN HUB → DEPARTMENT PACKAGE → ENVIRONMENT PACKAGE → BUILDING/WORKSHOP → CHARACTER PACKAGE → PROP/MACHINE PACKAGE → RESEARCH OBJECT → INTERACTION/DATA LAYER

Each package has asset ID, version, provenance, licence and department-access policy.

## Department package matrix
- FARMING: farms, regenerative plots, irrigation, nurseries, smart-farming machinery
- METALLURGY: foundries, furnaces, forges, machining, testing labs
- TEXTILES: fibre fields, spinning, weaving, dyeing, textile workshops
- MATERIALS: composites, hemp materials, ceramics, advanced-material labs
- BIOTECH: plant labs, culture spaces, microscopy, controlled growing
- FOOD/AGRO: processing, kitchens, cold storage, packaging, QC
- PHOTONICS: optical benches, FSO/LiFi/VLC, structured-light labs
- ENERGY: storage, solar research, power electronics, experimental systems
- AI/ROBOTICS: AI lab, data centre, robotics, simulation, digital twins
- MARINE: hydrofoil showcase, boat workshop, marine materials, water testing
- MOBILITY: vehicle design, composites, simulation and test zones
- CONSERVATION: biodiversity labs, seed banks, habitat restoration
- CRYSTAL/GEOMETRY: mineral labs, crystal optics, computational geometry
- ANCIENT TECHNOLOGY: reconstruction and claim-testing labs
- NEW AGE THEORY: Atlantis, Mu, Hyperborea, Tartaria, Hollow Earth
- RESEARCH/ARCHIVE: library, GIS, evidence and provenance rooms
- NFT/DIGITAL: minting gallery and digital exhibition

## Asset classes
ENV, BLD, WRK, CHR, VEH, MAC, PRP, RES, UI, VFX, NAV

## Standard metadata
asset_id, package_id, department_id, environment_id, asset_class, version, source, creator, licence, provenance, evidence_state, poly_budget, texture_budget, lod_set, collision, animation_rig, dependencies, access_scope, status

## Performance
LOD0 showcase, LOD1 exploration, LOD2 mobile, LOD3 distant, collision mesh and optional mobile materials.

Targets: Windows desktop, Android/mobile, future web/streaming client.

## Mod-asset integration
Allocated mod assets are candidate implementation/reference assets, not automatically redistributable assets:
MOD ASSET → LICENCE/PERMISSION CHECK → PROVENANCE → COMPATIBILITY → OPTIMISE → PACKAGE → MANIFEST

Where redistribution is not permitted, create a Biupiu-original replacement and retain the mod as reference-only.

## Package tiers
WORLD-CORE; DEPT-*; LAB-*; CHAR-*; VEH-*; PROP-*; RESEARCH-*; SHOWCASE-*

## Build order
1. Main Hub
2. Department portals
3. Shared character system
4. Farming + Metallurgy + Textiles + Materials
5. Biotech + Food + Conservation
6. Photonics + Energy + AI/Robotics
7. Marine + Mobility
8. Crystal/Geometry + Ancient Technology
9. New Age Theory
10. Archive/NFT/Showcase
11. Cross-department campus
12. Android optimisation

## Quality gates
Provenance, licence, evidence-state, access control, scale, collision, LOD, materials, interaction, mobile performance and repository manifest.