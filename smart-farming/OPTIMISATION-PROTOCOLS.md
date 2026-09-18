# Biupiu Farming System OS — Optimisation Protocol Framework

**Version:** 0.1

## Objective
Create a software-release framework that progressively improves plant-growth recommendations from measured data while preserving traceability and avoiding unsupported universal claims.

## Growth-cycle model
Every plant profile can be represented as stages such as:
1. Establishment
2. Vegetative/development
3. Reproductive/flowering or crop-specific production stage
4. Maturation/fill
5. Harvest/readiness
6. Post-harvest observation

The stage names and parameters must be configurable by crop rather than hard-coded as universal biology.

## Optimisation loop
Observe -> Validate -> Compare -> Recommend -> Human review -> Implement -> Measure -> Learn -> Version.

## Optimisation dimensions
- Soil/substrate moisture
- Root-zone temperature
- Air temperature
- Relative humidity
- Light exposure
- CO2 where relevant and safely measured
- Water quantity/timing
- Soil/substrate EC and pH where supported
- Plant growth observations
- Phenological stage
- Pest/disease observations
- Weather/environment context

## Protocol maturity levels
**L0 — Template:** untested starting profile.
**L1 — Observed:** telemetry and observations collected.
**L2 — Experimental:** controlled comparison underway.
**L3 — Repeated:** repeatable evidence across multiple runs.
**L4 — Validated for defined conditions:** evidence supports use within explicitly documented boundaries.

Only L3/L4 protocols should be surfaced as established optimisation protocols, and their conditions must remain visible.

## Software-release mechanism
Plant profiles, sensor mappings and optimisation protocols should be versioned independently from the core OS. A software release may add:
- new plant profiles;
- new sensor compatibility;
- new derived metrics;
- new optimisation experiments;
- updated thresholds with documented evidence;
- new product recommendations;
- revised safety limits.

Each release records source data, test period, affected plant profile, assumptions, known limitations and rollback version.

## Product linking
A plant profile may reference compatible Biupiu products such as soil nodes, climate nodes, irrigation controllers, greenhouse devices and future robotics. Compatibility must be explicit rather than inferred.
