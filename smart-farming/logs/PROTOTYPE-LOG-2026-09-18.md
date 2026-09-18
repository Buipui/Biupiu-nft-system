# Biupiu Digital Workshop — Smart Farming Prototype Log

**Run:** SF-01 / 001
**Date:** 2026-09-18
**Stage:** Architecture + software prototype

## Objective
Build the first Raspberry Pi + Arduino smart-farming node and establish a controlled interface to the Biupiu Intelligence Hub.

## Hypotheses to test
- H1: Soil-moisture telemetry can provide a useful irrigation signal after soil/sensor calibration.
- H2: Combining soil moisture with microclimate and light data can improve advisory context versus a single sensor.
- H3: A Raspberry Pi gateway can buffer, validate and normalize edge telemetry before intelligence processing.

## Current evidence status
**Not yet experimentally validated.** This entry records the prototype architecture and testable hypotheses, not proof of performance.

## Next measurements
1. Calibrate moisture sensor against gravimetric soil moisture.
2. Log 24–72 h of soil moisture, temperature/RH and light.
3. Compare advisory recommendations with manually observed soil condition.
4. Record false positives/negatives and sensor drift.
5. Test network loss and gateway restart recovery.

## Result fields
- Raw data:
- Calibration curve:
- Environmental conditions:
- Advisory output:
- Human decision:
- Outcome after 6/12/24 h:
- Faults:
- Revision:
