# SF-01 Wiring Blueprint v0.1

## Prototype wiring map

Arduino 5V -> sensor VCC (only where the chosen sensor explicitly supports 5V)
Arduino GND -> common sensor GND
Soil moisture analog OUT -> A0
Light analog OUT -> A1
Digital temperature/T/RH -> selected digital GPIO (define after exact module selection)
Arduino USB -> Raspberry Pi USB

## Control boundary
Raspberry Pi may issue advisory messages to the Intelligence Hub. Arduino firmware must enforce local safe states. Do not connect pumps, valves or mains equipment directly to GPIO. Use appropriately rated isolated driver hardware and hardware interlocks in later actuator prototypes.

## Commissioning checklist
- Verify every sensor's voltage requirement from its datasheet.
- Confirm common-ground strategy for low-voltage sensors.
- Add fusing/current protection to field power.
- Measure idle and peak current before battery/solar sizing.
- Calibrate every analog sensor before using AI features.
