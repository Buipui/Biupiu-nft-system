# Biupiu Unified Visualization Package v1.0

A single package specification coordinates multiple visualisation targets from one validated source model and asset-manifest set.

## Principle
One authoritative source model + validated asset manifests → renderer-specific packages. Renderer outputs remain derivative presentation artifacts.

## Targets
Lumion, Unreal Engine 5, V-Ray and Blender can be enabled independently. Each target has its own profile and output formats while sharing the same project/source-model identity.

## Determinism
Record units, coordinate system, real-world scale, camera set, environment set, source-model version and manifest versions before producing outputs.

## Promotion
Run the visual-asset validator before package generation. Production assets require verified licence status and provenance.

## Engineering boundary
This package coordinates visualisation only. CAD/CAE, CFD/FEA, measured material properties and physical validation remain authoritative for engineering decisions.