# PROP-07 — Cross-Discipline Microturbine Mission Model v1.0

## Gate result
A first numerical screening model has been added at:
simulators/biupiu_cross_discipline_mission_v0_1.py

It evaluates BT-70, BT-140, BT-200 and BT-300 concepts against:
- Automotive range-extender
- Marine hybrid cruise
- eVTOL cruise/transition
- Helicopter hybrid-electric study
- UAV endurance extender

## Important interpretation
The model is a screening tool, not a flight, marine or road-performance predictor. Mission power values are illustrative inputs. It deliberately exposes peak-power gaps so battery buffering can be sized rather than assuming the turbine supplies transient peak demand.

## Cross-discipline design rule
Use the turbine primarily as an efficient sustained-power source where the mission permits it; use battery/electric storage for transient demand. Aircraft applications additionally require mass, altitude, thermal, redundancy, containment and certification analysis. Marine applications require continuous-duty, corrosion, filtration and fire-safety analysis. Automotive applications require emissions, NVH, packaging and road-approval analysis.

## Next gate
PROP-08: replace the illustrative mission inputs with parameterized mission profiles and add:
1. battery sizing for peak-power gaps;
2. altitude/ambient-pressure effects;
3. marine sea-level continuous-duty thermal model;
4. helicopter/eVTOL hover-transition-cruise mission phases;
5. turbine mass and fuel-system mass;
6. recuperator pressure-drop penalty;
7. corrected whole-system energy accounting;
8. CSV/JSON output for the Biupiu digital twin.
