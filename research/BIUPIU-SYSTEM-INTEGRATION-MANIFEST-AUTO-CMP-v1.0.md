# Biupiu Systems Integration Manifest — Automotive / Composites v1.0

**Date:** 20 September 2026  
**Priority:** HIGH  
**Status:** Integration contract defined; runtime wiring and CI validation pending

## Canonical integration chain

`World Asset ID → Environment Manifest → Department Adapter → Material/Powertrain Simulator → Telemetry → Digital Twin → Validation → Promotion`

## Connected departments

- `AUTO`: donor vehicles, packaging, drivetrain, thermal and vehicle-level studies
- `COMPOSITES`: flax, hemp, hybrid laminates, sandwich panels and damage modes
- `BIO-RESINS`: PFA/furan, EVO-derived epoxy, bio-epoxy, cure and ageing data
- `TEXTILES`: woven/nonwoven reinforcement, prepreg architectures and textile laminates
- `ADV-MFG`: layup, infusion, compression moulding, curing, inspection and traceability
- `PHYS-SYS`: units, mechanics, thermal, vibration and uncertainty contracts
- `COMPUTE`: numerical kernels, parameter sweeps and reproducible runs
- `AI`: proposal and analysis layer only; not authoritative physical state
- `ROBOTICS`: future manufacturing cell, inspection and handling adapters
- `WORLD`: common environment, lighting, materials, weather and asset context

## System ownership rules

1. The Biupiu OS simulation kernel owns authoritative simulation state.
2. Department adapters translate domain-specific inputs into the shared schema.
3. AI may propose parameters, designs or experiments but cannot silently alter authoritative state.
4. Every material, engine, motor, donor vehicle and test result receives a provenance record.
5. Safety-critical components remain blocked from promotion until physical evidence and independent review exist.
6. External simulators execute in isolated adapters with explicit licensing, security and reproducibility checks.

## Initial asset IDs

- `BPU-CMP-DAMP-001` — flax versus carbon damping dataset
- `BPU-CMP-DAMAGE-001` — microcracking and delamination evidence matrix
- `BPU-AUTO-PANELS-001` — non-structural lightweight body-panel family
- `BPU-AUTO-HYPER-001` — dual inboard axial-flux front-drive concept
- `BPU-AUTO-EXPEDITION-001` — diesel P2 hybrid concept
- `BPU-AUTO-RESIN-001` — prepreg, resin and adhesive qualification route

## Shared minimum data contract

```yaml
asset_id: required
revision: required
source_provenance: required
evidence_class: established|supported_research|plausible_model|unresolved
units: SI
inputs: versioned
assumptions: explicit
boundary_conditions: explicit
solver_version: required
uncertainty: required
validation_status: untested|screening|correlated|independently_reviewed
promotion_status: research_only|prototype_candidate|engineering_candidate|released
```

## Integration stages

### Stage A — schema and provenance

- [x] Define asset IDs and evidence classes
- [x] Define shared integration chain
- [x] Define safety and authority boundaries
- [ ] Implement machine-readable schemas
- [ ] Add automated schema/unit checks

### Stage B — analytical workshop integration

- [x] Existing CLT and cure prototype identified
- [ ] Add mass, centre-of-gravity and packaging inputs
- [ ] Add motor torque-speed and thermal duty-cycle interfaces
- [ ] Add diesel/P2 driveline torque and torsional vibration interface
- [ ] Add moisture, damping and ageing modifiers
- [ ] Add uncertainty and sensitivity runner

### Stage C — digital twin and validation

- [ ] Connect to OS-SIM digital-twin bridge
- [ ] Add deterministic replay and telemetry contract
- [ ] Add published-data benchmark fixtures
- [ ] Add measured coupon data ingestion
- [ ] Add report and JSON export
- [ ] Independent technical review

## Current promotion rule

No automotive component is promoted beyond `research_only` without traceable inputs, validated calculations, test evidence, uncertainty reporting and documented engineering review.
