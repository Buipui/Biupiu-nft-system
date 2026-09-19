# Biupiu R&D OS — Digital Twin / DMS Adapter v1.0

The existing Biupiu Digital Twin research layer is connected to the modular DMS control plane without merging the systems.

## Boundary
R&D OS owns simulation, model state, evidence/provenance, research workflows and AI optimisation.
DMS owns identity, entitlements, site scope, asset/device records, API routing and enterprise audit.

## Flow
Digital Twin -> OS adapter -> authenticated DMS API -> DTM module -> audit/analytics

Physical path:
Device -> Site Node -> DMS -> DTM -> R&D OS twin adapter -> research/simulation

## Canonical contract
- DMS module: DTM
- Feature: digital-twin.advanced
- API: /api/v1/digital-twins
- Evidence: T0-T9
- Existing microturbine schema: digital-twin/schemas/microturbine_system_v0_1.json
- BM-11 calibration/active-learning loop

## Extermination checks
- reject empty twin IDs;
- reject non-consecutive evidence promotion;
- require model version and provenance references;
- keep DMS authorization separate from scientific evidence promotion;
- never equate subscription access with scientific validation;
- do not emit restricted research/IP into ordinary audit records.

## Status
Architecture adapter implemented. Live DMS transport, physical telemetry and production security remain execution gates.
