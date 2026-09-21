# Biupiu Smart Farming — Hardware Federation Gate G3
Date: 2026-09-21
Status: DESIGN SPEC REGISTERED / PHYSICAL HARDWARE VERIFICATION PENDING

## Scope
G3 converts the SF-01 Raspberry Pi + Arduino farming architecture into a buildable hardware interface for the Ola/olla raised-bed experiment.

The experiment remains one physical raised bed containing dhanya (coriander), mint and thyme, with three logical crop zones. The control system therefore preserves independent zone telemetry without requiring three separate beds.

## Federation topology
Raspberry Pi 5 — supervisor/gateway/HMI/logging
  -> Arduino Mega 2560-class edge controller
  -> three logical crop zones
  -> environmental sensors
  -> protected power distribution
  -> manual-safe irrigation/actuation boundary

AI/intelligence recommendations remain advisory. Local safety limits and manual approval remain authoritative for the prototype.

## Zone instrumentation
Zone A — dhanya:
- capacitive soil-moisture sensor
- DS18B20 soil-temperature probe
- olla/irrigation water-status sensor

Zone B — mint:
- capacitive soil-moisture sensor
- DS18B20 soil-temperature probe
- olla/irrigation water-status sensor

Zone C — thyme:
- capacitive soil-moisture sensor
- DS18B20 soil-temperature probe
- olla/irrigation water-status sensor

Shared:
- air temperature/RH sensor
- light sensor
- reservoir level sensor
- battery voltage/current monitor
- leak/fault input

## Provisional Arduino Mega pin map
A0 = Zone A soil moisture
A1 = Zone B soil moisture
A2 = Zone C soil moisture
A3 = reservoir level
A4 = battery voltage monitor
A5 = battery current monitor
A6 = light sensor
A7 = spare analog input

D22 = Zone A olla/water-status input
D23 = Zone B olla/water-status input
D24 = Zone C olla/water-status input
D25 = leak detector
D26 = irrigation actuator enable
D27 = emergency/fault input

D30 = 1-Wire bus for three DS18B20 probes
D31 = air temperature/RH digital bus
D32 = spare sensor bus
D33 = status/fault output
D34 = manual approval input

Serial1 = Raspberry Pi communications
Serial2 = reserved expansion
I2C = future ADC/current/expansion bus

## Electrical architecture
12 V rechargeable battery
 -> main fuse
 -> master disconnect
 -> protected DC distribution
 -> 5 V regulated rail for Raspberry Pi
 -> regulated rail for Arduino/sensors
 -> separately fused actuator rail

All sensor returns use a defined common reference. Actuator power is isolated from logic power as required by the final actuator choice. Outdoor electronics enclosure target: IP67 or better.

## Harness IDs
H-01 battery to protected distribution
H-02 protected 5 V to Raspberry Pi
H-03 logic supply to Arduino
H-04 Zone A sensor bundle
H-05 Zone B sensor bundle
H-06 Zone C sensor bundle
H-07 shared environmental sensor bundle
H-08 actuator/feedback bundle
H-09 emergency/fault chain
H-10 service/programming connectors

## Federation data contract
Each observation must carry:
experiment_id, zone_id, sensor_id, timestamp, raw_value, unit, calibration_id, quality_state, source_controller, model_version, evidence_state.

The Raspberry Pi may buffer and normalize telemetry. It must not silently convert simulated or inferred values into observed physical values.

## Required verification before build approval
1. Confirm exact Arduino board.
2. Confirm exact Raspberry Pi model and power budget.
3. Select exact sensor part numbers.
4. Verify voltage/current limits and connector pinouts from datasheets.
5. Verify battery chemistry, BMS, fuse ratings and enclosure thermal behaviour.
6. Bench-test every input before connecting the outdoor harness.
7. Perform sensor calibration against measured soil/water conditions.
8. Run network-loss and Raspberry Pi restart recovery tests.
9. Run actuator fault-injection with manual approval enabled.
10. Record measured results in the SF-01 experiment log.

## Supplier routing
Preferred procurement order remains:
1. Mantech
2. Mouser
3. Mustek
4. Communica

No supplier price or part number is treated as verified until a current supplier page or quotation is checked.

## Gate result
G3 architecture and provisional pinout are registered.
G3 is NOT marked physically verified.
Next gate: G4 — exact component selection, datasheet verification, current supplier pricing, electrical load budget and bench-test matrix.
