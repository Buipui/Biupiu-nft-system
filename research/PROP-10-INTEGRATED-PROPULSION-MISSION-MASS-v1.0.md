# PROP-10 — Integrated Propulsion/Mission/Mass Model v1.0

## Gate execution
The Biupiu Blade & Microturbines repository now links turbine output, propulsion-chain efficiency, mission-phase demand, battery buffering and hardware mass.

### Integrated variables
- turbine net electrical power
- turbine/recuperator/generator/fuel-system mass
- electric propulsion-path efficiency
- mission phase demand
- peak battery power
- battery energy requirement plus reserve
- battery mass from both energy and power constraints
- total system mass
- system specific power
- estimated fuel-energy input

### Application branches
The same integrated engine is applied independently to:
- AUTO
- MARINE
- EVTOL
- HELI
- UAV

This is deliberately a screening framework. The illustrative package masses and mission demands are assumptions, not measured Biupiu hardware data.

### Design principle
For each application, turbine sizing and battery sizing are treated as coupled variables. A larger turbine can reduce battery power/energy requirements but increases turbine-system mass; a smaller turbine can reduce turbine mass while increasing battery requirements. The next optimisation layer should search this trade space rather than selecting the largest turbine by default.

### PROP-11
Next gate should add:
1. parametric optimisation of turbine/battery split;
2. pressure-ratio/TIT/recuperator sensitivity;
3. altitude derating coupled to eVTOL/HELI/UAV missions;
4. marine continuous-duty thermal constraints;
5. digital-twin JSON schema and dataset export;
6. automated feasibility flags for thermal, power and mass limits.

Status: conceptual research/simulation only.
