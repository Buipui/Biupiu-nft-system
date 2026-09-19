# Biupiu Enterprise Digital Twin System v1.1

**Date:** 19 September 2026
**Status:** Architecture update — open-source compatibility patterns integrated; runtime deployment remains a separate gate.

## Purpose

Upgrade the Biupiu Enterprise Digital Twin from a domain integration layer into an interoperable Digital Twin System architecture that can coordinate data, context, decisions, process orchestration and controlled actuation across departments.

This record integrates **architectural patterns**, not unreviewed third-party source code. External projects remain replaceable compatibility targets and are subject to licence, security, API, performance and validation gates before code is incorporated.

## Target architecture

`Biupiu OS Core -> DMS Control Plane -> Enterprise Control Plane -> Enterprise Context/Knowledge Graph -> Digital Twin System -> Decision & Process Orchestration -> Domain Services -> Controlled Actuation`

A **Digital Thread** crosses every layer.

### DTS layers

1. **Data Layer**
   - telemetry and sensor data
   - engineering/model data
   - enterprise records
   - research evidence
   - simulation outputs
   - asset state
   - event streams

2. **Context Layer**
   - canonical entities
   - ontology and typed relationships
   - semantic identifiers
   - site/project/department context
   - asset and process context
   - provenance/evidence context

3. **Decision & Process Orchestration Layer**
   - rules and algorithms
   - physics/mathematics services
   - AI decision support
   - optimisation
   - workflow orchestration
   - scenario comparison
   - human approval gates
   - policy and entitlement checks

4. **Actuation Layer**
   - software commands
   - work orders
   - robotic workflows
   - simulation execution
   - approved machine/device commands
   - human operators

Actuation is always bounded by authorisation, safety and validation controls.

## Open-source architecture patterns integrated

### Eclipse Ditto pattern

Adopt as a compatibility pattern for:
- twin identity and state;
- reported/current/desired state separation;
- asynchronous command/event messaging;
- policy-controlled resources;
- connectivity abstraction;
- search/indexing of twins.

Ditto supports microservices for Policies, Things, Things-Search, Gateway and Connectivity, with external connections including MQTT, AMQP, HTTP and Kafka. See the external evidence record in the open-source manifest.

### FIWARE NGSI-LD pattern

Adopt as a compatibility pattern for:
- context federation;
- linked entity/context identifiers;
- cross-domain context exchange;
- interoperability between independent services.

### DTC Digital Twin System pattern

Adopt the four-layer Data / Context / Decision & Process Orchestration / Actuation separation as the top-level DTS model, with Digital Thread as the lifecycle connector.

### DTC interoperability pattern

Use interoperability as a first-class architecture concern rather than assuming all systems share one data model. Interfaces must declare identity, semantics, transport, security, lifecycle and version compatibility.

### Industry 4.0 / AAS pattern

Use Asset Administration Shell concepts where useful for industrial asset identity, submodels and structured asset semantics. Do not force AAS onto domains where another canonical model is more appropriate.

### Web of Things pattern

Use semantic Thing Descriptions as an interoperability option for physical/IoT entities and machine-readable capabilities.

### FMI/OpenModelica pattern

Use model-exchange/co-simulation interfaces as an engineering integration boundary rather than embedding individual simulation engines into the Enterprise Twin core.

### ROS 2 / Gazebo / PyBullet pattern

Use robotics middleware and simulation as domain services behind the actuation/engineering contracts. The enterprise architecture must not depend on one robotics simulator.

### O3DE / UE5 / Blender pattern

Treat 3D engines as presentation/simulation clients of the Twin, not authoritative system-of-record databases.

## Canonical twin contract

Each twin should expose, directly or through an adapter:

- `twin_id`
- `entity_type`
- `namespace`
- `version`
- `identity`
- `relationships`
- `reported_state`
- `desired_state`
- `computed_state`
- `capabilities`
- `telemetry_refs`
- `model_refs`
- `simulation_refs`
- `evidence_refs`
- `provenance`
- `policy_ref`
- `lifecycle_state`
- `updated_at`

## Event contract

Commands, responses and events must carry:

`event_id, correlation_id, twin_id, event_type, schema_version, timestamp, producer, causality_ref, evidence_ref, payload`

Unknown schema versions fail closed at controlled boundaries.

## Enterprise graph contract

The enterprise graph becomes the cross-linking mechanism for:

`Department -> Project -> Asset -> Twin -> Model -> Simulation -> Result -> Evidence -> Decision -> Work Order -> Product -> Cost -> Revenue/IP`

Relationship creation must be explicit and typed.

## State model

Use separate state channels:

- **observed** — what sensors/external systems report;
- **desired** — approved target state;
- **computed** — derived/calculated state;
- **simulated** — scenario state;
- **validated** — state supported by accepted evidence;
- **actuated** — commands actually issued/executed.

No simulated or desired state is silently promoted to observed or validated state.

## Enterprise functions enabled

- enterprise-wide dependency mapping;
- cross-department impact analysis;
- asset lifecycle management;
- digital-thread traceability;
- engineering-to-commercial linkage;
- R&D-to-product linkage;
- manufacturing and maintenance orchestration;
- AI/algorithm routing;
- scenario and what-if analysis;
- treasury/resource impact mapping;
- provenance and evidence tracking;
- controlled automation;
- multi-client visualisation;
- future multi-site/multi-tenant expansion.

## Security and governance

- least-privilege policies;
- namespace isolation;
- tenant/site/department boundaries;
- signed/provenance-aware evidence;
- audit events;
- secrets outside source and blockchain;
- blockchain used as optional integrity anchor;
- human approval for consequential financial, IP, safety and physical actions;
- no autonomous physical actuation merely because an AI recommendation exists.

## Integration rule

Do not create direct database coupling between departments when an enterprise contract/event/reference can perform the integration.

## Release gates

`DISCOVER -> LICENSE/PROVENANCE -> SCHEMA -> CONTRACT -> SECURITY -> STATIC -> UNIT -> INTEGRATION -> SIMULATION -> VALIDATION -> INDEX -> COMMIT -> RELEASE`

Runtime deployment, live telemetry and physical validation remain separate execution gates.
