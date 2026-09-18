# Biupiu World — 3D Gate 05: Cross-Department Campus & Shared-Service Layer v1.0

## Status
Specification committed for implementation. This gate defines world-level navigation, identity, shared services, controlled cross-department projects and asset streaming. It does not claim that production runtime services or binary assets have been deployed.

## Objective
Connect department environments into one coherent Biupiu World campus while preserving the department firewall established in Gates 01–04.

## Campus architecture
`WORLD CORE → IDENTITY → NAVIGATION → DEPARTMENT GATEWAY → ENVIRONMENT → WORKSHOP/LAB → DIGITAL TWIN`

Shared services sit below the department layer:
`IDENTITY | ENTITLEMENTS | NAVIGATION | ASSET STREAMING | RESEARCH INDEX | TELEMETRY ROUTER | AUDIT | NOTIFICATIONS`

## Identity and session
Every world session resolves:
- `actor_id`
- `subscriber_id`
- `organisation_id`
- `roles`
- `department_entitlements`
- `project_entitlements`
- `session_id`
- `client_platform`
- `access_policy_version`

Session rules:
1. authenticate before protected world entry;
2. resolve entitlements before loading protected resources;
3. issue temporary interaction scope where required;
4. revoke temporary scope on exit/session expiry;
5. record security-sensitive access events.

## World navigation
Navigation nodes use:
- `node_id`
- `parent_node_id`
- `node_type`
- `department_id`
- `environment_id`
- `required_entitlement`
- `visibility`
- `spawn_anchor`
- `streaming_profile`

Node types:
- MAIN_HUB
- DEPARTMENT_GATE
- ENVIRONMENT
- BUILDING
- WORKSHOP
- LAB
- RESEARCH_ARCHIVE
- SHOWCASE
- NEW_AGE_THEORY

New Age Theory remains a clearly separated world layer and inherits evidence-state controls.

## Shared campus services

### Navigation service
Provides authorised destination discovery, spawn anchors, route metadata and accessibility routes.

### Identity service
Maintains session identity and role/entitlement context. It must not expose private subscriber information to unrelated departments.

### Asset streaming service
Loads only assets required by:
- current world zone;
- authorised department;
- current interaction;
- client performance tier.

Protected assets must not be downloaded merely because a user can see an adjacent environment.

### Research index service
Routes search/retrieval through department and project permissions before returning research objects.

### Twin/telemetry router
Routes authorised digital-twin events from Gate 04 to the correct department/project context. Cross-department telemetry requires explicit shared entitlement.

### Audit service
Records:
- login/session events;
- protected resource access;
- entitlement decisions;
- cross-department requests;
- object interactions;
- research writes;
- exports;
- permission failures.

### Notification service
Notifications inherit the same department/project scope as their source event.

## Controlled cross-department projects
A project may involve multiple departments without granting unrestricted access.

Project record:
- `project_id`
- `owner_department`
- `participating_departments`
- `resource_scopes`
- `shared_data_scopes`
- `data_retention`
- `access_expiry`
- `audit_policy`

Example:
`FARMING + MATERIALS` can share a regenerative composite irrigation component project while unrelated metallurgy or biotech records remain inaccessible.

## Shared-resource model
World-level shared resources:
- Main Hub navigation;
- public/common educational signage;
- approved shared utilities;
- universal accessibility settings;
- public showcase assets.

Department-protected resources:
- research records;
- specialist tools;
- digital twins;
- private projects;
- restricted datasets;
- department AI retrieval context.

## Asset streaming tiers
- L0: Main Hub/common shell
- L1: current department
- L2: current environment
- L3: current workshop/lab
- L4: active twin/interaction objects

Unload rules:
- unload protected L2–L4 assets when leaving scope unless required by an explicitly authorised shared project;
- cached assets retain access metadata;
- expired entitlements invalidate protected cached content.

## Cross-platform strategy

### Desktop/Windows
Supports richer scene density, multi-panel dashboards, higher LOD and simultaneous authorised twin views.

### Android
Uses scoped streaming, reduced scene density, LOD2/LOD3 assets where appropriate, simplified dashboards and aggressive unloading.

Both platforms use the same logical access and research contracts.

## Cross-department workflow
`DISCOVER → REQUEST SHARE → AUTHORISE → LOAD SCOPED ASSETS → INTERACT → WRITE RESEARCH EVENT → AUDIT → REVOKE/EXPIRE`

No cross-department access is inferred from proximity, visual visibility or possession of another department's avatar.

## Accessibility
Campus services should support:
- alternate navigation routes;
- readable interaction prompts;
- scalable UI;
- reduced visual effects;
- simplified interaction mode;
- keyboard/controller/touch mappings where supported;
- clear evidence-state labels.

## Evidence-state integration
Every research/cultural/speculative object retains:
- DOCUMENTED
- RECONSTRUCTED
- EXPERIMENTAL
- HYPOTHESIS
- SPECULATIVE
- CREATIVE INTERPRETATION
- REFERENCE ONLY

World presentation must not convert a speculative object into a documented historical claim.

## Failure and offline handling
If a shared service is unavailable:
- retain only authorised cached metadata;
- enter OFFLINE mode;
- never fabricate live telemetry;
- preserve queued local research events only when policy permits;
- mark synchronisation state explicitly.

## Security tests
| Test | Expected |
|---|---|
| Enter protected department without entitlement | denied |
| View adjacent protected asset | metadata/asset withheld |
| Search restricted research | no restricted result |
| Cross-department project | only declared shared scope |
| Expired project access | access revoked |
| Cached asset after expiry | protected access blocked |
| Notification from restricted event | not delivered |
| Cross-department telemetry | blocked without shared scope |
| Offline mode | no LIVE status |
| Audit trail | access decision recorded |

## Performance acceptance
- Main Hub remains lightweight.
- Only scoped assets are streamed.
- Unused department content is not loaded on mobile.
- Twin telemetry is subscribed to only while authorised/needed.
- Asset LOD follows client tier.
- Cross-department projects do not force unrelated department packages into memory.

## Acceptance criteria
1. One world navigation graph spans all authorised departments.
2. Identity and entitlements are resolved before protected resource loading.
3. Cross-department projects use explicit scopes.
4. Asset streaming respects department/project boundaries.
5. Research search, notifications and telemetry inherit the same firewall.
6. Desktop and Android use the same logical permissions.
7. Offline mode is explicit and never masquerades as live.
8. Audit events cover access and cross-department operations.
9. Evidence-state labels remain intact throughout the world.
10. No production runtime or live service deployment is claimed by this specification.

## Package additions
`WORLD-SERVICES/`
- `identity/`
- `navigation/`
- `entitlements/`
- `asset-streaming/`
- `research-index/`
- `twin-router/`
- `audit/`
- `notifications/`
- `accessibility/`
- `tests/`

## Next gate
**Gate 06 — World data/API contract and persistent project state**, defining versioned schemas for navigation, subscribers, projects, research objects, digital twins, telemetry, events and synchronisation.
