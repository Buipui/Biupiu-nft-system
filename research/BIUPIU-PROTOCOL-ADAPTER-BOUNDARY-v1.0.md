# Biupiu Protocol Adapter Boundary v1.0

**Gate:** Protocol adapter conformance  
**Status:** Repository-side boundary implemented; physical protocol execution pending.

## Canonical boundary

All transport implementations must expose the same capability-facing operations:

- connect / disconnect
- capability discovery
- telemetry/state read
- command submission
- connection/error state
- simulated vs observed state
- capability identity preservation

## Protocol families

The boundary is designed to host adapters for:

1. OPC UA
2. MQTT
3. Modbus
4. ROS / ROS 2
5. CAN / CAN-FD
6. Ethernet/IP
7. serial / GPIO
8. vendor-specific adapters

The protocol is an implementation detail beneath the canonical Machine Capability contract.

## Safety boundary

A READ_ONLY capability cannot receive actuation commands. Controlled and ACTUATION permissions require later authorisation, security, safety and hardware-in-loop gates.

## Evidence rule

The in-memory adapter is a conformance test double only. It is **not** evidence that any physical OPC UA, MQTT, Modbus, ROS, CAN or vendor device has been connected.
