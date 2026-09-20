# Biupiu OS Simulator Kernel v1.0

Date: 2026-09-19
Status: IMPLEMENTED AT SOURCE LEVEL; CONNECTED RUNTIME VALIDATION OPEN

## Canonical flow
CREATE -> LOAD -> REGISTER -> RUN -> EVENT -> MEASURE -> VALIDATE -> PROVENANCE -> REPLAY -> RELEASE GATE

## Gates
- OS-SIM-01 Runtime Bootstrap
- OS-SIM-02 Simulation Kernel
- OS-SIM-03 Deterministic Replay
- OS-SIM-04 Digital Twin Bridge
- OS-SIM-05 OpenUSD Boundary
- OS-SIM-06 Engine Adapter
- OS-SIM-07 Smart Systems Control Surface

OS-SIM-01 to OS-SIM-03 now have source-level implementation and regression coverage. OS-SIM-04 to OS-SIM-07 remain planned implementation gates.

## Invariants
Simulation starts explicitly; duplicate entities are rejected; unknown measurement targets are rejected; external engines remain adapters; physical actuation requires separate safety validation; AI cannot bypass OS validation/provenance.

## Routing
Core OS, Digital Twin, PHYS-SYS, GPU-SYS, CG-3D, GEOMETRY, COMPUTE, AI, ROBOTICS, AERO, MARINE, AUTO, AGRI, WATER, ADV-MFG.

A gate is PASS only after a real CI or connected-host result. Repository presence alone is not runtime verification.

## P0 Multi-Language Core Binding — 20 September 2026
The simulator kernel is bound to the Core OS language contract: C ABI/HAL -> Rust safety-oriented services -> C++ simulation/geometry/graphics -> OS validation -> Digital Twin -> Intelligence. Simulator adapters must not bypass the C ABI/OS contract.

Source seed: `core/multilang/`. Build/runtime evidence remains required before promotion.
