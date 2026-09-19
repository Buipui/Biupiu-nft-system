# Biupiu Farming Simulator Resource Registry v1.0

**Date:** 19 September 2026  
**Purpose:** Research and integration registry for the Biupiu Smart Farming System and Biupiu World farming simulation layer.

## 1. Integration principle

Farming Simulator is treated as an **external reference/simulation adapter**, not as the Biupiu World core engine. Biupiu owns its own simulation schemas, world assets, physics abstractions and provenance records.

External resources are indexed rather than copied. Code or assets may only be incorporated when their licence permits the intended use and the dependency has passed the Biupiu provenance/security gate.

## 2. GitHub resource classes

### FS25 tooling and development
- **VertexDezign/FSTools** — Linux command-line helpers for packing, deploying, launching and debugging FS25 mods. Useful as a reference for the Biupiu farming build/test workflow.
- **GtX-Andy/FS25_EasyDevelopmentControls** — development/content-testing controls. Useful for test-scenario design; repository explicitly restricts copying/modification, so treat as reference only.
- **w33zl/FS25_DevTools** — Lua/object inspection and developer workflow reference.
- **w33zl/FS25_PowerTools** — development/content-authoring workflow reference.
- **FSGModding/FS25-GE10-Scripts-Modding-Tools** — Giants Editor 10 mapping/foliage/spline conversion references.

### Automation, telemetry and digital-twin bridge
- **getflowkits/fs25-farmhand-mod** — MIT-licensed FS25 companion concept exposing farm state and accepting ordinary in-game actions. High-value reference for a controlled simulator-to-Biupiu telemetry/action adapter.
- **VertexDezign/VDTelemetry** — FS25 telemetry pipeline with JSON state export and a live dashboard architecture. High-value reference for telemetry schemas and dashboard design.
- **Courseplay/Courseplay_FS25** — mature open-source automation/reference project for field operations. Use as behavioural/reference input; do not assume its licence permits arbitrary code reuse without checking the repository licence.
- **AndrewMommers/FS25-John-Deere-Precision-Ag-Suite** — MIT-licensed planning/reference architecture for guidance, field passes, telemetry and operator UI.
- **Bones50/FS25-Distribution-Redux** — demand-driven logistics/distribution reference for production, storage, livestock and material flows.

### Management and realism references
- **Callum-Mason/FS25-Farm-Managment-System** — farm-management UI concepts: field state, crop stages, fertiliser, crop rotation, livestock and finance.
- **exekx/FS25_RealisticHarvesting** — harvesting telemetry, machine-load and operational realism reference; treat implementation as external until licence compatibility is verified.
- **HLLMR/silo** — MIT-licensed mod-library management, integrity, conflict detection and reversible loadout concepts.

## 3. Open-book / open-access research layer

### Precision agriculture technology
**Qin Zhang, Precision Agriculture Technology for Crop Farming (2016)** — open-access edition indexed through Open Library/OAPEN. Relevant topics: sensing, data handling, crop modelling, production control, intelligent machinery and field robots.

### Precision-agriculture modelling
**Precision Agriculture: Modelling (2023)** — Springer reference covering crop/soil monitoring and modelling for decision support.

### Precision agriculture for sustainability
**Precision agriculture for sustainability: Second Edition (2026)** — current reference covering proximal soil/crop sensing, remote sensing, UAVs, multisensor fusion, site-specific irrigation and AI/data methods. Some chapters are open access; full book access varies by chapter/institution.

### Precision irrigation
**Modelling impacts of precision irrigation on crop yield and in-field water management** — open-access research reference for crop/water response modelling and precision irrigation.

### AI + drones
**Integrating machine learning and drone technology for precision agriculture (2026)** — open-access research reference combining soil sensors, local weather forecasting, ML irrigation prediction and autonomous drone application.

## 4. Biupiu translation layer

Translate the external simulator/reference material into Biupiu-native modules:

1. **FIELD-SIM** — field geometry, crop lifecycle, soil state and operations.
2. **WATER-SIM** — rainfall, storage, irrigation, infiltration, water demand and losses.
3. **CROP-SIM** — crop phenology, growth, yield, stress and rotation.
4. **SOIL-SIM** — fertility, organic matter, moisture, erosion and regeneration.
5. **MACHINE-SIM** — vehicle/implement state, energy/fuel, work rate and machine constraints.
6. **ROBOTICS-SIM** — autonomous guidance, field coverage, sensing and task planning.
7. **TELEMETRY-BRIDGE** — simulator state -> JSON/schema -> Biupiu Digital Twin.
8. **FARM-ECON** — input costs, labour, energy, yield, storage, processing and virtual trade.
9. **WORLD-ADAPTER** — converts validated simulation state into Biupiu World gameplay/learning scenarios.
10. **PROVENANCE** — source, licence, model version, assumptions, validation state and derivative status.

## 5. Biupiu World use

The farming simulator layer must support:
- regenerative agriculture;
- Waru Waru and terracing scenarios;
- water harvesting and irrigation experiments;
- greenhouse/sensor experiments;
- crop rotation and soil restoration;
- machinery and robotics testing;
- farm logistics and storage;
- historical civilisation farming scenarios;
- virtual economic experiments;
- measurable scenario comparison.

## 6. Licence boundary

**GREEN:** permissive licence confirmed and intended use compatible.  
**YELLOW:** useful reference, but licence/redistribution scope requires review.  
**RED:** proprietary/restricted asset or unclear rights — do not copy or redistribute.

Third-party Farming Simulator code/assets are not automatically Biupiu assets.

## 7. Status

**FARM-SIM-01: EXECUTED — external resources discovered, classified and mapped into the Biupiu Smart Farming + World Digital Twin architecture.**

Runtime integration remains a separate host-validation gate; no live Farming Simulator execution is claimed from repository indexing alone.
