# AI-07 — Physical Laboratory & Sensor Ingestion

## Objective
Create the software boundary between the R&D OS and physical experimental devices.

## Supported device classes
- Raspberry Pi
- Arduino
- ESP32
- Generic IoT gateway

## Flow
DEVICE REGISTRATION → SENSOR READING → VALIDATION → NORMALISATION → EXPERIMENT DATASET → ANALYSIS

## Implemented foundation
- device registry
- registered-device enforcement
- normalized sensor-reading schema
- ingestion service
- automated tests
- Android device/reading DTOs

## Data integrity
Sensor data retains device ID, sensor ID, timestamp, value, unit and quality state. Unknown devices are rejected at ingestion.

## Safety boundary
This gate only establishes data ingestion. It does not authorize autonomous control of machinery, electrical systems, laboratory equipment or hazardous processes.

## Next gate
AI-08: experiment dataset storage, time-series handling and AI feedback loop.
