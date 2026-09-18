# PROP-08 — Mission Profiles & Battery Buffer v1.0

## Executed
Added the phased mission and battery-buffer screening model.

## Mission tracks
- Automotive: urban → highway → overtake → return
- Marine: departure → cruise → acceleration → cruise
- eVTOL: hover → transition → cruise → reserve
- Helicopter: takeoff → climb → cruise → approach → landing
- UAV VTOL: hover → climb → cruise → landing

## Battery-buffer logic
For each phase the turbine supplies sustained electrical power and the battery supplies the instantaneous deficit. Peak battery power and integrated battery energy are calculated, with a configurable reserve factor.

## Cross-discipline rule
A turbine nameplate rating is not treated as equivalent aircraft rotor power, propulsive power, or wheel power. Conversion efficiency, motor/propulsor efficiency, mass, altitude, thermal limits and control margins remain separate variables.

## PROP-09
Add altitude/ISA correction, compressor-map limits, recuperator pressure-drop and thermal penalties, fuel-system and battery mass, complete propulsion-chain efficiency, reserve accounting, and digital-twin output.

Status: research/simulation only; no certification or operational-performance claim.