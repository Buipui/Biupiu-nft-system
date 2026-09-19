# Biupiu Blender Android Architecture v1.0

## Role
Blender Android is the 3D engine layer for the Biupiu R&D OS. It provides modelling, materials, animation, rendering, simulation and visualization while Biupiu owns the higher-level project, Digital Twin, asset and research orchestration.

## Runtime layers
Biupiu Mobile Shell → Biupiu Core → Digital Twin Service → Blender Bridge → Blender Android Engine

The bridge exchanges stable Biupiu asset/digital-twin records rather than coupling the application to Blender internals.

## Biupiu packages
- biupiu-core
- biupiu-ai
- biupiu-digital-twin
- biupiu-materials
- biupiu-simulation
- biupiu-robotics
- biupiu-photonics
- biupiu-world
- biupiu-blender

## Domain adapters
- Microturbines / blades
- Biomaterials / plant composites
- Bio-adhesives, epoxy and resins
- Marine
- Automotive
- eVTOL / aerospace
- Robotics
- Photonics / optical systems
- Regenerative agriculture
- Biupiu World

## Deployment tiers
### Mobile Lite
Geometry, inspection, materials, lightweight animation and basic rendering.

### Mobile Full
High-end ARM64/Vulkan devices with Cycles and heavier libraries where supported.

### Remote
Android remains the control/inspection surface while heavy simulation or rendering runs on a workstation/cloud.

## Digital Twin contract
Every supported object should have a stable Biupiu ID and versioned metadata: geometry reference, dimensions, mass, materials, manufacturing metadata, simulation parameters, research references, evidence classification, version and asset hashes.

Blender scenes are views/representations of the Digital Twin rather than the canonical research record.

## Build strategy
Use the upstream Android build system rather than rewriting Blender's build system. Keep Biupiu integration in a bridge/add-on layer. Pin upstream commits and verify APK builds before updating.
