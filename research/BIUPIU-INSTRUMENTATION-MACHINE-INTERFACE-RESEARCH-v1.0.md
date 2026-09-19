# Biupiu Instrumentation & Machine Interface Research Register v1.0

**Date:** 20 September 2026  
**Status:** Research integration gate — references/adapters only until licence, security, compatibility and hardware-in-loop gates pass.

## Purpose
Routes reusable instrumentation, telemetry, industrial communication, robotics and machine-interface resources into the Biupiu OS Intelligence / Machine Capability architecture.

## Priority architecture
SENSORS/INSTRUMENTS -> EDGE ACQUISITION -> MACHINE CAPABILITY SCHEMA -> OPC UA/MQTT/MODBUS/OTHER ADAPTER -> DIGITAL TWIN -> MATH/PHYSICS -> AI/ANALYTICS -> VALIDATION -> CONTROLLED ACTUATION

## High-value resources
- ROS-Industrial: https://github.com/ros-industrial — industrial robotics and ROS/ROS 2 interoperability reference.
- CNR-ITIA/COMAU: https://github.com/CNR-STIIMA-IRAS/comau-experimental — Italian industrial robot integration reference.
- Serial Studio: https://github.com/Serial-Studio/Serial-Studio — telemetry/instrumentation and PLC/SCADA-adjacent monitoring reference.
- HumaRobotics Modbus: https://github.com/HumaRobotics/modbus — Python Modbus/ROS reference including Siemens PLC integration.
- PLCnext ROS bridge: https://github.com/PLCnext/PLCnext-ROS-bridge — ROS/ROS 2 to IEC 61131 PLC bridge reference.
- Siemens OPC UA: https://www.siemens.com/en-us/products/opc-ua/ — vendor-independent industrial communication and information modelling reference.
- Siemens RoboDK: https://www.siemens.com/en-gb/products/robodk/ — simulation, offline programming, reachability and virtual commissioning benchmark.
- Siemens industrial AI: https://www.siemens.com/en-gb/content/architecture-hub/industrial-ai-orchestration-layer/ — industrial edge, MQTT/OPC UA/REST and AI orchestration reference.
- Fujitsu Research: https://github.com/FujitsuResearch — AI, optimisation, anomaly detection and agent-evaluation research source.

## Instrumentation contract
Every Biupiu instrument/device adapter should expose where possible:
identity, manufacturer/model, firmware/software version, capability schema, sensor channels, actuator channels, units, calibration state, sampling rate, timestamp/clock source, quality flags, operating range, alarms/events, communication endpoint, protocol, safety constraints, Digital Twin reference and provenance/version.

Minimum telemetry record:
device_id, timestamp, channel_id, value, unit, quality, calibration_id, source_protocol, twin_id, schema_version, provenance_id

## AI instrumentation path
raw signal -> validation -> normalisation -> feature extraction -> Digital Twin association -> model inference -> uncertainty -> decision proposal -> simulation/validation -> authorised action

AI must not silently convert inferred state into observed state.

## Gate rules
1. Research source is not automatically a production dependency.
2. Licence must be recorded.
3. Security review precedes privileged integration.
4. Protocol adapters conform to the Biupiu Machine Capability contract.
5. Hardware-in-loop testing precedes physical actuation.
6. Safety-critical control remains independently validated.
7. Provenance survives telemetry transformation.
8. Foreign-language sources retain original terminology and source identity.

## Status
Italian and German sources are prioritised, with Siemens and Fujitsu explicitly routed into the research layer. Instrumentation, automation, robotics and AI are cross-linked to MATH, COMPUTE, AI, DIGITAL-TWIN, ROBOTICS, ELECTROMAG and ADV-MFG.
