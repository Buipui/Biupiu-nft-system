# SF-01 Physical Blueprint — v0.1

## Conceptual layout (not manufacturing-certified)

      TOP VIEW — weather-resistant enclosure
      +---------------------------------------+
      | [solar/power input] [status LED]      |
      |                                       |
      | [Raspberry Pi gateway]                |
      |        | USB/Serial                   |
      | [Arduino sensor controller]           |
      |   |       |       |       |            |
      +---|-------|-------|-------|------------+
          |       |       |       |
       soil M  soil T   air T/RH  light

## Mechanical design intent
- Electronics remain above splash zone.
- Sensor cables exit through sealed glands on the lower/side face.
- Soil probes mount vertically with strain relief.
- Enclosure includes service access and a removable sensor harness.
- Keep low-voltage sensor wiring physically separated from pumps/actuator wiring.

## Engineering note
Dimensions are intentionally provisional until selected enclosure, connector and sensor models are frozen. Produce a CAD drawing only after those components are selected and measured.
