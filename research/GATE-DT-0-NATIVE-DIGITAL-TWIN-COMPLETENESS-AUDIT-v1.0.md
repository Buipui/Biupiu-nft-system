# GATE DT-0 — Native Digital Twin Completeness Audit v1.0

Date: 21 September 2026
Repository: Buipui/Biupiu-nft-system
Scope: native Digital Twin implementation, dependencies, tests, integration and verification boundary.

## Executive result

The Digital Twin is a substantial native repository implementation, not a specification-only concept. The canonical TypeScript core, DMS boundary, evidence-state rules, evidence validation tooling, schemas, domain integration records and rendering adapters exist in the repository.

Runtime verification is not established by repository inspection alone. The repository currently has no recorded GitHub Actions run/status for the audited latest commit, and physical telemetry, HIL, UE5 runtime and production actuation remain open.

## Completeness matrix

| Layer | Classification | Evidence |
|---|---|---|
| Canonical twin identity/model contract | NATIVE CODED | packages/biupiu-rnd-os/src/digital-twin.ts |
| Twin event/provenance contract | NATIVE CODED | digital-twin.ts |
| T0-T9 sequential promotion | NATIVE CODED + TESTS | digital-twin.ts + digital-twin.test.ts |
| DMS site/asset scope and route | NATIVE CODED + TESTS | src/dms.ts + digital-twin.test.ts |
| Governed actuation boundary | NATIVE CODED | digital-twin.ts |
| AAS-style / NGSI-LD-style mappings | NATIVE CODED | digital-twin.ts |
| DMS adapter boundary | NATIVE CODED / INTEGRATED | DIGITAL-TWIN-DMS-ADAPTER-v1.0.md |
| Authenticated transport contract | NATIVE CODED / CONTRACT | DMS-TRANSPORT-GATE-v1.0.md |
| Live DMS transport | OPEN | runtime endpoint and Site Node connectivity not evidenced |
| Evidence-state engine | NATIVE CODED + TESTS | simulators/biupiu_evidence_state_engine_v0_1.py + tests |
| PROP-15/18 data validation | NATIVE CODED + CI DEFINED | dataset validator + prop18 workflow |
| Calibration schema / BM-11 | NATIVE SCHEMA / INTEGRATION | BIUPIU-DIGITAL-TWIN-CALIBRATION-SCHEMA-v1.0.json |
| Bio-composite/material twin | ARCHITECTURE + SIMULATION INTEGRATION | BIUPIU-BIO-COMPOSITE-DIGITAL-TWIN-v1.0.md |
| AI/math integration | CONTRACT / INTEGRATION | codex/ai/MATH-INTEGRATION-CONTRACT.md |
| Domain twins | MIXED DEPTH | microturbine, mobility, farming, materials and other adapters vary by implementation |
| Blender binding | ADAPTER CONTRACT | packages/biupiu-blender/README.md |
| UE5 binding | ADAPTER / WORKSTATION DEPENDENT | software/unreal/README.md |
| UE5 runtime | OPEN | workstation/runtime evidence required |
| Physical telemetry | OPEN | no physical-host evidence in repository inspection |
| HIL / physical actuation | OPEN | no execution evidence established |
| Production qualification | OPEN | requires real validation/qualification evidence |

## CI repair executed

The Digital Twin contract workflow previously checked file presence, JSON parsing and JavaScript syntax only; it did not compile the Digital Twin TypeScript source or execute its contract tests.

The workflow was repaired to:
1. type-check the Digital Twin/DMS/test TypeScript surface;
2. execute digital-twin.test.ts through a TypeScript runtime;
3. retain the required contract-file checks.

Repair commit: db2035ca7148814ad1d204637586fe793d48b565.

## Verification boundary

Repository implementation evidence: ESTABLISHED.

GitHub Actions execution for the audited latest repository state: NOT ESTABLISHED.

Physical sensor/device evidence: NOT ESTABLISHED.

UE5/Visual Studio runtime: NOT ESTABLISHED.

Production actuation: NOT ESTABLISHED.

No runtime or physical claim is promoted merely because source code or workflow definitions exist.

## Next gate

DT-1 — Execute the repaired CI contract suite and then connect the Digital Twin adapter to a controlled authenticated DMS/Site Node runtime test.

Acceptance:
- TypeScript compilation PASS
- Digital Twin contract tests PASS
- evidence regression tests PASS
- DMS transport integration PASS
- deterministic event/replay behaviour PASS
- no evidence-state promotion bypass
- runtime evidence recorded before any gate is marked VERIFIED