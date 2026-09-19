# Biupiu Vehicle Customizer Specification v1.0

## Goal
A modular vehicle configuration tool for the Biupiu Digital Workshop and Virtual Garage.

## Slot system
BODY_FRONT, BODY_REAR, SIDE_SKIRT, FENDER_FRONT, QUARTER_REAR, HOOD, ROOF, ROOF_SCOOP, SPOILER, MIRROR, HEADLIGHT, TAILLIGHT, EXHAUST, WHEEL_FRONT, WHEEL_REAR, BRAKE, WIDEBODY, CARBON_PANEL, ATTACHMENT, INTERIOR, TRUNK, GLASS, DECAL, VINYL, NEON.

## Performance modules
ENGINE, ECU, TRANSMISSION, FINAL_DRIVE, SUSPENSION, TYRE, BRAKE, WEIGHT, TURBO, SUPERCHARGER, NITROUS, AERO.

## Digital Twin rules
- Every slot has a unique PartID.
- Parts declare compatibility tags.
- Materials are parameterised rather than hard-coded.
- Visual and simulation changes are linked but independently reversible.
- Each build stores revision, author, timestamp, licence and validation status.
- Unreal and Blender importers consume the same JSON schema.
- No proprietary NFS asset is required.

## Workshop functions
Select vehicle -> inspect twin -> choose part -> preview -> validate compatibility -> apply -> recalculate mass/aero/performance -> save revision -> export Unreal/Blender/web package.

## Validation gates
Geometry, attachment points, wheel clearance, collision, material slots, mass properties, suspension travel, tyre clearance, aerodynamic sanity, licence/provenance.

## R&D extensions
Parametric body panels, Biupiu hemp composites, regenerative-material options, computational geometry bodywork, CFD hooks, manufacturing constraints, robotics/assembly metadata and digital-fabrication exports.
