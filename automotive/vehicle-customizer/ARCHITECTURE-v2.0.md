# Biupiu Vehicle Customizer Architecture v2.0

## Design basis
The architecture takes the strongest ideas visible in NFSU2 Unlimiter—data-driven part categories, configurable part availability, custom attributes, independent front/rear wheel handling, paint groups, custom costs/ratings, camera configuration, and separation of visual/performance parts—and modernises them for a Biupiu Digital Twin. NFSU2 Unlimiter documents these capabilities publicly. No NFS assets are copied.

## Modern stack
- Canonical vehicle state: JSON Schema + versioned manifests.
- Runtime configurator: web/TypeScript prototype -> Unreal Engine implementation.
- Asset authoring: Blender procedural/modular pipeline.
- Simulation adapter: vehicle dynamics, aero, thermal and manufacturing models.
- Digital Twin: immutable revisions, validation gates and provenance.
- R&D exchange: glTF/GLB where practical; engine-native assets remain derived build artifacts.

## New divisions
### AUTO-01 Vehicle Architecture & Digital Twin
Platform geometry, coordinate systems, packaging, interfaces and configuration management.

### AUTO-02 Exterior & Computational Bodywork
Body panels, aero, widebody, computational geometry, lighting and surface design.

### AUTO-03 Advanced Materials & Composites
Hemp composites, bio-resins, carbon alternatives, sandwich structures and material testing.

### AUTO-04 Powertrain & Energy Systems
ICE/EV/hybrid concepts, microturbine range-extender studies, thermal systems, energy storage and controls.

### AUTO-05 Chassis, Suspension & Braking
Mass distribution, suspension kinematics, brakes, tyres, steering and structural interfaces.

### AUTO-06 Aerodynamics & CFD
Wings, diffusers, ducts, underbody, drag/downforce studies and CFD/flow simulation.

### AUTO-07 Electronics, Sensors & Controls
ECUs, sensor packages, telemetry, embedded systems, robotics interfaces and vehicle networks.

### AUTO-08 Robotics & Manufacturing
Assembly cells, tooling, inspection, digital fabrication, tolerances and manufacturing sequence.

### AUTO-09 Interior, HMI & Human Factors
Cabin, seating, controls, displays, lighting and workshop UX.

### AUTO-10 Validation, Safety & Test
Geometry, collision, fatigue, thermal, electrical, aero and simulation validation.

## Cross-department Digital Twin links
Agriculture/materials -> regenerative fibres and bio-composites.
Biochemical research -> bio-resins, fuels and coatings.
Energy systems -> storage and powertrain.
AI/computation -> optimisation and simulation.
Photonics -> sensors, optical communications and LiDAR concepts.
Aerospace -> lightweight structures, composites, aero and digital-twin methods.
Robotics -> manufacturing and inspection.
Conservation/biological research -> materials and regenerative sourcing where appropriate.

Every cross-link is a research dependency, not an automatic transfer of commercial IP.

## Safety
External code/assets enter through: licence check -> dependency/security review -> isolated prototype -> automated tests -> Digital Twin validation -> human approval -> integration.
