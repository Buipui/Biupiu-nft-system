# Biupiu Vehicle + Environment Sandbox Specification

## World sandbox
The first sandbox should combine:
- a Biupiu research campus
- regenerative farming plots
- rural roads
- workshop and robotics areas
- water-management demonstration zones
- materials laboratory
- small urban/industrial district
- test track
- marine/port test zone

## Vehicle sandbox
Original vehicle prototypes should be tested through common interfaces:
- acceleration
- braking
- steering
- turning radius
- mass
- traction
- suspension
- energy/fuel model
- cargo capacity
- autonomous assistance
- sensor suite
- maintenance state

No GTA V or Forza proprietary model, texture or physics file is required for the interface.

## Environment sandbox
Each environment package should expose:
- terrain
- roads
- buildings
- vegetation
- water
- lighting
- weather
- navigation mesh
- interaction points
- research stations
- marketplace hooks
- Digital Lab hooks

## World-building principle
GTA V and Forza are reference systems for studying how a sandbox can feel coherent and explorable. Biupiu's implementation must be independently authored.

## Asset performance tiers
LOD0: close inspection
LOD1: normal gameplay
LOD2: medium distance
LOD3: far distance
COLL: collision proxy
NAV: navigation geometry
THUMB: catalogue preview

## Vehicle categories
BIU-CITY, BIU-FARM, BIU-RESEARCH, BIU-LOGISTICS, BIU-MARINE, BIU-EMERGENCY, BIU-EXPERIMENTAL.

## Integration
World Runtime -> Environment Loader -> Vehicle Manager -> Physics Interface -> Intelligence Hub -> Digital Lab -> telemetry/research log.
