# Biupui DigiCiv — Architecture + Farming + Light Information Map

**Date:** 2026-09-24  
**Status:** ARCHITECTURE REGISTERED — IMPLEMENTATION GATE REQUIRED

## Purpose

DigiCiv is the Biupui digital-civilisation matrix for creating, comparing and observing machine-readable maps of interacting systems.

The first integrated simulator pair is:

- **Architecture Simulator** — built environment, infrastructure, topology, spatial relationships and candidate optical paths.
- **Farming Simulator** — soil, water, crop/environment state, telemetry and agricultural resource flows.

These become map-producing systems rather than isolated simulators.

## System-within-system structure

```text
BIUPUI INTELLIGENCE
        |
     DigiCiv
        |
  +-----+------------------------------+
  |                                    |
DigiCat                              DigiFile
catalogue                             evidence
  |                                    |
  +----------------+-------------------+
                   |
          Computational Geometry
                   |
             +-----+------+
             |            |
       Architecture     Farming
        Simulator      Simulator
             |            |
             +-----+------+
                   |
          Environment / Terrain
                   |
          Light Information Map
                   |
       +-----------+-----------+
       |           |           |
      FSO         VLC     Structured Light
       |           |           |
       +-----------+-----------+
                   |
          Quanticor Referee
                   |
       Native Quantum Protocol
                   |
      regression / learning / anchor
```

## Map classes

DigiCiv maintains separate but cross-linked maps:

1. Architecture map
2. Farm/ecology map
3. Infrastructure map
4. Resource-flow map
5. Sensor/telemetry map
6. Light-path map
7. Information-transfer map
8. Simulated-environment map
9. Observed-environment map
10. Native-quantum-protocol map

### Simulated versus observed

A **simulated map** represents model-generated states and candidate paths.

An **observed map** represents measured or directly recorded environmental/system behaviour.

They must never be silently merged.

```text
SIMULATION -> candidate geometry/path -> experiment
OBSERVATION -> measured geometry/path -> evidence
                                  |
                              comparison
                                  |
                              Quanticor
```

## Farming → light transfer

The farming environment becomes part of the optical channel model.

Relevant state variables include:

- terrain
- crop/vegetation geometry
- water and irrigation state
- atmospheric conditions
- dust/particles where measured
- structures
- sensor nodes
- power availability
- line-of-sight
- receiver placement

This allows Biupui to test how an agricultural environment changes candidate light-information paths.

## Architecture → light transfer

The architecture simulator contributes:

- transmitter/receiver placement
- line-of-sight
- obstruction/occlusion
- reflections and candidate surfaces
- node topology
- infrastructure connectivity
- energy/resource availability

The resulting optical graph can be passed to Quanticor as a controlled intersection candidate.

## Native quantum protocol boundary

The phrase **native quantum protocol** refers here to the Biupui computational protocol layer for representing and testing quantum/photonic information models.

It does **not** claim that the current Biupui software has physical quantum or photonic hardware.

The controlled path is:

```text
OBSERVE
  -> MAP
  -> ENCODE
  -> INTERSECT
  -> REFEREE
  -> DECOMPOSE
  -> DEFRAGMENT
  -> ANCHOR
  -> RECOMPILE CANDIDATE
  -> REGRESSION
  -> LEARN
  -> OPTIMISE
  -> PROMOTE
```

## DigiCat role

DigiCat indexes:

- simulator
- map
- node
- interface
- capability
- information path
- environmental condition
- benchmark
- external research relationship
- Quanticor state

DigiCat is not execution authority.

## DigiFile role

DigiFile records:

- input state
- simulator version
- source revision
- generated map hash
- observation hash
- measurement metadata
- model parameters
- external source provenance
- test evidence
- transformation history
- Quanticor event ID
- promotion state

Every meaningful map transformation should therefore remain reconstructable.

## Performance matrix

The first common benchmark dimensions are:

| Dimension | Architecture | Farming | Light transfer | Quanticor |
|---|---|---|---|---|
| Functional equivalence | ✓ | ✓ | ✓ | ✓ |
| Path availability | ✓ | ✓ | ✓ | ✓ |
| Latency | ✓ | ✓ | ✓ | ✓ |
| Throughput | ✓ | ✓ | ✓ | ✓ |
| Information integrity | — | — | ✓ | ✓ |
| Environmental loss | ✓ | ✓ | ✓ | ✓ |
| Occlusion | ✓ | ✓ | ✓ | ✓ |
| Resource availability | ✓ | ✓ | ✓ | ✓ |
| Fault/recovery | ✓ | ✓ | ✓ | ✓ |
| Provenance | ✓ | ✓ | ✓ | ✓ |

Performance claims remain evidence-gated. External research supplies benchmark dimensions and hypotheses; executable tests and physical measurements supply acceptance evidence.

## Integration rule

No existing simulator is deleted or replaced.

The current architecture/farming implementations remain independently operable and are additionally exposed through the DigiCiv mapping contract.

**AS-IS tree** and **BUIPUI Native Systems tree** must both be able to consume the same map/evidence vocabulary.

## Current gate

- Architecture mapping: REGISTERED
- Farming mapping: REGISTERED
- Light-information mapping: REGISTERED RESEARCH MODEL
- Quantum mapping: REGISTERED RESEARCH MODEL
- DigiCat integration: CONTRACT DEFINED
- DigiFile integration: CONTRACT DEFINED
- Physical photonic validation: NOT CLAIMED
- Physical quantum validation: NOT CLAIMED
- Production promotion: BLOCKED pending executable/regression evidence
