# Simulation Adapter v1.0

Consumes structured outputs from existing Biupiu Python simulators and exposes them for UE visualization.

Initial source families:
- propulsion simulator
- propulsion comparison
- propulsion optimiser
- integrated propulsion mission
- cross-discipline mission
- component-map interfaces
- cycle physics
- mission profiles

## Data flow
Python numerical model → versioned result → validation metadata → UE SimulationResultComponent → visualization.

UE visualization must preserve source dataset identity and units.
