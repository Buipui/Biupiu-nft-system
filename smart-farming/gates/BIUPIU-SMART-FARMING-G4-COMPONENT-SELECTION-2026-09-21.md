# Biupiu Smart Farming — G4 Exact Component Selection & Verification Gate
Date: 2026-09-21
Status: PARTIALLY VERIFIED / PROCUREMENT QUOTE & BENCH VALIDATION PENDING
Commit target: next repository commit

## 1. Build baseline
Controller: Arduino Mega 2560-class board.
Gateway: Raspberry Pi 5 8GB.
Physical experiment: one raised bed; three logical zones: dhanya, mint, thyme.
Irrigation concept: olla/ola reservoirs and passive wick delivery; powered irrigation is retained only as an optional controlled assist, not assumed as necessary.

## 2. Selected/provisional components
A. Zone soil moisture x3
Preferred: Mantech CSMS-V2.0 capacitive soil/moisture board.
Verified technical data: 3.3–5V supply, <20mA, 0–5V output, -10 to +70C, adjustable sensitivity; exact soil calibration remains mandatory.
Price: Mantech currently lists price on request.

B. Zone soil temperature x3
Preferred: Mantech DS18B20-P2M or KS0316 waterproof probe.
DS18B20-P2M is listed at R79.20 each excl VAT; KS0316 at R113.13 each excl VAT.
Use one 1-Wire bus with unique sensor IDs.

C. Air temperature/RH x1
Prototype option: Mantech DHT22/AM2302, R198.89 excl VAT.
Higher-quality production candidate: weatherproof SHT31-class sensor through Mouser; final part number/quote remains open.

D. Raspberry Pi x1
Mantech Cape Town listing confirms Pi 5 8GB model, but price is currently quote/on-request. Raspberry Pi 5 official specification confirms 5V/5A USB-C power requirement and 40-pin header.

E. Arduino Mega x1
Mantech lists Mega 2560-class development hardware; current exact standalone board price should be quoted rather than substituting a kit. A Mega expansion/breakout shield is listed at R112.23 excl VAT.

F. Soil reference instrument
Mantech PMS-714 is available at R3,919.88 excl VAT and is retained as a calibration/reference instrument, not a permanent embedded sensor.

## 3. Hardware decisions
- Keep Mega 2560 as the edge controller because the current architecture requires more I/O and expansion headroom than an Uno.
- Keep Pi 5 8GB as gateway for logging, HMI, federation and local buffering.
- Use capacitive rather than exposed-resistive soil probes for the primary embedded moisture channel.
- Use DS18B20 probes for zone temperature because multiple devices can share the same 1-Wire bus.
- Keep DHT22 as prototype-only pending comparison against a weatherproof higher-grade RH sensor.

## 4. Pin allocation locked for bench prototype
A0/A1/A2 = zone moisture A/B/C
A3 = reservoir level
A4 = battery voltage sense
A5 = battery current sense
A6 = light
A7 = spare
D22/D23/D24 = zone olla/water-status
D25 = leak
D26 = actuator enable
D27 = emergency/fault
D30 = DS18B20 1-Wire
D31 = air temperature/RH
D33 = status/fault
D34 = manual approval
Serial1 = Pi link
I2C = expansion

## 5. Important correction
The previous G3 wording described the system as a single raised bed with three logical crop zones. This is the authoritative physical layout for this experiment. The software remains zone-independent so future three-bed deployment can reuse the same contracts.

## 6. Price evidence
Prices below are current web observations and exclude VAT unless the supplier states otherwise:
- DS18B20-P2M: R79.20 each
- KS0316 waterproof DS18B20: R113.13 each
- DHT22: R198.89 each
- Mega expansion shield: R112.23
- PMS-714 reference meter: R3,919.88
- Pi 5 8GB: quote/on-request at Mantech
- CSMS-V2.0 capacitive soil sensor: quote/on-request at Mantech
Mouser South Africa supports ZAR purchasing and BOM/quote workflows; current selected-part prices must be captured from the exact final part numbers before procurement.

## 7. Verification gates still open
- exact Mega SKU and Pi 5 SKU quote
- three CSMS-V2.0 quotes
- final weatherproof RH sensor
- reservoir-level technology and exact part
- battery chemistry/capacity/BMS
- regulator efficiency and current budget
- fuse sizing
- IP67 enclosure and cable glands
- actuator selection, if powered assist is retained
- complete BOM total
- bench electrical test
- sensor calibration
- outdoor ingress/thermal test

## G4 result
G4 is REGISTERED as a controlled hardware-selection baseline.
It is NOT marked fully verified because supplier quotations, final component datasheets, battery/power calculations and physical bench tests remain open.
Next gate: G5 — electrical power budget + wiring harness + protection/fuse design + bench test matrix.
