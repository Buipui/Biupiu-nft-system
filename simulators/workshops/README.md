# Biupiu Workshop Simulators

This directory contains department-specific simulator definitions built on the automotive workshop and flight-hangar work.

## Current gates
- Shared workshop lifecycle: defined.
- Automotive workshop: reference architecture defined.
- Hangar maintenance: reference architecture defined.
- Department simulator registry: created.
- External resource registry: created.
- UE5 integration: adapter-ready architecture; engine/project implementation remains dependent on the active UE5 project tree.

## Rule
Do not duplicate physics, diagnostics, inventory, safety, telemetry or digital-twin logic per department. Extend the shared contracts and provide domain adapters.
