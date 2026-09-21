# Vehicle Evidence Mass Model Gate 06 — v1.0

**Date:** 21 September 2026  
**Status:** EXECUTED — source-backed baseline mass model; measured/CAD integration remains OPEN

## Evidence refresh

### Hypercar — first-generation Audi R8 4.2 FSI quattro
The published technical data records:
- 4,163 cc V8
- 309 kW / 420 bhp
- 430 Nm
- 1,560 kg unladen mass excluding driver
- 1,860 kg gross limit
- front axle limit 890 kg
- rear axle limit 1,050 kg
- aluminium ASF body
- 4,431 mm length
- 1,904 mm width
- 1,252 mm height
- 2,650 mm wheelbase
- front/rear track 1,632 / 1,593 mm

These values are donor-reference inputs. They do not establish the mass of the proposed converted vehicle.

### Overlander — IVECO Daily 4x4 4,175 mm baseline
Current IVECO material records the 4,175 mm wheelbase and 7,000 kg GVM configuration. The current specification records 132 kW and 430 Nm. IVECO also states that final payload varies with body selection.

A prior IVECO South Africa technical sheet records a 4,175 mm cab/chassis kerbweight of 2,900 kg, including a 75 kg driver, full fuel, oils, toolkit and spare wheel when present. This is retained as a historical/configuration-specific reference, not as the exact mass of a 2026 build.

## Evidence-backed boundary calculations

### R8 donor mass reserve
Gross limit − unladen mass = 1,860 − 1,560 = **300 kg nominal reserve**.

This is NOT available as a conversion allowance. It is simply the difference between the cited donor unladen mass and gross limit. Any conversion must separately account for occupants, fuel, fluids, retained equipment, replacement bodywork, hybrid hardware and safety systems.

### Daily reference payload
7,000 kg GVM − 2,900 kg historical cab/chassis kerb reference = **4,100 kg nominal difference**.

This is NOT a guaranteed usable payload because the 2,900 kg figure is configuration/date-specific and IVECO states final payload depends on body selection.

## Axle-load model

For wheelbase L, total mass M and CG distance x from front axle:

Front = M × (L − x) / L  
Rear = M × x / L

For the R8, axle limits remain **890 kg front / 1,050 kg rear** from the cited technical data.

For the Daily, this gate does not substitute an axle-rating assumption where the exact selected configuration has not been verified.

## Gate 06 controls

1. Donor kerb/unladen mass is not interchangeable with dry mass.
2. Manufacturer GVM/GVW is not a target operating mass.
3. Historical technical-sheet weights cannot be silently assigned to current builds.
4. Every proposed replacement component must have source, mass, location and uncertainty.
5. Composite mass savings require component-level BOM evidence.
6. Any change to axle load requires recalculation before structural approval.
7. CAD clearance is not verified until geometry is measured or imported from a validated source.
8. FEA remains downstream of the evidence-backed mass/geometry model.

## Gate result

**EXECUTED**
- Exact working R8 4.2 FSI donor configuration now has a source-backed baseline mass, dimensions and axle limits.
- Daily 4x4 4,175 mm baseline has current GVM/GCM/wheelbase/power evidence plus a clearly labelled historical cab/chassis mass reference.
- Conversion mass-reserve calculations were performed with their limitations explicitly recorded.
- CG/axle-load calculation controls remain active.

**OPEN / NOT VERIFIED**
- Actual donor vehicle weighing.
- Exact current Daily chassis-cab mass.
- Component-level hybrid-system masses.
- Actual component CG coordinates.
- CAD geometry and interference checks.
- Structural load paths.
- FEA/CAE.
- Thermal validation.
- Crashworthiness.
- Physical testing.

## Gate 07 entry

Build the component-level evidence ledger for the proposed R8 hybrid configuration and Daily expedition configuration, assigning each mass/geometry value an evidence class, uncertainty and coordinate reference. Then calculate actual predicted mass, CG and axle loads before CAE.
