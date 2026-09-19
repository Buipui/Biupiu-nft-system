# Biupiu Digital Twin + DMS Integration Gate v1.0

## Executed scope
The existing digital-twin architecture is mapped into the DMS DTM module and existing digital-twin.advanced feature.

## Integration map
- DigitalTwinRef -> DTM registry
- TwinEvent -> DMS event/audit pipeline
- T0-T9 -> research evidence state
- dmsSiteId -> site scope
- dmsAssetId -> asset scope
- modelVersion -> versioned model record
- provenanceRefs -> audit/provenance links
- simulation/test/calibration -> analytics/research events

## DMS boundary
Identity, entitlement, site authorization and audit remain authoritative in DMS. The OS adapter does not bypass them.

## BM-11
SIMULATION -> PREDICTION -> PHYSICAL TEST -> QC -> CALIBRATION -> ERROR/UNCERTAINTY UPDATE -> DIGITAL TWIN VERSION -> ACTIVE LEARNING

The adapter transports references and state; simulation does not automatically become validation evidence.

## Modular packaging
Department packages can consume the digital-twin contract without importing the complete DMS implementation.

## Next runtime gate
Connect the adapter to authenticated DMS API and Site Node queue after contract/integration tests pass.
