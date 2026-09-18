# Biupiu SF-02 — Premium Farming System OS

Prototype phase: 0.2 — enclosure + touchscreen HMI + OS function layer
Date: 2026-09-18

## Product direction
SF-02 is the premium field-console evolution of SF-01. The housing is designed around Biupiu composite-material research: a lightweight structural shell, replaceable sensor/maintenance panels and weather-resistant outer skin. Final composite formulation remains an R&D item and must be mechanically, electrically and environmentally tested before production claims are made.

## Industrial-design language
- Premium biotech × regenerative agriculture × advanced materials.
- Clean geometric surfaces, restrained branding and concealed fasteners where practical.
- High-contrast touchscreen interface with large field-readable controls.
- Modular front/rear service panels.
- Sensor and power connections protected from splash and accidental snagging.

## Composite housing concept
Shell: hemp-fibre or other Biupiu-developed natural-fibre composite candidate.
Core: optional lightweight structural core after mechanical testing.
Protection: replaceable UV/weather-resistant exterior coating or skin selected through materials testing.
Internal: non-conductive electronics mounting plate with thermal and vibration isolation.

## Material validation gates
1. Fibre/resin formulation and supplier documented.
2. Tensile, flexural, impact and fastener pull-out tests.
3. Water absorption and dimensional stability.
4. UV/weather exposure.
5. Thermal cycling.
6. Flame/smoke behaviour assessed where required.
7. EMC/grounding strategy verified for the final enclosure.

## Touchscreen architecture
Display: Raspberry Pi-compatible capacitive touchscreen, target 5–10 inch class.
UI: Biupiu Farming System OS.
Primary views: Dashboard, Field Zones, Soil, Climate, Irrigation, Devices, Experiments, Intelligence, Alerts, Maintenance, Data.

## Farming System OS functions — v0.1
- Live sensor dashboard.
- Zone-based farm map abstraction.
- Sensor health and calibration status.
- Irrigation recommendation queue.
- Manual approval/override controls.
- AI advisory history.
- Experiment creation and logging.
- Threshold/rule management.
- Device discovery/status.
- Offline data buffering.
- Local alarm/event log.
- Maintenance checklist.
- Exportable CSV/JSON datasets.
- Intelligence Hub connection status.
- Firmware/version inventory.

## Intelligence Hub contract
The OS sends normalized observations and context to the Biupiu Intelligence Hub. The Hub returns advisory information containing recommendation, evidence, confidence and required approval state. Actuator commands remain constrained by local safety rules.

## Initial dashboard
FIELD STATUS | SOIL | CLIMATE | WATER | INTELLIGENCE

Each zone exposes: moisture, temperature, humidity, light, last update, sensor health and current recommendation.

## Prototype acceptance criteria
- Touchscreen launches directly into Farming System OS.
- Dashboard works without internet using cached/local data.
- Hub connection failure is clearly displayed and does not disable local monitoring.
- AI recommendations are logged with timestamp and source data.
- Manual override remains available.
- Composite housing does not interfere with sensor operation or thermal management.