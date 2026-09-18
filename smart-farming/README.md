# Biupiu Smart Farming Digital Workshop

Prototype lab for AI-assisted regenerative farming devices using Raspberry Pi and Arduino-class controllers, linked to the Biupiu Intelligence Hub.

## Architecture
- **Edge layer:** Arduino/ESP-class controller reads sensors and drives safe local actuators.
- **Gateway layer:** Raspberry Pi aggregates telemetry, timestamps observations, performs local rules/feature extraction, buffers data, and exposes an API.
- **Intelligence Hub:** receives normalized observations and returns advisory actions; the edge controller never accepts unrestricted AI commands.
- **Research layer:** experiment logs, calibration records, hypotheses, failures and measured results.

## Safety principle
AI recommendations are advisory by default. Irrigation, nutrient dosing, pumps and other actuators require explicit safety limits, local interlocks and, for the prototype, manual approval.

## Prototype target
First device: **SF-01 Soil & Microclimate Node** — soil moisture, soil temperature, air temperature/humidity, light and optional electrical-conductivity sensing. The design is modular so additional sensors can be added after calibration.
