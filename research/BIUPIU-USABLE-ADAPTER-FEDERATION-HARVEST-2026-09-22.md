# BIUPIU FEDERATION USABLE-ADAPTER EXTERNAL HARVEST — 2026-09-22

Status: HARVESTED / NORMALISED / NATIVE REGISTRY INTEGRATED / EXECUTABLE PROMOTION GATED

## Scope

Internal repositories were searched first for existing adapter contracts, capability registries, simulator boundaries, Digital Twin transport, federation transport, multilingual routing, machine capability and guided-fault infrastructure.

External federation harvest then searched current/open resources across:
- foreign OEM/industry collaborations;
- open automotive/software-defined-vehicle projects;
- development organisations and standards bodies;
- government research/open-source portals;
- nonprofit/open-source foundations;
- robotics/simulation/federated-learning ecosystems.

No proprietary OEM source, restricted material, credentials, classified material or copied third-party implementation was imported.

## Current usable adapter set

The native registry is:
`software/rnd-os-ai/src/biupiu_ai/adapter_registry.py`

Registered interface families:
1. MQTT 5 — IoT/device/event transport.
2. Eclipse Ditto — Digital Twin state/connectivity over HTTP, MQTT, Kafka and AMQP.
3. OPC UA PubSub — industrial information models and telemetry.
4. ROS 2 / DDS — robotics topics/services/actions and simulator federation.
5. OpenUSD — world/scene and digital-world interchange.
6. FMI/FMU — model exchange and co-simulation.
7. Flower — federated ML.
8. NVIDIA FLARE — federated ML/privacy-preserving workflows.
9. OpenTelemetry — trace/context/telemetry correlation.
10. A2A — agent-to-agent interoperability.
11. OpenSharing — AI asset/data exchange.
12. AUTOSAR Adaptive CAPI — automotive middleware reference; access/licence conditions remain a promotion gate.

These are interface-level adapter records, not automatic third-party dependency installation.

## External evidence harvested

### Automotive / OEM ecosystem

**COVESA VSS/VISS**
- VSS provides a common vehicle-signal language independent of protocol/serialization.
- Current VSS repository shows active development and v6.0 release material.
- VISS provides standardised access to VSS data and supports HTTPS, MQTT and WebSockets.
- Contributors include BMW, Volvo Cars, Jaguar Land Rover, Robert Bosch and Geotab.
- Useful Biupiu route: AUTOMOTIVE -> MACHINE-CAPABILITY -> DIGITAL-TWIN -> AI -> DMS.

Sources:
- https://github.com/COVESA/vehicle_signal_specification
- https://github.com/COVESA/vehicle-information-service-specification

**COVESA Open1722**
- Open implementation of IEEE 1722 for audio/video, CAN/LIN tunnelling and peripheral access.
- Candidate transport adapter for automotive/industrial media and bus federation.
- Source: https://github.com/COVESA/Open1722

**AUTOSAR CAPI 1.0**
- AUTOSAR announced CAPI 1.0 in August 2026 with an implementation of the Adaptive Platform, including communication, execution management, logging and diagnostics.
- Useful as an automotive middleware compatibility/reference boundary.
- It is NOT promoted as unrestricted source because access is tied to AUTOSAR partner conditions.
- Sources:
  - https://www.autosar.org/capi
  - https://www.autosar.org/news-events/detail/capi-release-10-is-here

**Eclipse S-CORE / SDV**
- Open-source core-stack work for software-defined vehicles.
- Useful for OS/middleware/interface patterns and safety-oriented architecture.
- Source: https://github.com/eclipse-score

### Digital Twin / industrial

**Eclipse Ditto**
- Provides device-to-Digital-Twin integration with desired/reported/current state concepts.
- Supports managed connections including AMQP, MQTT, HTTP and Kafka and payload mapping.
- Useful for Biupiu Digital Twin/DMS transport abstraction.
- Sources:
  - https://eclipse.dev/ditto/
  - https://eclipse.dev/ditto/basic-connections.html

**OPC UA**
- Retained as an industrial information-model/PubSub adapter boundary.
- No vendor SDK is copied or promoted.

**FMI/FMU**
- Retained as a neutral model-exchange/co-simulation contract.
- Implementation-specific licence and runtime gates remain.

### Robotics / simulation

**ROS 2 / DDS**
- Retained as the primary robotics federation interface candidate.
- Current ROS 2 control documentation lists Gazebo, Isaac Sim, Webots and MuJoCo integration surfaces.
- Source: https://control.ros.org/

**NVIDIA Isaac Sim**
- Current documentation supports ROS 2 integration, programmatic simulation control, USD worlds, robot/entity management and synthetic-data workflows.
- It can operate with internal ROS libraries in some container workflows.
- Sources:
  - https://docs.isaacsim.omniverse.nvidia.com/
  - https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/overview/ros2_reference_architecture.html

**NASA RAPID**
- NASA's open-source RAPID reference framework provides standard programming interfaces and data-distribution middleware for interoperability between robot software modules.
- Useful as a robotics federation/interoperability pattern.
- Source: https://software.nasa.gov/software/ARC-16368-1A

### Federated ML / learning

**Flower**
- Framework-agnostic federated AI platform with support for multiple ML frameworks and numerous federated-learning strategies.
- Useful for the external federated-learning adapter boundary.
- Source: https://github.com/flwrlabs/flower

**NVIDIA FLARE**
- Open-source, domain-agnostic federated-learning SDK supporting privacy-preserving distributed collaboration and existing ML workflows.
- Useful as a candidate research adapter for federated training and analytics.
- Source: https://developer.nvidia.com/flare

### Observability / AI interoperability

**OpenTelemetry**
- Retained as a semantic trace/context/telemetry pattern for F18 observability.
- Core Biupiu remains dependency-light; external SDK adoption is separately gated.

**A2A**
- Linux Foundation reports the A2A project reached more than 150 supporting organisations and production deployments in 2026.
- Useful for agent-to-agent interoperability and cross-system task routing.
- Source: https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year

**OpenSharing**
- Linux Foundation announced OpenSharing in June 2026 as an open protocol for exchanging AI skills, models and data across platforms.
- Useful for future AI asset/data federation.
- Source: https://www.linuxfoundation.org/press/linux-foundation-announces-openSharing-project-to-standardize-ai-asset-and-data-exchange

### Government / standards / development research

**NASA Open Source**
- NASA's current open-source catalogue contains hundreds of approved projects, including robotics, simulation, distributed systems and AI-related resources.
- The catalogue includes RAPID, NTRTsim, xGDS and other reusable research software.
- Source: https://code.nasa.gov/

**NIST Digital Twin**
- NIST's 2026 work emphasises interoperability, VVUQ, cybersecurity, semantic models and standards for trustworthy Digital Twins.
- These patterns directly reinforce Biupiu's Digital Twin -> validation -> learning boundary.
- Sources:
  - https://www.nist.gov/publications/digital-twins-workshops-summary-report
  - https://www.nist.gov/programs-projects/digital-twins-advanced-manufacturing
  - https://www.nist.gov/digital-twins/digital-twin-standardization

**Japan NEDO**
- NEDO's 2026 AI programme inventory includes projects covering physical AI, multimodal foundation models, robot foundation models and next-generation computing.
- Used as a research-source routing signal rather than executable dependency.
- Source: https://www.nedo.go.jp/koubo/2026_list_05_03.html

**Linux Foundation**
- Current AI interoperability work includes A2A and OpenSharing.
- These are treated as protocol/reference candidates until repository-level licence/dependency/runtime gates pass.

## Internal integration executed

- Added `biupiu-adapter-registry` to the native federation registry.
- Added `adapter_registry.py` with deterministic interface records and fail-closed promotion checks.
- Added adapter regression tests.
- Added adapter set to the systemwide module registry.
- Added adapter-contract and governed-learning links to the system architecture registry.
- Upgraded Native ML learning policy with evidence-weighted reusable-learning scoring and drift penalty.
- Added Native ML regression tests for bounded scoring and human-gated reuse.
- Existing guided fault finding remains the first-line diagnostic route for adapter failures.

## Native learning upgrade

The learning engine now has an additional deterministic evidence policy:
- verified fix;
- regression safety;
- provenance quality;
- uncertainty reduction;
- recurrence/information gain;
- drift penalty.

The score is bounded and used only for candidate selection/prioritisation. It does not grant promotion authority.

Reuse still requires:
VERIFIED FIX -> REGRESSION -> PROVENANCE -> LICENCE -> LOW DRIFT -> HUMAN APPROVAL -> CORE OS PROMOTION

## Guided fault-finding route

Adapter and ML failures route through:

OBSERVE
-> CLASSIFY
-> OWNERSHIP
-> EVIDENCE
-> ISOLATE
-> REPAIR PROPOSAL
-> INDEPENDENT VALIDATION
-> REGRESSION
-> LEARNING
-> CONTROLLED REUSE

Security faults remain quarantined. Unknown/untrusted executables remain blocked.

## Semantic/code-function check

Source-level semantic review targets:
- adapter identity and deterministic lookup;
- family routing;
- promotion fail-closed behaviour;
- learning-score bounds;
- drift penalty;
- human approval boundary;
- registry cross-links;
- existing guided-fault contracts;
- external-vendor authority boundary.

Source-level implementation is recorded as complete. Runtime execution, clean build, security scan, cross-platform execution and hardware/runtime adapter verification remain separate gates.

## Department routing

Primary:
AI, COMPUTE, DIGITAL-TWIN, ROBOTICS, AUTOMOTIVE, ELECTROMAG, ENERGY, AGRI, ADV-MFG, MATERIALS, PHOTONICS, MARINE, AERO, BIOMED, MATH, GEOMETRY, IP.

Secondary:
WATER, HEMP, BIOCARBON, BIOCHEM, TEXTILES, COAT, LAND-GIS and NFT-PROV where adapters support sensing, modelling, provenance or manufacturing workflows.

Universal rule:
IP/licence review remains attached to every external adapter before executable promotion.

## Status

INTERNAL HARVEST: COMPLETE
EXTERNAL FEDERATION HARVEST: COMPLETE FOR CURRENT SEARCH SCOPE
NATIVE ADAPTER REGISTRY: IMPLEMENTED
NATIVE ML UPGRADE: IMPLEMENTED
GUIDED FAULT-FINDING CROSS-LINK: IMPLEMENTED
SEMANTIC SOURCE CHECK: IMPLEMENTED
FUNCTIONAL TESTS: ADDED
CI/BUILD/RUNTIME/HIL: OPEN UNTIL FRESH EXECUTION EVIDENCE
THIRD-PARTY EXECUTABLE PROMOTION: BLOCKED UNTIL GATES PASS
