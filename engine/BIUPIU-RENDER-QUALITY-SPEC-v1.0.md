# Biupiu Render Quality Specification v1.0

## Mission
Prioritize immersive visual quality and commercial product visualization for Biupiu World, advertising and cinematic video.

## Render tiers
- R0 Preview: fast iteration.
- R1 Real-time: interactive world production.
- R2 Cinematic: high-quality marketing/video capture.
- R3 Reference: offline/high-quality stills where the renderer supports it.

## Core visual systems
- Physically based materials
- HDR lighting and exposure
- Tone mapping and color management
- High-resolution textures with controlled memory budgets
- Normal/roughness/metalness/height workflows
- Real-time shadows
- Reflection/environment capture
- Volumetric atmosphere
- Water and weather
- Foliage/vegetation
- Particles
- Animation and deformation
- Post-processing
- Cinematic camera
- Deterministic render capture

## Product advertising requirements
Every commercial product scene should support:
- hero camera
- detail/macro camera
- turntable
- exploded-view presentation when supplied by the product pipeline
- material/finish variants
- lighting presets
- clean studio background
- immersive environmental placement
- video frame sequence export
- still-image export

## CAD relationship
CAD is the lower-level geometric foundation. Visual assets are derived representations. The system records source-to-derived lineage, revision, units and provenance.

## Quality separation
Engineering accuracy, visual realism and game-runtime optimization are separate properties. A high-detail render does not by itself certify manufacturing geometry or engineering performance.

## Performance
Each asset records:
- triangle/vertex budget
- texture memory
- shader/material complexity
- LOD availability
- collision availability
- target render tier
- target platform

## Acceptance
The first graphics demonstrator must prove a repeatable path from an approved asset record to an immersive rendered scene and captured marketing output.
