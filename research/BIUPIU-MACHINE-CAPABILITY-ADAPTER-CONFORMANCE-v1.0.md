# Biupiu Machine Capability Adapter Conformance v1.0

**Gate:** Adapter conformance and deterministic simulation  
**Status:** Repository implementation executed; live protocol/HIL remains pending.

## Purpose
Exercise the canonical Machine Capability contract without connecting to physical hardware. The simulator must preserve the same capability identity, units, quality state, Digital Twin reference, provenance and permission boundary used by a real adapter.

## Required behaviours
1. Discover/load a capability document.
2. Validate it against the canonical schema.
3. Normalise telemetry into a deterministic envelope.
4. Reject invalid values and unknown capability fields.
5. Preserve units and quality state.
6. Preserve Digital Twin and provenance identifiers.
7. Never convert simulated state into observed physical state.
8. Deny actuation when the capability is READ_ONLY.
9. Emit deterministic results for identical input.

## Protocol boundary
The test adapter is transport-neutral. OPC UA, MQTT, Modbus, ROS/ROS 2, CAN/CAN-FD and vendor adapters must implement the same contract before promotion.

## Promotion boundary
Simulation conformance is not hardware-in-loop, safety approval or production certification.
