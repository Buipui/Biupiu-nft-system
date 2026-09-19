# Biupiu World — Private R&D Centre

Status: PRIVATE R&D / PERSONAL DIGITAL LAB
Customer access: NONE
Promotion to Biupiu World: MANUAL OWNER APPROVAL ONLY

This centre is for owner-only experimentation, physics validation, digital-twin development, system modelling, prototype software and speculative research before anything is promoted into the customer-facing Biupiu World environment.

SEPARATION RULE
PRIVATE R&D -> TEST -> VALIDATE -> REVIEW -> PROMOTE OR RETAIN PRIVATE

Nothing here is automatically published, packaged for customers, exposed through the Biupiu World runtime, or treated as production-ready.

SECURITY NOTE
This is a logical product/IP boundary, not a GitHub access-control boundary. If the repository is accessible to other people, confidential research must be moved to genuinely private storage before being stored here.

PHYSICS-FIRST DIGITAL SYSTEMS
- 6-DoF rigid-body dynamics
- aerodynamics and propulsion
- rotating machinery / turbine models
- vehicle dynamics
- marine dynamics
- robotics and actuator models
- thermal systems
- fluid/pressure networks
- structural/lumped compliance models
- electrical/power-system models
- material-property models
- sensor/actuator models
- environmental and terrain interaction
- coupled multi-domain digital twins

PROMOTION CLASSES
PRIVATE -> owner research only
EXPERIMENTAL -> test model with incomplete validation
VALIDATED -> repeatable model with documented test evidence
CANDIDATE -> suitable for owner review for Biupiu World
WORLD -> explicitly approved for customer-facing integration

A model must never move to WORLD merely because it exists or passes a software test.

CORE PATHS
- engine/ reusable physics and numerical primitives
- models/ machine-readable model definitions
- scenarios/ controlled test scenarios
- telemetry/ test outputs and validation records
- promotion/ owner approval and release gates
- docs/ architecture and operating rules

Current gate: PHYS-SYS-01. The physics engine becomes a reusable Biupiu World systems layer, with flight simulation treated as one application domain rather than the whole engine.
