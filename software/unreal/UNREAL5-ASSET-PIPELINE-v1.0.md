# Biupiu Unreal Engine 5 Asset Pipeline v1.0

## Asset classes

- Automotive and mobility concepts
- Marine vessels and systems
- eVTOL and helicopter concepts
- Microturbines and propulsion studies
- Advanced-material/composite concepts
- Regenerative-farming digital twins
- Architectural and environmental scenes
- Computational-art and NFT presentation assets

## Project folders

- /Game/Biupiu/Assets/Geometry
- /Game/Biupiu/Assets/Materials
- /Game/Biupiu/Assets/Textures
- /Game/Biupiu/Assets/Animation
- /Game/Biupiu/Assets/VFX
- /Game/Biupiu/Assets/Blueprints
- /Game/Biupiu/Assets/Environments
- /Game/Biupiu/Assets/Showreel
- /Game/Biupiu/Tests

## Geometry validation

Before import: apply intended transforms, check scale and coordinates, verify normals and smoothing, remove accidental duplicate geometry, confirm UVs where required, and separate collision geometry where appropriate.

## Provenance

Recommended chain: Research ID -> asset ID -> source application -> source revision/commit -> export format -> UE asset path -> project revision -> licence/IP status.

For NFT computational art also preserve algorithm family/version, parameters, seed and hashes under the existing Biupiu provenance architecture.

## Visual validation

1. Silhouette and geometry
2. Materials and textures
3. Lighting and exposure
4. LOD/performance
5. Collision/physics where applicable
6. Real-time render
7. Movie Render Queue/showreel output where applicable

## Cross-tool responsibility

Blender: modelling, geometry and simulation.
Cinema 4D: procedural modelling and computational scene authoring.
KeyShot: product/material visualization.
Redshift: GPU production rendering.
Twinmotion: rapid environment and walkthrough production.
Unreal Engine 5: real-time interactive visualization, digital twins, asset presentation and interactive showreels.
Visual Studio: UE C++ development, debugging, tests and integration tooling.
