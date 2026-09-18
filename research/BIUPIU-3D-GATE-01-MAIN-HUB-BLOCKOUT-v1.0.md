# Biupiu World — 3D Gate 01: Main Hub Blockout v1.0

## Gate objective
Create the first greybox/blockout specification for the shared Biupiu World 3D foundation before detailed modelling.

## Scene hierarchy
WORLD_ROOT
- MAIN_HUB
  - Arrival Plaza
  - World Map / Navigation Core
  - Department Gateway Ring
  - New Age Theory Gateway
  - Research Archive Portal
  - Character Spawn / Identity Zone
  - Asset Preview Gallery
  - Accessibility / Settings Zone

## Shared modelling standards
- Coordinate system and scale must be fixed before production assets are imported.
- Use modular wall, floor, doorway, stair, portal and lighting kits.
- Every scene receives a collision proxy and four LOD targets.
- Keep source meshes, optimised meshes and runtime exports separate.
- Use placeholder geometry first; do not spend production time on detail before navigation and scale are validated.

## First blockout packages
- BPU-3D-CORE-PLAZA
- BPU-3D-CORE-MAP-PORTAL
- BPU-3D-CORE-DEPARTMENT-RING
- BPU-3D-CORE-NEW-AGE-GATEWAY
- BPU-3D-CORE-CHARACTER-SPAWN
- BPU-3D-CORE-ASSET-GALLERY

## Department gateway slots
FARMING, METALLURGY, TEXTILES, MATERIALS, BIOTECH, FOOD, PHOTONICS, ENERGY, AI/ROBOTICS, MARINE, MOBILITY, CONSERVATION, CRYSTAL/GEOMETRY, ANCIENT TECHNOLOGY, NEW AGE THEORY, RESEARCH/ARCHIVE and NFT/DIGITAL.

## Acceptance checks
1. Player can enter and exit every gateway.
2. Department permissions are enforced at portal and resource level.
3. New Age Theory is visibly separate from documented historical environments.
4. Character spawn and interaction anchors are standardised.
5. Blockout runs with placeholder assets before mod assets are integrated.
6. Mod assets require provenance and licence records before runtime packaging.
7. Windows and Android scene budgets are recorded in the manifest.

## Next gate
Gate 02: shared character base, retargeting skeleton, animation states and mobile-ready avatar package.