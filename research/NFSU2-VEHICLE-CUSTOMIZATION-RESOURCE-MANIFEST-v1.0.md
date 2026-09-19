# NFSU2 Vehicle Customization Resource Manifest v1.0

This record extracts design patterns and technical architecture, not copyrighted NFS game assets, for the Biupiu Automotive digital workshop.

## Sources reviewed
- GitHub NFSU2 Unlimiter: expanded body-shop categories, custom rims, paint channels, vinyl layers, attachments and aero/performance hooks.
- GitHub NFSTools/GlobalLib and nfs-toolbox: Global structures including CarParts, CarSkins, Materials, FNG, TPK and preset systems.
- GitHub PryHUB: NFSU2 parser/inspector with geometry, textures, validation, discovery and glTF export concepts.
- GitHub NFSU2Forge: chassis, engine, torque curve, gearbox, grip, steering, suspension and braking parameters.
- GitHub nfsu2-gizmo: parsed assets to meshes/materials/vehicle-controller pipeline.
- Nexus Mods and ModDB: current vehicle examples and visual-upgrade/modular replacement ecosystem.

## Isolated customization model
Exterior: front/rear bumper, side skirts, fenders, quarter panels, hood, roof, roof scoop, spoiler, mirrors, headlights, taillights, exhaust, wheels/rims, brakes, wide-body, carbon-fibre panels and modular attachments.

Appearance: base paint, part paint, rim/brake/engine/exhaust/trunk accents, vinyl layers, decals, lighting/neon and glass/decal zones.

Interior/specialty: cabin, trunk/audio layout, doors, dashboard/interior modules and specialty equipment.

Performance: engine, ECU, transmission, suspension/chassis, nitrous, tyres, brakes, weight reduction, turbo/supercharger and aerodynamics.

Simulation metadata: mass, centre of gravity, torque curve, RPM limits, gear ratios, grip, steering lock, spring/damping and brake force.

## Biupiu implementation rule
Use these as abstract capability categories. Do not copy EA/NFS meshes, textures, names, branding or proprietary game files into Biupiu. User-supplied/licensed assets require a rights/licence gate.

## Digital Twin mapping
VehicleTwinID -> BaseVehicle -> PartSlots -> Materials -> Appearance -> Aero -> Powertrain -> Chassis -> Simulation -> Validation -> Revision.

Every change is reversible and records asset provenance/licence.

## Target engines
1. Unreal Engine 5 primary interactive workshop target.
2. Blender asset preparation/procedural modelling.
3. Local web configurator for lightweight preview/control.

## Status
Research patterns isolated and converted into a Biupiu-native specification. External projects remain references; no external game assets are included.
