# BIUPIU WORLD — VISUAL / HMI / INSTRUMENTATION GATE v1.0
## 20 September 2026

## Purpose
Canonical screen-interface and smart-systems integration contract for Biupiu World, aligned with Biupiu OS architecture for farming, automotive, aerospace/hangar, marine, robotics, world-development and media/rendering systems.

## World visual system
- Unified Biupiu premium biotech × regenerative aesthetic.
- Deep-green/gold visual identity remains authoritative.
- Legibility is a hard requirement at target display distance and resolution.
- Shared Asset IDs, provenance state and visual-QA state apply to World and simulator assets.

## Core HMI
Primary multi-panel HMI: System State/Health | Active Subsystem | Live Instrumentation | Alerts/Faults | Controls/Commands | AI Recommendations | Evidence/Provenance.
AI recommendations cannot directly execute safety-critical commands without the applicable OS authority gate.

## Instrumentation schema
Device ID -> sensor/channel -> timestamp -> value/unit -> quality -> calibration state -> fault state -> source -> evidence state.
Initial telemetry families: power/energy, thermal, pressure, flow, speed/RPM, position, structural/load, environmental, battery/storage, CAN-FD communications, agricultural soil/plant/water, marine and aerospace vehicle state.

## Smart-system interface
SENSOR -> EDGE DEVICE -> BIUPIU OS DRIVER -> VALIDATION -> INTELLIGENCE EVENT BUS -> HMI -> AI ANALYSIS -> HUMAN/OS AUTHORITY -> ACTUATOR.
Diagnostic states: NOMINAL / DEGRADED / WARNING / FAULT / ISOLATED / RECOVERY / VERIFIED.

## Simulator visual classes
Biupiu World control centre; Farming OS touchscreen; Automotive cockpit/HMI; Marine bridge/HMI; Aerospace/hangar instrumentation; Robotics control station; Laboratory instrumentation; Energy/power systems; Environmental/regenerative-farming dashboards.

## Exterminate rules
Reject unreadable UI text; contradictory telemetry units; duplicate device IDs; stale telemetry without explicit stale state; AI output presented as measured data; assets without Asset ID/provenance; safety-critical controls without authority state.

## Smoke-test gate
Architecture and repository contract are registered. Full runtime smoke testing requires the actual simulator/development host and connected instrumentation hardware or a deterministic telemetry simulator.

**STATUS: VISUAL/HMI CONTRACT REGISTERED. HOST RUNTIME EXECUTION PENDING.**