# Biupiu Global Hardware + OEM Harvest Register — September 2026

## Scope
Cross-reference the existing Biupiu capability/runtime architecture against current public hardware, embedded, robotics and OEM integration patterns.

## Existing Biupiu modules identified
- RuntimeSession / BiupiuRuntime
- DepartmentRuntime / DepartmentLauncher
- CapabilityRegistry / CapabilityRouter
- SharedContracts / BiupiuPlatformAdapter / BiupiuTransport
- Digital Twin boundary
- Instrumentation / Automation / Robotics / AI architecture
- C/C++/Rust core boundary
- Android CI/build gate
- Cross-platform target matrix

## Harvested implementation patterns

### Android / OEM
Android remains the common application baseline. OEM-specific enterprise/device APIs are isolated behind profiles and adapters rather than becoming core dependencies. Android enterprise documentation explicitly recognises OEMConfig/custom manufacturer APIs, while requiring them to comply with Android requirements. citeturn0search0turn0search1

### Cross-platform
Kotlin Multiplatform is suitable for extracting shared business/data logic while retaining native platform APIs. Compose Multiplatform can provide shared UI where appropriate; native escape hatches remain available. citeturn0search2turn0search3

### Embedded / hardware
Zephyr demonstrates vendor-neutral Bluetooth and USB subsystems and supports device-driver abstraction across embedded targets. Its current documentation also covers CAN, sensors, serial and related driver families. citeturn1search1turn1search2turn1search5

### Robotics
ROS 2 hardware interfaces provide a useful lifecycle model for sensor/system/actuator adapters: configure, activate, read, write, deactivate, error and shutdown. Biupiu should adopt the lifecycle concept at the contract level without copying ROS implementation code. citeturn1search13turn1search15

### Automotive / distributed systems
Eclipse uProtocol provides a relevant multi-language, multi-transport service abstraction for vehicle/cloud/mobile environments and explicitly bridges different transports rather than declaring one universal transport. This aligns with Biupiu's capability-first design. citeturn1search0

## Foreign-language/global harvesting rule
Research sources may be discovered in English, German, Italian, French, Spanish, Portuguese, Chinese, Japanese, Korean and Russian. Language is a discovery axis, not a trust signal. Official specifications, source releases, licences and test evidence outrank language or popularity.

## Hardware priority matrix
P0:
- USB
- BLE
- Wi-Fi/Ethernet
- sensors
- camera
- NFC
- serial
- CAN/CAN-FD

P1:
- GPIO
- I2C
- SPI
- OPC UA
- MQTT
- Modbus
- ROS 2

P2:
- vendor-specific enterprise/device APIs
- specialised industrial buses
- platform-specific acceleration/graphics

## OEM rule
OEM stores are a distribution layer. OEM-specific APIs are optional adapters. Core capabilities must remain portable.

## Safety rule
Read/observe paths may be broadly exposed after validation. Actuation paths remain fail-closed and require explicit authority, simulation/validation where applicable, and hardware-in-loop testing.

## Promotion rule
DISCOVER -> SOURCE/LICENCE -> SECURITY -> CAPABILITY CONFORMANCE -> TEST -> SIMULATION -> HARDWARE-IN-LOOP -> SAFETY -> PROVENANCE -> PROMOTE

No harvested repository is copied directly into the proprietary runtime. Only validated interfaces, compatible dependencies, or independently implemented patterns are promoted.

## Current gate result
**Gate 22 hardware/OEM architecture: IMPLEMENTED.**
**Runtime hardware support: NOT YET VERIFIED.**
**OEM-specific functionality: PROFILED, NOT CLAIMED VERIFIED.**
**Cross-platform desktop/iOS/web: ARCHITECTURE-DEFINED, NOT CLAIMED VERIFIED.**
