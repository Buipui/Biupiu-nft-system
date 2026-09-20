# Biupiu XR / VR / AR / MR Architecture v1.0

**Gate:** XR-01  
**Status:** INTEGRATED at contract/index level; device/runtime validation remains open

Runtime: OS -> Digital Twin -> Simulation State -> XR Adapter -> OpenXR Runtime -> Device.

OpenXR is the preferred common XR boundary. XR entities retain stable twin identity, transforms, units, spatial anchors where supported, interaction affordances, quality tier, provenance and simulated/observed state.

VR: Biupiu World, engineering inspection, factory walkthroughs, vehicle/aircraft/marine exploration, farming simulation, training and maintenance.

AR/MR: equipment identification, component overlays, telemetry, Digital Twin comparison, farm/site visualisation and controlled operator interfaces.

Physical actuation remains behind existing policy, authority and safety gates.

XR quality budgets cover frame rate, latency, geometry, texture memory, shader complexity, simulation tick, bandwidth and thermal/power envelope.

Next gates: XR-02 OpenXR device conformance; XR-03 spatial anchors; XR-04 hand/eye/controller interaction; XR-05 cross-engine XR replay; XR-06 physical-site Digital Twin overlay validation.
