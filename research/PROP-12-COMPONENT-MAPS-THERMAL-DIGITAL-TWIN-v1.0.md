# PROP-12 — Component Maps, Thermal Limits & Digital-Twin Integration v1.0

## Executed
Added a data-driven component-map interface and upgraded the digital-twin schema.

### Component interfaces
The architecture now accepts separate maps for compressor, turbine, generator and recuperator. Each operating point carries corrected speed, corrected flow and pressure ratio with explicit validity status.

### Why this matters
The PROP-11 optimiser used heuristic scaling factors. PROP-12 creates the interface needed to replace those assumptions with published, manufacturer or Biupiu bench-test maps.

### Thermal and mass integration
The digital twin now has explicit fields for turbine, recuperator, generator, fuel-system and battery mass, altitude, ambient temperature, mission phases and validation evidence.

### Application tracks
AUTO / MARINE / EVTOL / HELI / UAV remain separate application branches.

### Evidence rule
Missing component-map data is reported as NO_MAP_DATA rather than silently substituted with a claimed performance value.

## PROP-13
Add published component datasets where permitted, map interpolation, generator maps, recuperator flow/temperature response, thermal rejection, mission-linked lookup, uncertainty/sensitivity analysis and digital-twin result export.

Status: research/simulation only.
