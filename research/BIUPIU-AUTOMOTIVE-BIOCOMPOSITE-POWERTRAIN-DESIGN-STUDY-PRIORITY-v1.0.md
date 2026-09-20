# Biupiu Automotive Bio-Composite & Hybrid Powertrain Design Study v1.0

**Date:** 20 September 2026  
**Priority:** HIGH — automotive body panels, lightweighting, textiles, composites, bio-resins and adhesives  
**Status:** Feasibility study / concept architecture; not a certified vehicle design

## Executive conclusion

The programme is technically plausible as a staged demonstrator programme, but not yet validated as a road-ready or race-ready vehicle. The near-term viable product path is non-crash-critical body panels, interior panels, acoustic/trim components, underbody shields and modular textile-composite products. Crash structures, suspension links, steering components, half-shafts, engine mounts and high-temperature powertrain-adjacent parts require dedicated material qualification and vehicle-level certification.

## Damping finding

The approximately 300% claim is supported for flax laminates in specific test conditions, not for every bio-composite. One study reports flax laminate damping coefficients approximately 200–283% above carbon in selected directions/frequency ranges; another reports roughly 2–3 times better low-frequency damping for flax-fibre polymer composites than carbon-fibre composites. Damping is frequency-, strain-, temperature-, architecture- and boundary-condition-dependent. A 2024 flax/carbon/PA11 hybrid study reported a damping factor 20% above pure carbon, demonstrating that hybrid performance varies by lay-up and test method.

## Micro-cracking and damage modes to track

Potential or documented damage mechanisms include matrix microcracking, fibre–matrix debonding, fibre pull-out, lumen-related porosity, fibre breakage, kink-band/micro-compressive damage, delamination, interlaminar shear failure, moisture-assisted interface degradation, thermal-mismatch cracking and fatigue accumulation. Hybrid flax/carbon laminates require special attention to inter-ply delamination and strain incompatibility. “Microcracking” must be defined by microscopy, CT, acoustic emission or other measurable criteria; it must not be inferred from a load curve alone.

## Hypercar concept study

### Engine-code correction

CCFA and CKDA are associated with the Volkswagen Group 4.2-litre V8 TDI diesel family, not a generic Audi 4.2-litre twin-turbo petrol engine. CCFA is associated with Audi Q7 applications, while CKDA is associated with the Volkswagen Touareg 4.2 TDI; exact turbo, emissions, ECU, transmission, cooling and mounting details must be confirmed from the specific donor VIN and engine data plate. The proposed architecture therefore requires an engine-selection gate before packaging.

### Proposed architecture

- Lightweight composite body panels and non-structural closures.
- Reinforced safety cell retained from a validated donor or newly engineered and certified structure.
- Two inboard axial-flux electric motors, nominally 200 kW each, driving the front wheels through independent reduction, differential/drive units and engineered half-shafts.
- The YASA unit identity, continuous/peak power, torque-speed envelope, cooling requirements, inverter compatibility, rotor containment, IP rating and packaging dimensions must be confirmed with the exact supplier model. “200 kW” alone is insufficient for shaft, bearing, thermal or traction calculations.
- Composite half-shafts are a high-risk subsystem: torsional fatigue, critical speed, impact damage, joint articulation, containment and fail-safe behaviour require dedicated testing. Initial demonstrators should use qualified metallic shafts or a certified hybrid shaft until composite shaft validation is complete.

### Hypercar test gates

1. Body-panel coupon and attachment testing.
2. Chassis torsional-rig model and physical correlation.
3. Motor torque-vectoring and traction simulation.
4. Half-shaft torsional and fatigue analysis with safety factors.
5. Thermal management for motors, inverters, brakes and engine bay.
6. FEA, modal analysis, crashworthiness review and regulatory pathway.

## Expedition vehicle concept study

### Candidate diesel comparison

- **Cummins 5.9 6BT:** simple mechanical-era architecture and strong aftermarket knowledge, but substantial mass and packaging burden. Biodiesel compatibility must be determined by exact year, injection-system components, seals, fuel quality and OEM guidance; do not assume B100 approval.
- **Mercedes OM606:** mechanically robust inline-six platform with a large tuning and conversion ecosystem, but donor condition, fuel-pump configuration, cooling, emissions compliance, transmission interface and biodiesel material compatibility require inspection and testing.

Cummins documentation states that approval depends on engine model/build date and fuel specification; B100 must meet ASTM D6751 and blends must meet applicable blend standards. HVO/renewable diesel is chemically distinct from FAME biodiesel and must be treated as a separate fuel case.

### P2 architecture

Proposed layout: diesel engine → clutch/disconnect or coupling → single BorgWarner MVH250 motor-generator → mechanical transmission → transfer case. Confirm the exact MVH250 variant, continuous/peak power, torque, speed, cooling, clutch/rotor inertia, control system, packaging envelope and transfer-case compatibility before selecting the donor. A P2 system can support launch assist, torque fill, regenerative braking, engine load shifting and exportable electrical power, but the transmission, torsional vibration, clutch control and thermal system are major integration risks.

### Expedition validation gates

1. Engine and fuel-system inspection with documented baseline compression, oil pressure, cooling and injection condition.
2. Fuel compatibility and elastomer/material test programme for B5/B20/B100 and HVO where relevant.
3. P2 torsional vibration and driveline shock model.
4. Motor-generator thermal duty cycle and regenerative braking limits.
5. Transfer-case, prop-shaft, differential and axle torque validation.
6. Water, dust, vibration, thermal cycling and serviceability testing.

## Donor/platform strategy

Use existing vehicles as rolling laboratories before creating a clean-sheet platform. Candidate categories:

- A longitudinal AWD performance donor with a documented safety cell and available front-drive packaging for the hypercar study.
- A ladder-frame 4x4 donor with a mechanically accessible transmission/transfer-case arrangement for the expedition P2 study.
- A common production hatchback/SUV or light commercial donor for body-panel, interior-panel, acoustic and textile-composite trials.

Selection criteria: local parts availability, donor documentation, wheelbase/track, legal registration path, crash structure, drivetrain layout, mass budget, cooling envelope, brake capacity, suspension loads, serviceability and total prototype cost. No donor is approved until a complete packaging and structural audit is completed.

## First-factory product launch sequence

### Phase 1 — lower-risk products

- Flax/hemp composite interior trim panels.
- Door cards, parcel shelves, console panels and acoustic panels.
- Non-structural bonnet/boot and service-access panels where thermal and impact requirements are met.
- Composite textile laminates, protective covers, luggage and expedition interior modules.
- Bio-resin adhesive and coating samples for controlled non-safety-critical applications.

### Phase 2 — engineering products

- Sandwich body panels with tested cores and attachment systems.
- Semi-structural panels with hybrid flax/carbon or flax/basalt reinforcement.
- Prepreg rolls, resin systems and bonded-joint kits with controlled batch records.
- Thermal and acoustic components near but not directly exposed to high-temperature powertrain zones.

### Phase 3 — high-risk automotive components

- Crash-relevant structures, suspension parts, steering parts, shafts and powertrain mounts only after formal engineering validation, destructive testing, regulatory review and independent sign-off.

## Workshop simulator requirements

The simulator shall contain: mass and centre-of-gravity model; laminate ABD matrices; modal and vibration model; torque-speed and efficiency maps; thermal balance; fatigue and duty-cycle estimates; moisture/ageing factors; uncertainty ranges; and a traceable comparison against conventional controls. Simulation outputs are screening estimates until calibrated using physical measurements.

## Priority research records

- `BPU-CMP-DAMP-001`: flax damping versus carbon under matched test conditions.
- `BPU-CMP-DAMAGE-001`: microcracking, debonding, delamination and fatigue evidence matrix.
- `BPU-AUTO-HYPER-001`: dual 200 kW inboard front e-axle concept.
- `BPU-AUTO-EXPEDITION-001`: diesel P2 hybrid concept.
- `BPU-AUTO-PANELS-001`: lightweight non-structural panel product family.
- `BPU-AUTO-RESIN-001`: prepreg, bio-resin and adhesive qualification route.

## Decision

Proceed as a staged research and demonstrator programme, prioritising body panels, textiles, bio-resins, adhesives and acoustic components. Do not release claims of roadworthiness, crashworthiness, shaft durability, emissions compliance or production viability until the required test gates are completed.
