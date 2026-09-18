# SF-01 — Soil & Microclimate Node

**Status:** Prototype specification v0.1
**Date:** 2026-09-18

## Functional specification
| Item | Prototype target |
|---|---|
| Controller | Arduino-compatible MCU with USB/serial to Raspberry Pi |
| Gateway | Raspberry Pi Zero 2 W / Pi 4/5 |
| Soil moisture | Capacitive analog sensor; calibrate for soil type |
| Soil temperature | Waterproof digital temperature probe |
| Air T/RH | Digital T/RH sensor |
| Light | Digital/analog light sensor |
| Optional EC | EC interface with isolated/protected input as appropriate |
| Power | 5 V regulated rail; separate actuator rail if used |
| Communications | USB serial for first prototype; MQTT/HTTP later |
| Enclosure | IP-rated outdoor enclosure for field prototype |
| Data interval | 60 s default; configurable |
| Local storage | SQLite/CSV buffer on Pi |
| AI interface | JSON observations -> Intelligence Hub -> advisory JSON |

## Acceptance tests
1. Sensor readings are timestamped and validated.
2. Out-of-range values are rejected or flagged rather than silently used.
3. Loss of Raspberry Pi/network does not create uncontrolled actuator behavior.
4. AI advice is logged with the input observation and model response.
5. Manual override remains available.

## Initial bill of materials categories
MCU, Raspberry Pi gateway, capacitive moisture probe, T/RH sensor, temperature probe, light sensor, regulated power supply, connectors, enclosure, mounting hardware, cable glands and optional relay/MOSFET driver.
