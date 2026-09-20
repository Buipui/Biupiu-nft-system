# Vehicle Mass & Clearance Gate 04 — v1.0

**Date:** 20 September 2026
**Status:** EXECUTED — preliminary configuration and calculation framework; physical/CAD validation OPEN

## Working configurations

### Hypercar
**Working donor baseline:** first-generation Audi R8 V8 ASF platform.

Audi identifies the first-generation production R8 as using a 4.2 L V8 FSI mounted behind the passenger compartment, with the original version producing 420 PS and later 430 PS. Audi describes the R8 body as an Audi Space Frame (ASF). The R8 platform has a 2,650 mm wheelbase; the published R8 dimensions document for a later V10 performance body gives 4,429 mm overall length, so that length is retained as a body-envelope reference only and is not assigned to the first-generation V8 without model-year confirmation.

**Status:** donor family selected for controlled study; exact year/body/gearbox and structural condition remain OPEN.

### Overlander
**Working chassis baseline:** IVECO Daily 4x4, 4,175 mm wheelbase, 7,000 kg GVM configuration.

IVECO's current material lists 4,175 mm wheelbase, 7,000 kg GVM and 10,500 kg GCM for relevant configurations. The current published 3.0 L engine is rated at 132 kW and 430 Nm. Payload is configuration/body dependent.

**Status:** baseline configuration selected for calculation; exact chassis-cab, axle ratings, body and equipment remain OPEN.

## Source-backed dimensional anchors

| Input | Value | Evidence |
|---|---:|---|
| R8 wheelbase | 2,650 mm | Audi |
| R8 overall length reference | 4,429 mm | Audi later R8 body document; envelope reference only |
| R8 first-gen V8 | 4.2 L, 420 PS initially / 430 PS later | Audi |
| Daily 4x4 wheelbase | 4,175 mm | IVECO |
| Daily 4x4 GVM | 7,000 kg | IVECO |
| Daily 4x4 GCM | 10,500 kg | IVECO |
| Daily 4x4 engine | 3.0 L, 132 kW / 430 Nm | IVECO |
| YASA 750R mass | 37 kg each | YASA datasheet |
| Two YASA 750R motor mass | 74 kg | Calculated from published 37 kg each |
| Two YASA 750R peak power | 400 kW nominal | Calculated from published 200 kW each; not vehicle output |

## First-order axle-load calculation

For a vehicle with wheelbase L, total mass M, and centre of gravity located x from the front axle:

- Front axle load = M × g × (L − x) / L
- Rear axle load = M × g × x / L

For mass budgeting in kilograms-force-equivalent terms:

- Front mass share = M × (L − x) / L
- Rear mass share = M × x / L

No numerical axle-load result is promoted until actual component masses and CG locations are measured or sourced.

## Packaging / clearance framework

Every major subsystem receives:
X_min/X_max, Y_min/Y_max, Z_min/Z_max, mass, CG, service envelope, thermal envelope, attachment points, allowable movement and uncertainty.

Required envelopes:
1. Engine and exhaust/after-treatment.
2. Transmission/transaxle and shafts.
3. Front YASA motor(s), inverter(s), half-shafts and steering clearance.
4. Battery enclosure and HV service disconnects.
5. Cooling radiators, pumps, hoses and airflow paths.
6. Suspension travel and steering lock.
7. Brake system and wheel/tire envelope.
8. Composite body panels and bonded interfaces.
9. Crash structures and occupant cell.
10. Service/removal paths.

## Conservative mass ledger

No mass is credited as a composite saving until a component-level replacement bill of materials exists.

For the hypercar:
M_total = donor retained structure + powertrain + electrical + battery + cooling + suspension/brakes + wheels/tyres + body/composites + glazing + interior + safety + fluids + fasteners + wiring + margin

For the overlander:
M_total = chassis/cab + engine/powertrain + body/subframe + suspension + wheels/tyres + fuel + battery/HV system + water + auxiliary power + recovery equipment + interior + payload + safety + margin

## Gate 04 result

- **Executed:** exact working donor families/configurations established for controlled calculation.
- **Executed:** source-backed wheelbase/GVM/GCM/power and motor-mass anchors captured.
- **Executed:** first-order axle-load equations and clearance-envelope protocol registered.
- **Open:** measured component masses, exact CG, axle ratings, CAD geometry, suspension travel, structural load paths, crash analysis, thermal model and physical inspection.
- **Not verified:** sub-1,000 kg hypercar target; any conversion's crashworthiness; composite structural equivalence; final drivetrain durability.

## Gate 05 entry

Acquire exact donor-year/model documentation and component-level measurements/CAD. Populate the mass ledger, calculate CG/axle loads, then run first-order longitudinal/lateral load cases before any FEA promotion.
