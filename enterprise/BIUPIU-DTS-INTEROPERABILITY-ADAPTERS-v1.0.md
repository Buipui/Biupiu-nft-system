# Biupiu Digital Twin System Interoperability Adapters v1.0

**Date:** 19 September 2026
**Status:** Architecture contract

## Adapter matrix

| External pattern | Biupiu adapter role | Boundary |
|---|---|---|
| Eclipse Ditto | twin state, policy, connectivity, events | Twin Gateway |
| FIWARE NGSI-LD | contextual entity exchange | Context Gateway |
| AAS / Eclipse BaSyx | industrial asset semantics | Asset Adapter |
| W3C Web of Things | semantic device description | Thing Adapter |
| FMI / OpenModelica | model exchange/co-simulation | Simulation Adapter |
| ROS 2 / Gazebo / PyBullet | robotics and physics simulation | Robotics Adapter |
| O3DE / UE5 / Blender | 3D visualisation/simulation client | Experience Adapter |
| Kafka / MQTT / HTTP / AMQP | event and telemetry transport | Event Gateway |

## Non-negotiable boundaries

1. External projects are not authoritative over Biupiu enterprise identity.
2. External project schemas are mapped into canonical Biupiu contracts.
3. External code is not copied into production without licence and security review.
4. A failed adapter must not corrupt authoritative twin state.
5. Adapter transformations must be versioned and testable.
6. Provenance must identify the external source and transformation version.

## Routing

`Physical/External System -> Transport -> Adapter -> Canonical Event -> Twin/Context -> Decision -> Approved Process -> Adapter -> External System`

## Compatibility strategy

Adapters are replaceable. The enterprise architecture therefore remains independent of any single open-source project or vendor.

## Validation

Each adapter requires:
- schema tests;
- round-trip mapping tests where applicable;
- authentication/authorisation tests;
- malformed-message tests;
- version compatibility tests;
- provenance tests;
- failure/retry tests;
- performance/load tests before production promotion.
