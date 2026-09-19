# SF37 — Farming Simulator Digital-Twin Bridge v1.0

## Purpose

Define the adapter between Farming Simulator-style external simulation resources and the Biupiu Smart Farming System.

## Architecture

External Simulator / Reference
-> Telemetry Adapter
-> Normalised Farm State
-> Biupiu Digital Twin
-> Smart Farming Intelligence
-> Scenario Engine
-> Biupiu World
-> Results / Provenance

## Normalised farm state

Minimum schema:

- farm_id
- scenario_id
- timestamp
- field_id
- crop_id
- growth_stage
- soil_moisture
- soil_fertility
- soil_organic_matter
- weather
- irrigation_state
- rainfall
- machinery_state
- implement_state
- speed
- fuel_or_energy
- work_rate
- yield_estimate
- harvested_yield
- livestock_state
- storage_state
- input_inventory
- market_state
- autonomy_state
- sensor_health
- source/provenance metadata

## Control boundary

External simulator commands must pass through a Biupiu adapter and policy layer. The World layer never receives unrestricted simulator control.

Allowed future command classes:
- start/stop scenario;
- select field;
- configure crop;
- configure irrigation;
- set machine/implement scenario;
- request telemetry;
- run autonomous test;
- record result.

## Smart-system functions

The bridge feeds:
- crop-growth modelling;
- irrigation optimisation;
- soil-regeneration experiments;
- machinery utilisation;
- autonomous field navigation;
- sensor-fusion experiments;
- farm logistics;
- cost/yield analysis;
- Digital Twin replay.

## World functions

Validated results can become:
- educational missions;
- farming challenges;
- historical agriculture scenarios;
- robotics trials;
- virtual farm management;
- before/after regenerative experiments;
- research visualisations.

## Validation

Every imported external record must retain:
- source repository;
- commit/tag/version where available;
- licence;
- source timestamp;
- transformation version;
- validation status;
- Biupiu asset/derivative status.

**Status: ARCHITECTURE REGISTERED. Live adapter execution remains a host-validation gate.**
