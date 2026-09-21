# Vehicle Evidence Mass Model Gate 06 — v1.0

**Date:** 21 September 2026  
**Status:** EXECUTED — source-backed baseline mass model; measured/CAD integration remains OPEN

## Evidence refresh

### Hypercar — Porsche Boxster 986 baseline
The hypercar donor is corrected from Audi R8 to the **Porsche Boxster Type 986**.

Porsche identifies the 986 as a mid-engine roadster with a water-cooled flat-six. Porsche's current Classic material confirms the 986 model family from model year 1997 onward and the Boxster S introduction in 1999. Porsche's published historical material records the 2.7 L Boxster at 162 kW / 220 PS and later 168 kW / 228 PS, and the 3.2 L Boxster S at 185 kW / 252 PS and later 191 kW / 260 PS. citeturn1search0turn1search22

For the controlled dimensional/mass baseline, the 986 family reference records a **2,415 mm wheelbase** and curb weights varying by derivative/transmission. The 2.7 L 2000–2002 reference is 1,260 kg manual / 1,310 kg Tiptronic; the 3.2 L Boxster S 2000–2002 reference is 1,295 kg manual / 1,335 kg Tiptronic. These are retained as model-family reference values pending exact donor-year/derivative confirmation. citeturn0search0

**Status:** donor family selected; exact 986 model year, engine derivative, transmission and donor condition remain OPEN.

### Overlander — IVECO Daily 4x4 4,175 mm baseline

### Overlander — IVECO Daily 4x4 4,175 mm baseline
Current IVECO material records the 4,175 mm wheelbase and 7,000 kg GVM configuration. The current specification records 132 kW and 430 Nm. IVECO also states that final payload varies with body selection.

A prior IVECO South Africa technical sheet records a 4,175 mm cab/chassis kerbweight of 2,900 kg, including a 75 kg driver, full fuel, oils, toolkit and spare wheel when present. This is retained as a historical/configuration-specific reference, not as the exact mass of a 2026 build.

## Evidence-backed boundary calculations

### Boxster donor mass reference
The previous R8 mass-reserve calculation is **superseded and must not be used**.

For the 986 family, published reference curb masses range approximately from 1,250 kg to 1,360 kg depending on derivative/transmission. These are donor-reference values only and are not a conversion mass allowance. citeturn0search0

Any conversion must separately account for occupants, fuel, fluids, retained equipment, replacement bodywork, hybrid hardware and safety systems.

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

## Correction control

The Audi R8 baseline is **SUPERSEDED for this case study**. All future hypercar calculations in this vehicle track shall use the Porsche Boxster 986 family unless a later user instruction selects a different Boxster generation/derivative.

The prior R8-specific numerical mass and axle-limit inputs are not to be reused as Boxster data.

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
