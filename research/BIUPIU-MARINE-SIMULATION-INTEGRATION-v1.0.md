# Biupiu Marine Simulation Integration v1.0

**Gate:** MARINE-SIM-01  
**Date:** 19 September 2026  
**Status:** ARCHITECTURE REGISTERED — external runtime validation pending

## Design direction

The marine division must use the current Biupiu design language:

- Stealth geometric marine forms
- Premium biotech × regenerative agriculture × advanced materials aesthetic
- Deep marine green, graphite, controlled metallic accents and restrained gold branding
- Photorealistic presentation where appropriate
- Full-craft framing with the Biupiu Bioblade microturbine system clearly visible
- No generic pirate, low-poly, toy-like or conventional yacht styling for Biupiu concept renders

The official Biupiu logo/wordmark remains the authoritative brand reference for renders and showreels.

## Simulation architecture

`Concept geometry → asset manifest → marine adapter → environment/water solver → vehicle dynamics → sensors/autonomy → telemetry → Digital Twin → validation record → showreel`

## Resource classes

### Marine physics and water

- SEA-Stack: marine/offshore dynamics and marine-energy research reference.
- Stonefish: underwater and marine robotics simulation reference.
- Godot realistic-environment/ocean systems: reusable ocean, sky, wind, buoyancy and boat-system reference.
- Godot Endless Waves: renderer-compatible Gerstner-wave and buoyancy reference; mobile/performance limitations require testing.

### Game and world modules

- Godot-based sailing and naval gameplay modules may be used as architectural references for camera systems, world routing, ship controls, ports, weather and interaction.
- Corsairs: procedural ship, sailing, world, port and scene-separation reference. Do not copy protected game assets.
- Kenney Watercraft Kit: CC0 asset reference for prototyping only; final Biupiu vessels must use original or properly licensed geometry.

### Visual and environment pipeline

- Blender/ glTF interchange for authoritative source geometry and material metadata.
- Bevy/Godot/Unreal adapters remain engine-specific presentation targets, not authoritative sources.
- Asset manifests must preserve provenance, licence, source identity, transform, material and version metadata.

## Proposed packages

- `MAR-01` — stealth geometric hydrofoil / research craft.
- `MAR-02` — stealth expedition and ocean-testing vessel.
- `MAR-03` — autonomous surface vessel and sensor test platform.
- `MAR-04` — underwater robotics / inspection platform.
- `MAR-ENV-01` — virtual boatyard, launch ramp, harbour and sea-testing area.
- `MAR-TEST-01` — calm water, swell, crosswind, storm, current and sensor-visibility scenarios.

## Integration boundaries

1. Third-party repositories remain references or external dependencies until licence and compatibility review is complete.
2. No proprietary or copyrighted game assets are represented as Biupiu-owned IP.
3. Visual similarity is not sufficient for engineering validation; buoyancy, stability, propulsion, structural and control models require measured or solver-backed evidence.
4. Runtime compilation, performance profiling, physics validation and cross-platform packaging remain separate execution gates.
5. Marine assets must not be promoted automatically into customer-facing Biupiu World releases.

## Render brief

All new concept renders should:

- Show the entire vessel in frame.
- Use a stealth-geometric hull with integrated advanced-material paneling.
- Make the Bioblade microturbine system visibly identifiable without overwhelming the craft.
- Use realistic ocean lighting, physically plausible wake and controlled atmospheric perspective.
- Apply the Biupiu gold-on-deep-green premium brand treatment sparingly.
- Include clean technical presentation variants: three-quarter exterior, side profile, top/plan view, boatyard workshop and sea-test scene.

## Acceptance criteria

- [ ] Resource and licence metadata recorded.
- [ ] Marine adapter interfaces defined.
- [ ] Source geometry and render geometry separated.
- [ ] Full-vessel render brief applied.
- [ ] Bioblade system visible in concept views.
- [ ] No integration claim until local or connected runtime tests produce evidence.

**MARINE-SIM-01:** Architecture and resource map registered. Runtime integration and validation are pending connected development environments.
