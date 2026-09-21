# Biupiu Multicore + Spatial Compute Federation Gate v1.0

Status: IMPLEMENTED / STATIC VERIFICATION PENDING / LIVE HARDWARE PENDING

## Scope
Unifies heterogeneous CPU, GPU, NPU and spatial/VR compute under capability-first
federation. Resources are discovered at runtime; core counts are never hard-coded.

## Implemented
- Capacity-aware CPU/GPU/NPU federation contract.
- Preferred/minimum workload requirements and fail-closed dispatch.
- Execution telemetry.
- Machine capability registry independent of vendor/device names.
- CAN/CAN-FD, LIN, Ethernet, SPI, I2C, GPIO and ADC transport identifiers.
- Desktop/mobile/VR endpoint architecture.
- Hardware-specific translation isolated behind adapter boundaries.

## Spatial/VR
A common simulation state can be rendered to desktop, mobile, AR or VR.
VR is an endpoint; authoritative state remains in the federated simulation layer.
Heavy simulation may remain on workstation/server compute.

## Safety
Capability abstraction does not remove hardware adapters. For safety-critical
machines: Biupiu abstraction -> verified adapter -> safety boundary -> device.
Experimental AI must not bypass a safety boundary.

## Open verification
Python tests, TypeScript tests, x86_64/ARM64/Apple discovery, GPU/NPU discovery,
contention/scaling, fault injection, VR timing/input, ECU/CAN-FD HIL and
Windows/macOS/Linux/Android regression remain hardware/runtime gates.
