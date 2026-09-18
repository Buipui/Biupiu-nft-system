# Biupiu Smart Farming v1.0

**Department:** FARMING
**Audience:** Growers, regenerative-farming operators and farming subscribers
**Access:** Farming entitlement only

## Product concept

A department-specific smart farming environment for recording, monitoring and improving farming operations. It uses the same Biupiu subscriber architecture while restricting knowledge, projects, sensor data and AI retrieval to farming resources.

## Subscriber boundary

A `FARMING` subscriber receives access to:
- farming knowledge resources;
- farm/project records;
- soil and water records;
- crop records;
- sensor observations;
- irrigation records;
- regenerative practices;
- field trials;
- farm equipment records;
- farming-specific AI retrieval.

It does not receive metallurgy-only resources unless a separate `METALLURGY` entitlement exists.

## Resource registry

Suggested object types:

`FarmProject`
`FieldRecord`
`CropRecord`
`SoilRecord`
`WaterRecord`
`SensorRecord`
`IrrigationRun`
`WeatherObservation`
`RegenerativePractice`
`TrialRecord`
`YieldRecord`
`EquipmentRecord`
`FailureRecord`
`ReferenceSource`

## Smart farming workflow

`FIELD → OBSERVE → PLAN → INTERVENE → MEASURE → RESULT → REPEAT/FAILURE → FARM KNOWLEDGE`

The platform should support manual records first, with future sensor/IoT integration.

## Smart functions

- Field and crop registry
- Soil and water observations
- Irrigation tracking
- Sensor data ingestion
- Regenerative farming trial records
- Crop-health observations
- Yield and input records
- Equipment records
- Experiment planning
- Failure/lessons register
- Photo/document attachments
- Farming-only AI retrieval
- Farm dashboards
- Exportable farm records

## Access examples

Allowed:
`FARMING subscriber → FarmProject`

Denied:
`FARMING subscriber → MetalProject`

Allowed when explicitly entitled:
`FARMING + METALLURGY subscriber → both department workspaces`

## Product objective

Provide a focused farming workspace that can later connect to smart sensors, automation and the broader Biupiu Living Systems Lab while preserving strict department-level information boundaries.
