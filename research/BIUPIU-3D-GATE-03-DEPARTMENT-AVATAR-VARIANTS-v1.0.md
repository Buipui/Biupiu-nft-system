# Biupiu World — 3D Gate 03: Department Avatar Variants v1.0

## Status
Specification committed for modelling implementation. This gate defines the first four department-specific character packages and their workshop interaction contracts. It does not claim that binary 3D assets have been generated.

## Objective
Turn the shared Gate 02 character foundation into reusable specialist avatars for Farming, Metallurgy, Textiles, and Materials while preserving one common rig, access-control model, provenance system, and mobile optimisation path.

## Package map

### BPU-3D-FARMING-CHAR-01
Role: regenerative farming researcher/operator.
- Clothing: practical fieldwear with modular boots, gloves, hat/head covering, weather layer.
- Equipment slots: soil sampler, irrigation controller, crop inspection kit, field tablet.
- Environment bindings: farm plots, water systems, nursery, regenerative trial areas.
- Interactions: inspect soil, sample crop, sow, plant, water, harvest, inspect sensor, record trial.
- Data bindings: FieldRecord, CropRecord, SoilRecord, WaterRecord, SensorRecord, TrialRecord, YieldRecord.

### BPU-3D-METALLURGY-CHAR-01
Role: workshop metallurgist.
- Clothing: workshop PPE slot system with configurable protective equipment.
- Equipment slots: caliper/measurement tool, sample holder, furnace/forge interaction tool, material record tablet.
- Environment bindings: Smart Metal Workshop, furnace area, forge area, material testing station.
- Interactions: identify material, inspect sample, measure, load/unload simulated equipment, record heat-treatment run, log failure.
- Data bindings: MaterialRecord, AlloyRecord, HeatTreatmentRun, FurnaceRecord, ForgeRecord, TestRecord, Measurement, FailureRecord.
- Safety interactions are informational/simulation controls, not certification.

### BPU-3D-TEXTILES-CHAR-01
Role: fibre and textile researcher/artisan.
- Clothing: modular workshop garments with culturally configurable but provenance-tagged variants.
- Equipment slots: fibre sample tray, spindle, loom interaction controls, dye/sample tools.
- Environment bindings: Southern African Fibre & Weaving House, West African Textile Studio, North African/Mediterranean Loom House, South Asian Textile Workshop, East Asian Fibre & Silk House, Global Fibre Innovation Lab.
- Interactions: inspect fibre, spin, weave, dye, compare sample, catalogue textile, record process.
- Data bindings: FibreRecord, TextileRecord, ProcessRecord, ReferenceSource, ExperimentRecord.

### BPU-3D-MATERIALS-CHAR-01
Role: advanced materials researcher.
- Clothing: laboratory/workshop base with configurable protective equipment.
- Equipment slots: specimen tray, microscope/scan interface, composite layup tools, measurement tablet.
- Environment bindings: Southern African Materials & Earth Workshop, West African Furnace & Materials Heritage, North African/Mediterranean Materials House, South Asian Materials Workshop, East Asian Kiln & Materials Studio, Ancient Americas Materials Studio, Advanced Materials Laboratory.
- Interactions: inspect specimen, prepare sample, compare material, run simulated test, record measurement, review failure.
- Data bindings: MaterialRecord, CompositeRecord, TestRecord, Measurement, FailureRecord, ReferenceSource.

## Shared interaction contract
Every specialist avatar implements:
1. Spawn at department-approved anchor.
2. Resolve subscriber entitlement before accessing department objects.
3. Display only authorised tools and research data.
4. Enter inspection mode for research objects.
5. Trigger an auditable interaction event.
6. Write results to the relevant project/research record.
7. Exit workstation without retaining restricted object access.
8. Return to neutral avatar state when leaving the department.

## Visual provenance
- Original Biupiu assets: mark BIUPIU_ORIGINAL.
- Licensed/permissioned assets: record creator, licence and source.
- Public-domain assets: record source and verification.
- Reference-only assets: no redistribution.
- Cultural reconstructions and speculative environments require an evidence-state label.
- Mod/game assets require licence verification before integration.

## Shared rig strategy
All four specialist avatars target HUMANOID-BASE from Gate 02.
Specialist equipment is attachment-based rather than a duplicated body mesh.
Animation clips should be reusable wherever hand/prop contact points permit.
Department variants must not fork the base skeleton without an explicit compatibility decision.

## Mobile strategy
- LOD0: showcase.
- LOD1: desktop exploration.
- LOD2: Android exploration.
- LOD3: distant/crowd.
- Use shared texture atlases and material instances.
- Disable high-cost facial/cloth simulation by default on mobile.
- Prefer baked or simplified effects for workshop machinery.
- Keep specialist equipment modular so unused tools are not loaded.

## Test matrix
| Test | Farming | Metallurgy | Textiles | Materials |
|---|---|---|---|---|
| Spawn anchor | required | required | required | required |
| Entitlement check | required | required | required | required |
| Object inspection | required | required | required | required |
| Workstation interaction | required | required | required | required |
| Research record write | required | required | required | required |
| Restricted-resource rejection | required | required | required | required |
| Mobile LOD | required | required | required | required |
| Provenance check | required | required | required | required |

## Acceptance criteria
1. Four variants use the same humanoid retargeting foundation.
2. Each department has defined appearance, tools, environments, interactions, and data bindings.
3. Department permissions are enforced before tool/data access.
4. Cultural and mod-derived assets carry provenance/licence metadata.
5. Mobile variants can omit unused equipment and expensive effects.
6. Interaction events are auditable and linked to research records.
7. Restricted resources remain inaccessible after leaving a workstation.
8. No historical/speculative visual is presented as documentary fact solely by appearance.

## Next gate
**Gate 04 — Workshop interaction layer and digital-twin object binding**, connecting characters to live/simulated tools, machines, sensors, research records, and department dashboards.
