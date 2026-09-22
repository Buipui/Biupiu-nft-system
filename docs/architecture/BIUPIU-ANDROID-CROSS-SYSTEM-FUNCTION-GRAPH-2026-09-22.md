# Biupiu Android Cross-System Function Graph — 2026-09-22

Status: MAINLINE CANDIDATE — source-integrated; host/device runtime verification remains a separate gate.

## Runtime graph

MAIN ACTIVITY
→ BIUPIU APP / SHELL
→ MAIN HUB
→ CAPABILITY ROUTER
→ RUNTIME SESSION + ENTITLEMENT CHECK
→ DEPARTMENT MODULE REGISTRY
→ DEPARTMENT ACTIVITY / ADAPTER
→ SHARED RUNTIME CONTRACTS
→ DIGITAL TWIN / SIMULATOR EVENT
→ FEDERATION TRANSPORT
→ LEARNING EVENT LOG
→ BOUNDED ADAPTATION PROPOSAL
→ VALIDATION + REGRESSION
→ HUMAN/POLICY GATE
→ VERSIONED PROMOTION
→ DIGITAL TWIN UPDATE

Parallel cross-platform paths:

Android
→ Kotlin/Compose shell
→ shared TypeScript runtime contracts
→ native AI/federation adapters

Windows
→ WPF shell
→ same route/capability contract
→ shared TypeScript runtime contracts

R&D OS / AI
→ simulator registry
→ learning federation bridge
→ failure/drift classification
→ bounded adaptation

World / Digital Twin
→ asset/twin identity
→ simulation/test events
→ provenance
→ federation envelope

## Current Android route matrix

| Route | Registry | Runtime target | Current source status |
|---|---|---|---|
| SMART_FARMING | DepartmentModuleRegistry | SmartFarmingActivity | implemented |
| SMART_METAL_WORKSHOP | DepartmentModuleRegistry | SmartMetallurgyActivity | implemented |
| RND_OS | DepartmentModuleRegistry | RndOsActivity | implemented |
| RENDER_PIPELINE | DepartmentModuleRegistry | RenderPipelineActivity | repaired in this gate |
| CREATIVE_AI | DepartmentModuleRegistry | capability registered; no local activity | fail-closed / not locally enterable |

## Build layers

1. Gradle project configuration
2. Android application module
3. Compose UI + semantic state
4. Capability and entitlement routing
5. Department runtime adapters
6. Shared TypeScript contracts
7. Digital Twin contract
8. Federation transport
9. Native R&D OS AI learning bridge
10. Simulator adapters
11. CI/static/build/runtime verification

Android Studio's module model supports independently building, testing and debugging discrete functionality; Gradle build variants provide the packaging boundary. Biupiu therefore keeps platform shell code separate from shared contracts and simulator/AI layers.

## Verification boundary

PASS means source/configuration evidence exists.

NOT VERIFIED means an actual Android SDK/device/emulator/Gradle build has not been executed in the current tool session.

The repository currently records that the Android Gradle wrapper artifacts are incomplete/pending CI bootstrap. The new CI gate must use a pinned Gradle 8.9 toolchain rather than silently calling a missing wrapper.

## Harvested architectural inputs

- OpenUSD: layered/composable scene description and modular schemas.
- Gazebo Sim: physics/rendering/sensor/plugin/message-passing separation.
- ROS/digital-twin projects: explicit simulation, transport and hardware boundaries.
- Chinese digital-twin repositories: model → task → simulation → validation → export loops and bilingual documentation.
- RobWoT/TUM: URDF → digital twin/Thing Description generation and simulation interfaces.
- OpenBooks patterns: modular workspaces, append-only/event-oriented state, explicit API contracts and dependency checks were treated as architectural patterns only.

No external source code is copied into Biupiu by this harvest. External repositories remain references/adapters unless independently reimplemented and license-reviewed.
