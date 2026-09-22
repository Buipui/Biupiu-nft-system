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


## Native OS Language Selection — 22 September 2026
Smart Farming remains a domain subsystem and consumes the shared Biupiu language contract rather than defining a separate language authority.

Canonical contract: `apps/shared/runtime/BIUPIU-LANGUAGE-CONTRACT-v1.json`
Native selector: `apps/shared/runtime/LanguageSelector.kt`

The farming OS must preserve BCP-47 language/script/region identity, use deterministic fallback, retain original-language plant/research terminology, and expose locale selection to the shared OS/Intelligence layer. Translation is not treated as evidence validation.

Status: **CONTRACT INTEGRATED / DOMAIN RUNTIME UI DEPLOYMENT PENDING**.
