# Biupiu Mechanic & Workshop Resource Registry v1.0

## Purpose
Curated open resources for building physically grounded Biupiu workshop simulators. Resources are references and integration candidates; code/assets are not copied unless their licenses permit reuse.

## GitHub candidates
- tetreum/carmechanic — open-source car disassembly/assembly simulator; useful for component hierarchy, vehicle parts, lift/workshop interaction patterns.
- valdavole/automation-diy — open-source engine builder, dyno and vehicle-dynamics simulator; useful for engine configuration, telemetry, failure models and deterministic test scenarios.
- soda-auto/soda-sim — Unreal Engine vehicle/robotics validation framework with atomic vehicle components, sensors, ECUs and validation scenarios; useful for the UE5 digital-twin/diagnostic layer.
- openads-project/carla-simulator — UE5.5 vehicle simulation backend; useful for vehicle physics, sensors, environments and closed-loop validation.
- OpenAutomotiveSimulator/OAS-Engine — open automotive simulator focused on high-fidelity vehicle dynamics in Unreal Engine; candidate research reference.
- Rigs of Rods — open-source soft-body vehicle simulator; useful as a reference for deformation, damage and vehicle construction physics.

## Open textbook / mechanics references
- AutomotiveTextbook.com — peer-reviewed free automotive technology text covering engine repair, transmissions, drivetrains, suspension/steering, brakes, electrical/electronic systems, HVAC, engine performance, diesel, hybrid/EV and maintenance.
- Concordia University OER Engineering guide — open engineering resources covering mechanics, structures, materials and aerospace-related fundamentals.

## Integration rule
Use these projects as architectural/algorithmic references first. Verify each repository's current license and dependency terms before redistributing source code, models, textures, sounds or datasets. Prefer clean-room implementation of interfaces and algorithms when licensing is unclear.

## Workshop learning model
Every simulator should model:
1. Inspection -> diagnosis -> work order.
2. Component identification and dependency graph.
3. Safe disassembly/assembly sequencing.
4. Tool selection and procedure constraints.
5. Measurement/telemetry.
6. Fault injection and failure diagnosis.
7. Repair/replacement and verification.
8. Maintenance record + digital-twin state update.
9. Test/validation gate.
10. Evidence/provenance record.

## Safety
No simulator result is treated as real-world maintenance authorization. Real-world maintenance remains governed by applicable manufacturer manuals, approved maintenance data, certification requirements and qualified personnel.
