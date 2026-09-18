# Biupiu World — 3D Gate 04: Workshop Interaction & Digital-Twin Binding v1.0

## Status
Specification committed for runtime/3D implementation. This gate defines the interaction contract between department avatars, workshop objects, digital-twin records, simulated/live telemetry, research records and dashboards. It does not claim that live IoT hardware, binary 3D assets, or production runtime code have been deployed.

## Objective
Connect the Gate 03 specialist avatars to reusable workshop interaction anchors and digital-twin objects while preserving department isolation, provenance, evidence-state controls, auditability and desktop/Android performance.

## Runtime architecture
`AVATAR → INTERACTION ANCHOR → OBJECT/TWIN ADAPTER → ACCESS CHECK → OBJECT STATE → TELEMETRY/SIMULATION → RESEARCH EVENT → DASHBOARD`

The same contract must support:
- static 3D props;
- simulated machines;
- future sensor-connected machines;
- research instruments;
- environmental systems;
- vehicles and mobile equipment;
- department dashboards.

## Digital-twin object model
Every interactive object uses a logical twin record with:
- `twin_id`
- `asset_id`
- `package_id`
- `department_id`
- `environment_id`
- `project_id`
- `object_type`
- `version`
- `source`
- `creator`
- `licence`
- `provenance`
- `evidence_state`
- `access_scope`
- `operating_mode`
- `state`
- `telemetry_schema`
- `interaction_schema`
- `research_bindings`
- `dashboard_bindings`
- `safety_class`
- `status`

## Operating modes
### SIMULATION
Uses deterministic or scenario-driven values. Suitable for world-building, education, design studies and test workflows.

### REPLAY
Uses previously captured datasets without implying that the source is currently live.

### LIVE
Reserved for a future authenticated sensor/device gateway. Live status must only be shown when a trusted connector reports current data.

### OFFLINE
Uses cached metadata and locally available simulation/research records. No stale telemetry may be labelled live.

## Object state machine
`LOCKED → AVAILABLE → INSPECTING → ACTIVE → PAUSED → COMPLETE`

Failure/exception path:
`ACTIVE → FAULT → SAFE/PAUSED → REVIEW`

State transitions require:
1. entitlement;
2. valid interaction context;
3. compatible object state;
4. required input/data availability;
5. audit event.

## Interaction anchors
Each interactive object exposes named anchors such as:
- `INTERACT_PRIMARY`
- `INTERACT_SECONDARY`
- `INSPECT`
- `INSERT_SAMPLE`
- `REMOVE_SAMPLE`
- `CONTROL_PANEL`
- `SENSOR_VIEW`
- `MAINTENANCE`
- `DATA_VIEW`
- `SAFE_EXIT`

Anchors must be scale/orientation compatible with the Gate 02 humanoid base and must support desktop and Android interaction targets.

## Department bindings

### Farming
Twin examples:
- irrigation controller
- soil sensor
- weather station
- nursery system
- regenerative trial plot
- water storage system

Research bindings:
`FieldRecord, SoilRecord, WaterRecord, SensorRecord, IrrigationRun, TrialRecord, YieldRecord`

### Metallurgy
Twin examples:
- furnace
- forge
- material test station
- measurement bench
- heat-treatment setup
- workshop inventory station

Research bindings:
`MaterialRecord, AlloyRecord, HeatTreatmentRun, FurnaceRecord, ForgeRecord, TestRecord, Measurement, FailureRecord`

Safety-related interactions remain simulation/information unless separately certified by the relevant real-world system.

### Textiles
Twin examples:
- spindle
- loom
- dye station
- fibre preparation bench
- sample catalogue station

Research bindings:
`FibreRecord, TextileRecord, ProcessRecord, ReferenceSource, ExperimentRecord`

Cultural variants require provenance and evidence-state metadata.

### Materials
Twin examples:
- specimen preparation bench
- microscope/scan interface
- composite layup station
- test rig
- measurement station

Research bindings:
`MaterialRecord, CompositeRecord, TestRecord, Measurement, FailureRecord, ReferenceSource`

## Telemetry contract
Telemetry records should support:
- `timestamp`
- `source_id`
- `twin_id`
- `mode`
- `metric`
- `value`
- `unit`
- `quality`
- `sequence`
- `location_context`
- `schema_version`

Examples:
- temperature
- pressure
- flow
- humidity
- soil moisture
- vibration
- RPM
- power
- force
- material test measurement

Units and measurement semantics must be explicit. Unknown or inferred values must not be silently promoted to measured values.

## Research-event binding
Every meaningful interaction can emit:
`INTERACTION → OBSERVATION → MEASUREMENT → RESULT`

Event fields:
- `event_id`
- `timestamp`
- `actor_id`
- `subscriber_id`
- `department_id`
- `twin_id`
- `project_id`
- `action`
- `input_state`
- `output_state`
- `telemetry_refs`
- `research_record_refs`
- `evidence_state`
- `result`
- `audit_status`

Negative results and failed simulations remain retained as research history.

## Access-control contract
Before any object interaction:
1. resolve subscriber;
2. resolve organisation/tenant;
3. resolve department entitlement;
4. resolve project/resource scope;
5. resolve object access;
6. expose only authorised controls/data.

The access firewall applies to:
- 3D interaction;
- object inspection;
- AI retrieval;
- search;
- dashboards;
- exports;
- notifications;
- future live telemetry.

Leaving a department/workstation invalidates temporary object access.

## Dashboard binding
Dashboards consume authorised twin and research events rather than bypassing the access layer.

Department dashboards may show:
- object availability;
- simulated/live/offline mode;
- latest authorised measurements;
- experiment status;
- failures;
- maintenance state;
- project KPIs;
- research-result links.

Cross-department dashboards require explicit shared entitlement.

## Safety and simulation boundary
- Simulation labels must remain visible where relevant.
- Live data must carry source and freshness metadata.
- No virtual control should be represented as a real-world safety certification.
- Emergency/unsafe states in real hardware require an external certified safety system; the world layer is not that safety system.
- Historical, speculative and fictional environments retain their evidence-state labels.

## Mobile/offline strategy
Android:
- load only department-required twins and interaction assets;
- use simplified interaction UI;
- stream telemetry selectively;
- cache approved research metadata;
- fall back to SIMULATION/OFFLINE when live services are unavailable;
- never display cached live telemetry as current.

Desktop:
- support richer telemetry panels and multi-object dashboards;
- retain the same permission and data contracts.

## Provenance and licence
Digital twins inherit source/licence/provenance metadata from their assets and linked research objects. Mod/game-derived assets require licence verification before runtime redistribution. Reference-only assets may inform reconstruction but are not automatically runtime assets.

## Test matrix
| Test | Expected result |
|---|---|
| Entitlement before interaction | access denied unless authorised |
| Object inspection | authorised metadata only |
| State transition | invalid transitions rejected |
| Simulation telemetry | labelled SIMULATION |
| Replay telemetry | labelled REPLAY |
| Offline mode | no LIVE label |
| Live connector absent | fallback without fabricated telemetry |
| Research event | auditable event created |
| Dashboard | respects department scope |
| Cross-department object | blocked without explicit shared entitlement |
| Workstation exit | temporary access revoked |
| Provenance check | missing licence/provenance blocks restricted integration |
| Android LOD | unused objects/effects omitted |
| Negative result | retained as research history |

## Acceptance criteria
1. Gate 03 avatars can resolve reusable interaction anchors.
2. Interactive objects have a versioned digital-twin schema.
3. Simulation, replay, live and offline states are explicitly distinguished.
4. Object state transitions are deterministic and auditable.
5. Department entitlements are checked before object/data exposure.
6. Telemetry has explicit source, units, quality and mode metadata.
7. Research events link interactions to authorised project records.
8. Dashboards cannot bypass the access firewall.
9. Mobile clients can operate with scoped/offline data.
10. No live hardware integration is claimed until a trusted connector exists.
11. Provenance/licensing and evidence-state controls remain mandatory.

## Package convention
`TWIN-<department>-<object>/`
- `manifest.json`
- `model/`
- `colliders/`
- `anchors/`
- `materials/`
- `lod/`
- `twin/`
- `telemetry/`
- `interactions/`
- `research-bindings/`
- `ui/`
- `tests/`
- `licence/`
- `provenance/`

## Next gate
**Gate 05 — Cross-department campus systems and shared-service layer**, connecting department environments through navigation, identity, shared utilities, controlled cross-department projects, asset streaming and world-level service APIs.
