# Biupiu World — 3D Gate 06: World Data/API Contract & Persistent Project State v1.0

## Status
Specification committed for implementation. Defines versioned world data contracts and persistence boundaries for subscribers, navigation, projects, research objects, digital twins, telemetry, events and synchronisation. It does not claim a production database, API server or live cloud deployment.

## Objective
Provide one versioned data contract connecting Gates 01–05 without coupling the 3D client directly to storage internals.

## Data architecture
`3D CLIENT → WORLD API → AUTH/ENTITLEMENT → DOMAIN SERVICE → PERSISTENCE`

Domain services:
- Identity
- Navigation
- Projects
- Research
- Digital Twins
- Telemetry
- Events/Audit
- Asset Registry
- Synchronisation

## Contract rules
Every persisted resource requires:
- `id`
- `schema_version`
- `created_at`
- `updated_at`
- `status`
- `owner_scope`
- `access_scope`
- `provenance`
- `version`

Updates use optimistic concurrency through a version/ETag-style field. Clients must not silently overwrite newer server state.

## Core schemas

### SubscriberSession
`session_id, subscriber_id, organisation_id, roles, entitlements, platform, policy_version, issued_at, expires_at, status`

### WorldNode
`node_id, parent_node_id, node_type, department_id, environment_id, spawn_anchor, visibility, required_entitlement, streaming_profile, version`

### Project
`project_id, owner_department, participating_departments, project_type, objectives, resource_scopes, shared_data_scopes, milestones, kpis, access_expiry, status, version`

### ResearchObject
`research_id, project_id, department_id, object_type, title, source_refs, evidence_state, data_refs, access_scope, provenance, version`

### DigitalTwin
`twin_id, asset_id, department_id, environment_id, project_id, object_type, operating_mode, state, telemetry_schema, interaction_schema, research_bindings, dashboard_bindings, safety_class, version`

### TelemetryRecord
`telemetry_id, twin_id, source_id, timestamp, mode, metric, value, unit, quality, sequence, schema_version`

### InteractionEvent
`event_id, actor_id, subscriber_id, department_id, project_id, twin_id, action, input_state, output_state, telemetry_refs, research_refs, timestamp, audit_status`

### AssetRecord
`asset_id, package_id, asset_class, source, creator, licence, provenance, evidence_state, poly_budget, texture_budget, lod_set, dependencies, access_scope, version`

## API resource model
Logical endpoints:
- `/v1/session`
- `/v1/world/nodes`
- `/v1/projects`
- `/v1/research`
- `/v1/twins`
- `/v1/telemetry`
- `/v1/events`
- `/v1/assets`
- `/v1/sync`

The exact transport/framework remains implementation-neutral.

## Access enforcement
Every protected API operation evaluates:
`IDENTITY → ORGANISATION → DEPARTMENT → PROJECT → RESOURCE`

The server/API layer is authoritative. Client-side hiding is UX optimisation, not security.

Required controls:
- deny by default;
- least privilege;
- explicit cross-department scope;
- expiry of temporary access;
- audit protected reads/writes;
- prevent enumeration of restricted IDs;
- filter search/retrieval before response generation.

## Persistent project state
Project state supports:
- current milestone;
- completed/failed tasks;
- experiment state;
- measurements;
- attached research objects;
- digital-twin state snapshots;
- authorised team members;
- approvals;
- audit references.

State transitions are versioned and idempotent where possible.

## Synchronisation model
Clients maintain:
- `sync_cursor`
- `last_server_version`
- `pending_events`
- `local_changes`
- `conflicts`

Flow:
`PULL AUTHORISED DELTA → APPLY → PUSH LOCAL EVENTS/CHANGES → CONFLICT CHECK → ACK → ADVANCE CURSOR`

Offline clients may queue permitted research events. Protected data must not be expanded merely because the client is offline.

## Conflict handling
Conflict classes:
- stale object version;
- expired entitlement;
- project scope changed;
- research object updated;
- twin state changed;
- asset licence/status changed.

Default policy:
1. reject unsafe overwrite;
2. retain local change;
3. fetch current authorised state;
4. present/perform deterministic merge where permitted;
5. audit resolution.

## Telemetry persistence
Telemetry may be high-volume and should be separable from durable research records.

Research records store selected/validated measurements and references; telemetry storage may retain raw streams according to project retention policy.

No inferred or cached value may be stored as live measurement without its source/mode metadata.

## Versioning
Schema versions use:
`MAJOR.MINOR`

Rules:
- MAJOR: incompatible contract change;
- MINOR: backward-compatible field/addition;
- deprecated fields retain migration guidance;
- clients declare supported schema versions.

## Security and privacy boundaries
Store only data required by the world/application. Subscriber identity and private organisation information must not be exposed to unrelated departments. Audit logs are access-controlled and retained according to policy.

## Android/Desktop persistence
Android:
- scoped cache;
- encrypted local storage where implemented;
- queued authorised events;
- bandwidth-aware delta sync.

Desktop:
- larger cache;
- richer project/twin state;
- same server-side permissions.

Both clients must consume the same logical contracts.

## Evidence/provenance
Research and cultural objects retain evidence state and source provenance through API transformations. API serialisation must not drop these fields.

Supported states include:
- DOCUMENTED
- RECONSTRUCTED
- EXPERIMENTAL
- HYPOTHESIS
- SPECULATIVE
- CREATIVE INTERPRETATION
- REFERENCE ONLY

## Acceptance tests
| Test | Expected |
|---|---|
| Valid authorised read | resource returned |
| Unauthorised read | denied without restricted enumeration |
| Cross-department read | only explicit shared scope |
| Stale update | rejected/merged under policy |
| Expired entitlement | write/read blocked |
| Offline event | queued only if authorised |
| Sync conflict | preserved and audited |
| Telemetry mode | source/mode/unit retained |
| Research evidence state | preserved |
| Asset licence change | affected runtime access re-evaluated |
| Client schema mismatch | controlled compatibility response |
| Duplicate event | idempotent handling where supported |

## Package additions
`WORLD-SERVICES/`
- `schemas/`
- `api-contracts/`
- `migrations/`
- `sync/`
- `persistence/`
- `tests/`

## Acceptance criteria
1. Gates 01–05 have a common versioned data contract.
2. Protected resources are authorised server-side before response.
3. Project state persists independently from scene presentation.
4. Offline synchronisation cannot bypass entitlement boundaries.
5. Telemetry and validated research measurements remain distinguishable.
6. Evidence/provenance metadata survives API and persistence transformations.
7. Schema evolution and conflict handling are explicit.
8. Android and desktop use the same logical contracts.
9. No production backend deployment is claimed by this specification.

## Next gate
**Gate 07 — Runtime package/build matrix**, mapping World Core, department, environment, character, twin, research and platform packages into reproducible Windows/Android build profiles.
