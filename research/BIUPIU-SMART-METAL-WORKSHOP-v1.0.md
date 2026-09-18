# Biupiu Smart Metal Workshop v1.0

**Department:** METALLURGY
**Audience:** Hobbyists and home-workshop metalworkers
**Access:** Metallurgy entitlement only

## Product concept

A department-specific smart workshop environment for hobbyists who operate their own home metalworking spaces. It provides metallurgy-focused knowledge, records, planning, experiments, material tracking and workshop intelligence without exposing unrelated Biupiu departments.

## Subscriber boundary

The product uses the common Biupiu subscriber engine.

A `METALLURGY` subscriber receives access to:
- metallurgy knowledge resources;
- material records;
- heat-treatment records;
- furnace/forge equipment records;
- process logs;
- alloy experiments;
- hardness/strength test records;
- workshop inventory;
- project records;
- metallurgy-specific AI retrieval.

It does not receive farming-only resources unless a separate `FARMING` entitlement exists.

## Resource registry

Suggested object types:

`MetalProject`
`MaterialRecord`
`AlloyRecord`
`HeatTreatmentRun`
`FurnaceRecord`
`ForgeRecord`
`ToolRecord`
`ProcessRecord`
`TestRecord`
`Measurement`
`FailureRecord`
`SafetyRecord`
`ReferenceSource`
`WorkshopAsset`

## Hobbyist workflow

`MATERIAL → PROCESS PLAN → HEAT/FORMING OPERATION → MEASUREMENT → RESULT → REPEAT/FAILURE → KNOWLEDGE RECORD`

The system should support both manual entry and future sensor integration.

## Smart workshop functions

- Material identification and batch records
- Alloy/composition reference lookup
- Heat-treatment logging
- Temperature/time records
- Furnace/forge maintenance logs
- Tool and consumable inventory
- Experiment planning
- Measurement capture
- Failure and lessons register
- Photo/document attachments
- Searchable metallurgy library
- AI-assisted retrieval restricted to metallurgy resources
- Project dashboards
- Exportable workshop records

## Optional hardware integration

Future integrations can include temperature sensors, load cells, thermocouples, scales, cameras and other appropriate instrumentation. Hardware interfaces should be modular and must not be represented as safety-certified control systems unless independently certified.

## Access examples

Allowed:
`METALLURGY subscriber → MetalProject`

Denied:
`METALLURGY subscriber → FarmingProject`

Allowed when explicitly entitled:
`METALLURGY + FARMING subscriber → both department workspaces`

## Safety

The application records and organises workshop information; it does not replace competent supervision, equipment manuals, ventilation/fire controls, PPE, electrical safety, gas safety or applicable local requirements. High-temperature, molten-metal, pressure and combustible-material operations require appropriate risk controls.

## Product objective

Create a focused home-workshop metallurgy product that is useful on its own while remaining compatible with the wider Biupiu R&D OS.
