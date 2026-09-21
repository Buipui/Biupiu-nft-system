# Vehicle Component Evidence Ledger — Gate 07 v1.0

**Date:** 21 September 2026  
**Status:** EXECUTED — Boxster 986 component-ledger framework established; measured/CAD integration OPEN

## Gate correction
The hypercar track uses the **Porsche Boxster Type 986**, not the Audi R8. The R8 baseline is superseded and must not re-enter the active model.

Porsche identifies the 986 as a mid-engine roadster. Porsche Club Europe provides model-year-specific unladen weights for 986 variants.

## Evidence classes
- **A — externally supported:** manufacturer, regulatory/technical document, or traceable authoritative source.
- **B — provisional:** engineering placeholder, derived calculation, or secondary source pending primary confirmation.
- **C — unknown:** required input not yet established.

No B/C value is promoted to verified design fact.

## 1. Hypercar — Porsche Boxster 986

### Source-backed vehicle anchors
| Parameter | Value | Class |
|---|---:|---|
| Architecture | Mid-engine roadster | A |
| Wheelbase | 2,415 mm | A |
| 986 standard, MY 1997–1999 | 1,250 kg DIN | A |
| 986 Boxster, MY 2000–2003 | 1,275 kg DIN | A |
| 986 Boxster S, MY 2000–2002 | 1,320 kg DIN | A |

These family values are not interchangeable across model years or derivatives.

### Proposed component ledger
| Component/system | Mass | Location / coordinate | Uncertainty | Evidence | State |
|---|---:|---|---|---|---|
| Boxster shell/body/retained structure | TBD | x/y/z from donor datum | High | C | OPEN |
| Original flat-six + ancillaries | TBD | rear-mid engine bay | High | C | OPEN |
| Original transmission/final drive | TBD | rear-mid | High | C | OPEN |
| Proposed replacement engine/powertrain | TBD | donor engine bay | High | C | OPEN |
| YASA 750R motor 1 | 37 kg catalog | proposed front axle zone | Low on catalog mass; high on installation | A/B | OPEN |
| YASA 750R motor 2 | 37 kg catalog | proposed front axle zone | Low on catalog mass; high on installation | A/B | OPEN |
| YASA motors combined | 74 kg | front axle zone | Installation TBD | A/B | OPEN |
| Inverters | TBD | front/rear service zone | High | C | OPEN |
| HV battery | TBD | low central zone proposed | High | C | OPEN |
| HV cabling/contactors/fusing/IMD | TBD | distributed | High | C | OPEN |
| Cooling system | TBD | front/side/rear radiator zones | High | C | OPEN |
| Composite body panels | TBD | body envelope | High | C | OPEN |
| Joints/adhesives/fasteners | TBD | distributed | High | C | OPEN |
| Brakes/steering/suspension | TBD | axle locations | High | C | OPEN |
| Wheels/tyres | TBD | four corners | Medium | C | OPEN |
| Interior/seat/restraints | TBD | cabin | High | C | OPEN |
| Crash/fire/safety hardware | TBD | cabin/structural zones | High | C | OPEN |
| Fluids | TBD | distributed | High | C | OPEN |
| Wiring/control electronics/sensors | TBD | distributed | High | C | OPEN |
| Engineering/service margin | TBD | distributed | High | C | OPEN |

Only the two 750R catalog masses are currently carried numerically for proposed conversion hardware. The 74 kg total excludes inverters, mounts, cooling, wiring and controls.

### First-order mass model
For component masses m_i and longitudinal coordinates x_i measured from the front axle:

M = sum(m_i)

x_CG = sum(m_i*x_i) / M

For wheelbase L = 2415 mm:

F_z = M*(L-x_CG)/L

R_z = M*x_CG/L

These equations prepare the CAE dataset; no final CG or axle load is claimed until the ledger is populated.

### Boundary sensitivity — illustrative 1,000 kg vehicle
| CG from front axle | Front share | Rear share |
|---:|---:|---:|
| 1,000 mm | 58.6% | 41.4% |
| 1,100 mm | 54.4% | 45.6% |
| 1,200 mm | 50.3% | 49.7% |
| 1,300 mm | 46.2% | 53.8% |
| 1,400 mm | 42.0% | 58.0% |

Sensitivity only, not a predicted Boxster result.

## 2. Overlander — IVECO Daily 4x4

The working baseline remains the 4,175 mm wheelbase / 7,000 kg GVM configuration.

| Component/system | Mass | Location / coordinate | Evidence | State |
|---|---:|---|---|---|
| Chassis/cab | TBD | x/y/z donor datum | A/B/C depending exact build | OPEN |
| Engine/ancillaries | TBD | front zone | C | OPEN |
| Transmission/transfer case | TBD | longitudinal | C | OPEN |
| Axles/differentials/shafts | TBD | axle locations | C | OPEN |
| Body/subframe | TBD | rear/body envelope | C | OPEN |
| Suspension/brakes/wheels | TBD | axle locations | C | OPEN |
| Hybrid motor/inverter | TBD | proposed P2 location | C | OPEN |
| HV battery | TBD | low central zone proposed | C | OPEN |
| Fuel/water/auxiliary power | TBD | distributed | C | OPEN |
| Recovery/off-grid equipment | TBD | body envelope | C | OPEN |
| Interior/payload | TBD | body envelope | C | OPEN |
| Safety/service margin | TBD | distributed | C | OPEN |

## 3. Exterminate / conflict reconciliation
1. R8 donor data is quarantined from the active hypercar model.
2. No R8 axle limits are transferred to the Boxster.
3. No Boxster component mass is invented to close the 1,000 kg target.
4. Published donor mass is not treated as conversion allowance.
5. Catalog motor mass is not treated as installed-system mass.
6. No FEA, crash, thermal or physical validation is claimed.
7. Exact Boxster derivative remains open.

## 4. CAE-ready input schema
Every future component record must contain: component_id, source, evidence_class, mass_kg, x_mm, y_mm, z_mm, uncertainty, configuration, measurement_method, confidence, validation_status.

Coordinate convention: x = longitudinal positive rearward from front axle datum; y = lateral positive toward vehicle right; z = vertical positive upward from defined chassis datum.

## Gate 07 result
**EXECUTED / REGISTERED:** Boxster 986 is the active hypercar donor family; component-level evidence ledger, evidence classes, coordinate convention, mass/CG equations and sensitivity framework are registered.

**VERIFICATION STATUS:** vehicle-conversion model not yet verified.

**OPEN:** exact donor VIN/year/derivative; measured donor mass; component masses; component CG coordinates; CAD geometry; structural load paths; battery/inverter selection; thermal system; suspension/brake loads; crash structure; CAE/FEA; physical testing.

## Gate 08 entry condition
Populate the ledger with measured or primary-source component masses and coordinates, beginning with the actual Boxster donor and the two 750R installation package. Then calculate total mass, CG and static axle loads with uncertainty bounds before structural CAE.
