# Biupiu World — 3D Gate 02: Shared Character Base v1.0

## Status
Specification committed for modelling implementation. This gate defines the shared avatar architecture; it does not claim that binary 3D meshes, rigs, or animation files have been generated.

## Objective
Create a reusable, permission-aware character foundation for Windows and Android, supporting cultural environments, research workshops, department specialists, robotic agents, and future creature/vehicle interfaces.

## Character base families
- HUMANOID-BASE: neutral bipedal skeleton for researchers, visitors, artisans, engineers, historians, and environment guides.
- QUADRUPED-BASE: modular quadruped rig for farming, conservation, wildlife, and ecological environments.
- ROBOTIC-BASE: articulated service/industrial robot rig for AI/Robotics, farming automation, metallurgy, materials, and logistics.
- CREATURE-REFERENCE-BASE: non-documentary fictional or educational creatures, clearly labelled by evidence state and provenance.

## Retargeting
- Consistent world scale, axes, origin, and documented rest pose.
- Humanoid minimum: root, pelvis, spine, neck/head, clavicles, arms/hands, legs/feet, with optional facial and hand-detail extensions.
- Canonical joint names and a stable retargeting map.
- Separate deformation and control/IK bones where supported.
- Quadruped and robotic rigs document their own joint maps and compatibility limits.

## Animation state library
Core: idle, walk, run, turn, crouch/inspect, stop/recover.
World interaction: portal enter/exit, object interaction, research inspection, collect/place, workstation use, gesture, wave/acknowledge, seated/stationary accessibility interaction.
Specialist extensions: farming sow/harvest/water/soil inspection; metallurgy forge/measure/material inspection/safety pause; textiles weave/spin/dye/fibre inspection; laboratory sample/scan/record; marine/mobility pilot/inspect/maintenance; archive/NFT display/authenticate/catalogue.
All clips are tagged with package, provenance/licence, target rig, duration, root-motion mode, and performance tier.

## Modular appearance
- Slots for body, head/hair, clothing, footwear, tools, accessories, badges, cultural items, and specialist equipment.
- Desktop and mobile material variants.
- Cultural assets must be source-based, licensed, public-domain, permissioned, or labelled creative interpretation.
- Do not present historical/speculative characters as documentary fact solely from visual design.
- Use swappable meshes and texture sets.

## Metadata
Each character records:
`character_id, package_id, base_family, rig_version, animation_set, department_id, environment_id, access_scope, source, creator, licence, provenance, evidence_state, poly_budget, texture_budget, lod_set, collision_profile, dependencies, status`.

## Access and dialogue
- Character appearance, dialogue, tools, and research actions inherit subscriber department permissions.
- AI dialogue cites approved research records for factual claims.
- New Age Theory characters distinguish documented history, reconstruction, hypothesis, folklore, and creative fiction.
- Restricted resources cannot be exposed through search, dialogue, exports, notifications, or interaction.
- Sensitive actions and evidence-state changes are auditable.

## Performance tiers
LOD0 showcase; LOD1 desktop exploration; LOD2 Android/mobile; LOD3 distant/crowd.
Use simplified collision, limited animation layers, texture atlases, and optional facial detail on mobile. Define per-scene budgets for active characters, skinned meshes, draw calls, texture memory, and animation evaluation before production.

## Package structure
```
CHAR-<id>/
  manifest.json
  models/
  rigs/
  animations/
  materials/
  textures/
  lod/
  colliders/
  audio/
  ui/
  docs/
  licence/
  provenance/
  tests/
```

## Acceptance checks
1. Humanoid base has a documented rest pose and retargeting map.
2. Core animation states are named, tagged, and mapped to interaction events.
3. Clothing/accessory slots work independently of the base body.
4. Desktop and Android LOD targets are specified.
5. Collision and navigation proxies are defined.
6. Department/environment permissions are inherited by character interactions.
7. Source, creator, licence, provenance, and evidence state are recorded for every non-original asset.
8. Historical and speculative visual material is labelled accurately.
9. AI dialogue cannot bypass resource or department restrictions.
10. A test scene validates portal entry/exit, object inspection, workstation use, and accessibility alternatives.

## Next gate
**Gate 03 — Department avatar variants and interaction-ready workshop characters**, beginning with Farming, Metallurgy, Textiles, and Materials.
