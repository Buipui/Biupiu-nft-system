# Biupiu Multicore + Spatial Compute Federation Gate v1.0

Status: IMPLEMENTED IN BRANCH / STATIC TESTS PENDING EXECUTION / LIVE HARDWARE PENDING

## Scope
Unifies heterogeneous CPU, GPU, NPU and spatial/VR compute under capability-first
federation. The system must discover resources instead of assuming a fixed core count.

## Implemented
- Capacity-aware heterogeneous compute contract.
- CPU performance/efficiency/vector, GPU and NPU classes.
- Preferred/minimum workload requirements.
- Fail-closed dispatch when a required compute class is unavailable.
- Telemetry for execution success/failure.
- Machine capability registry independent of vendor/device names.
- Capability validation for range and readability.
- CAN/CAN-FD, LIN, Ethernet, SPI, I2C, GPIO and ADC transport identifiers.
- Architecture path for desktop, mobile and VR/spatial endpoints.
- Separation of machine abstraction from hardware-specific adapters.

## Spatial/VR extension
The same simulation state may be rendered to desktop, mobile, AR or VR.
VR is treated as an interaction/rendering endpoint, not as the authoritative
simulation state. Heavy simulation can remain on a workstation/server while
the headset receives controlled spatial frames and input.

## Safety boundary
Capability abstraction does not eliminate hardware adapters. For safety-critical
machines, the path remains:
Biupiu abstraction -> verified adapter -> safety boundary -> physical device.

ML, experimental algorithms and research workloads must not directly bypass a
safety boundary.

## Verification gates
1. Python syntax and unit tests.
2. TypeScript build/tests.
3. Native topology discovery on x86_64.
4. Native topology discovery on ARM64.
5. Apple Silicon discovery.
6. GPU discovery and compute/render separation.
7. NPU discovery where available.
8. Scaling and contention benchmarks.
9. Fault injection and recovery.
10. VR frame-timing and spatial-input integration.
11. ECU/CAN-FD hardware-in-the-loop testing.
12. Cross-platform regression on Windows/macOS/Linux/Android.

Until hardware-in-the-loop evidence exists, live hardware gates remain OPEN.
