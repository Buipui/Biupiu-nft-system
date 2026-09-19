# Biupiu Visual System Architecture — vNext

Status: EXECUTED / ACTIVE
Date: 2026-09-19

## Purpose
Define the shared visual production architecture while UE5.8.2 is being installed and the repository is being cloned/forked for recovery.

## Architecture
Biupiu World is the canonical visual environment and shared asset authority.

1. World Layer
- Biupiu World: environments, lighting, weather, terrain, vegetation, atmosphere, materials and world-building assets.
- Shared asset IDs and provenance remain provider-neutral.

2. Digital Twin Layer
- Physical/product specifications
- CAD/mesh references
- materials and manufacturing metadata
- department ownership and dependency graph
- variant/configuration state

3. Visual Intelligence Layer
- scene composition
- asset selection
- lighting/weather presets
- camera and shot planning
- material/look profiles
- cross-department visual consistency

4. Render Broker
- provider-neutral render request
- capability validation
- provider selection
- bounded retries
- polling
- provenance
- failure classification

5. Provider Adapters
- Unreal Engine 5: primary real-time world/runtime target
- Adobe/Firefly: generative visual production
- Blender: procedural/modelling support
- Twinmotion: rapid visualization
- KeyShot: product/material visualization
- Premiere/After Effects: motion/showreel finishing

6. Department Streams
Departments consume the same Biupiu World foundation but retain independent research/package boundaries. Automotive, regenerative agriculture, advanced materials, textiles and other streams may contribute validated assets back to the shared registry without collapsing their repositories.

## UE5 transition
UE5.8.2 remains the heavyweight runtime gate. The architecture must not block on its installation: provider-neutral assets, contracts, registries, Firefly outputs and visual planning can continue independently.

## Safety / rollback
- Preserve cloned/forked snapshots before importing pre-release material.
- Treat prerelease branches as quarantined inputs until validated.
- Never overwrite canonical assets without provenance and version metadata.
- Keep generated visual assets traceable to their provider and generation request.

## Current gate state
- Architecture: GREEN
- Biupiu World registry: GREEN
- Render broker: GREEN
- Firefly live generation: GREEN
- UE5 runtime: AMBER (installation/build gate)
- Full end-to-end cinematic pipeline: AMBER (awaiting UE5 runtime)
