# Biupiu Multilingual Digital Twin Architecture Research v1.0

**Date:** 19 September 2026
**Status:** Research/index gate completed

## Search lanes

Multilingual discovery was run across German, Japanese, Chinese, Korean and Russian terminology for digital twins, Industry 4.0, semantic interoperability, open-source architectures and simulation. Results were treated as discovery leads; implementation candidates require repository-level licence/security/compatibility review.

## Architecture upgrades selected

### 1. Semantic context layer
Adopt an NGSI-LD-style context boundary so twins can exchange typed entities, properties and relationships without coupling departments to one database schema.

### 2. Asset semantic layer
Adopt an AAS-compatible reference boundary so industrial assets can expose machine-readable identity, semantic identifiers and submodel references without making the Biupiu runtime dependent on one vendor.

### 3. Twin lifecycle / state separation
Keep the existing T0-T9 evidence ladder, while separately tracking operational state, model version, evidence state, provenance, simulation state, and policy/authorisation state.

### 4. Event-driven integration
Prefer immutable event records and projections between DMS, enterprise modules and twins. Department services must not directly mutate another department's storage.

### 5. Simulation-to-action safety gate
Add a distinct actuation boundary. AI may recommend; simulation may test; policy decides whether an action is eligible; human approval remains mandatory where required.

### 6. Open simulation interfaces
Maintain adapter boundaries for FMI/OpenModelica, robotics simulators and 3D engines. No simulator becomes the authoritative enterprise state store.

### 7. Ontology-first enterprise graph
Treat departments, assets, projects, products, research, algorithms, treasury records and provenance as typed entities with explicit relationships.

## Implemented repository change

`packages/biupiu-rnd-os/src/digital-twin.ts` now includes context entities, ontology references, AAS-style asset references, governed actuation requests, simulation-reference requirements, confidence/evidence checks and human-approval checks.

No external source code was copied into the repository.

## Foreign-language research policy

Foreign-language repositories and papers are discovery sources. Before executable code is promoted:
`DISCOVER -> TRANSLATE/UNDERSTAND -> LICENCE -> SECURITY -> DEPENDENCY -> API COMPATIBILITY -> TEST -> INTEGRATE -> PROVENANCE`

Translation does not count as validation, and repeated claims across derivative sources do not count as independent evidence.

## Next runtime gates

CI compilation, unit tests, interoperability tests against actual NGSI-LD/AAS/FMI implementations, security review and live integration tests remain required before production promotion.