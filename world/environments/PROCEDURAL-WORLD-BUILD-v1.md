# Biupiu World Procedural Environment Build v1

This phase converts civilisation environment manifests into an implementation-ready 3D sandbox architecture.

## Recommended runtime
Babylon.js is the reference runtime for the first web/mobile/desktop prototype because it supports scene graphs, procedural geometry, animation, physics, WebXR, glTF and native targets. The implementation remains engine-adapter based.

## Build layers
1. World loader
2. Terrain generator
3. Civilisation model generator
4. Water/farming generator
5. Library object generator
6. Avatar controller
7. Interaction system
8. Evidence/UI layer
9. Simulation event bridge
10. Save/provenance layer

## Avatar flow
Login -> Avatar Profile -> World Select -> Evidence Card -> Spawn Gate -> Orientation -> Explore -> Interact -> Simulate -> Save

## Performance
Use streamed zones and level-of-detail. Desktop/VR may load high-detail architecture; mobile receives simplified geometry.

Repository manifests describe intended assets. They do not claim meshes/textures are already created or deployed.
