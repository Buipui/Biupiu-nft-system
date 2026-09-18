# SF-51 — AUTOMOTIVE SHOWROOM DATA CONTRACT & RUNTIME INTEGRATION

## Purpose
Define the stable data contract connecting the AeroBlade GT showroom asset to Biupiu World, the Digital Lab, Academy, Research Library and Product Studio.

## Stable identity
- scene_id: AUTO-01
- project_id: BPU-AUTO-SPORT-001
- hero_asset_id: BPU-AUTO-SPORT-001
- department_id: D-AUTO
- district_id: advanced-mobility-district
- claim_class: CONCEPT

## Runtime context
The showroom consumes the existing world session context: user_id, environment_id, facility_id, avatar_id, property_id, lesson_id and experiment_id. Automotive interactions add scene_id, vehicle_id and display_zone_id.

## Display zones
AUTO-EXT exterior hero; AUTO-PWR powertrain; AUTO-EV electric traction; AUTO-ENG energy generation; AUTO-AERO aerodynamics; AUTO-MAT materials; AUTO-LAB Digital Lab; AUTO-ACADEMY Academy; AUTO-STUDIO Product Studio.

## Interaction contract
Each hotspot resolves to a stable ID and may expose: title, short_description, claim_class, research_link, lab_link, lesson_link, provenance_link and media_asset_ids.

## Architecture data
The data model records the rear/mid turbocharged biodiesel-compatible engine as mechanical rear-wheel propulsion with electrical-generation support; individual electric traction motors at each wheel; front motors as torque-vectoring/AWD research; rear electric assistance; regenerative braking; and Biupiu microturbine auxiliary electrical generation to the HV system.

## Material data
Record HempCarbon/advanced-composite zones and Biupiu resin architected/metasurface surfaces as research concepts. Metasurface terminology does not imply demonstrated electromagnetic performance.

## Claims and rights
Every visible asset requires provenance, rights_status and claim_class. Blocked claims remain: validated stealth, invisibility, radar-proof operation, certified performance, road legality, production availability and measured performance.

## Runtime states
PARKED_SHOWCASE → INTERACTIVE_DISPLAY → RESEARCH_DEMO → FIELD_SIMULATION/FUTURE_DRIVEABLE only when separately approved and technically implemented.

## Mobile fallback
If interactive 3D is unavailable, serve optimized still render plus hotspot cards and links to the Digital Lab/Academy.

## Integration state
DATA_CONTRACT_READY / RUNTIME_MAPPING_READY / IMPLEMENTATION_PENDING.

## Next gate
SF-52 — Automotive showroom implementation scaffold and cross-link validation.
