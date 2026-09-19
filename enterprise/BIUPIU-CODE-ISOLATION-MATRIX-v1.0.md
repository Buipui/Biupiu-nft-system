# Biupiu Open-Source Code Isolation Matrix v1.0

## Candidate components

| Reference | Potentially reusable layer | Promotion rule |
|---|---|---|
| Eclipse Ditto | twin state, device abstraction, messaging patterns | isolate adapter; licence/dependency/security review |
| Eclipse BaSyx | AAS/Industry 4.0 asset semantics | isolate semantic adapter; test against AAS |
| FIWARE NGSI-LD | context/entity/relationship interoperability | isolate context adapter; validate NGSI-LD |
| W3C Web of Things | Thing Description / semantic interoperability | use standards-compatible schema adapter |
| OpenModelica/FMI | engineering model exchange and simulation | isolate FMI adapter; deterministic test |
| ROS 2/Gazebo | robotics and simulation interfaces | isolate robotics adapter; safety validation |
| PyBullet | physics/robotics prototyping | sandboxed simulation dependency |
| O3DE | 3D simulation/visualisation | presentation/simulation adapter only |
| IndustryFusion Process Data Twin | industrial semantic/data patterns | architecture reference; code only after licence review |

## Isolation rule

No third-party code is copied into Biupiu core merely because it is useful. Candidate repositories are isolated as external dependencies or adapters until:

1. licence compatibility is confirmed;
2. dependency tree is reviewed;
3. security posture is checked;
4. API/schema compatibility is tested;
5. deterministic tests pass;
6. provenance records the upstream project/version/commit;
7. a maintainer explicitly promotes the dependency.

## Current implementation

The Digital Twin core now implements Biupiu-native context and AAS-style references rather than embedding third-party runtimes. This keeps the core portable while allowing future adapters.

## Gate status

Architecture integration: PASS.
External-code promotion: NOT YET PROMOTED pending repository-specific licence/security/test evidence.
