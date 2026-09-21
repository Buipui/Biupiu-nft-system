# Biupiu Learning Protocol v2

Status: DEFAULT PROTOCOL — SOURCE IMPLEMENTED / RUNTIME VERIFICATION PENDING

## Mandatory event model
The learning layer records:
INBOUND SEARCH -> SOURCE -> EXTRACTION -> NORMALISATION -> CLASSIFICATION -> CROSS-CHECK -> SIMULATION -> RESULT -> FAILURE/SUCCESS -> OUTBOUND UPDATE.

## LearningEvent fields
- sequence
- direction
- event_type
- source_uri/reference
- repository_path
- source_version/commit
- licence_state
- input_hash
- output_hash
- model_version
- assumptions
- units
- evidence_state
- confidence
- validation_status
- parent_event
- simulator_id
- twin_id
- agent_id
- timestamp

## Learning behaviour
The algorithm must learn from both positive and negative evidence:
- successful build/test;
- failed build/test;
- rejected licence;
- stale dependency;
- conflicting model;
- numerical instability;
- unit mismatch;
- translation uncertainty;
- simulator disagreement;
- successful cross-validation.

Learning is bounded to metadata, model parameters, retrieval/routing statistics and explicitly promoted model artefacts. It must not rewrite historical records.

## Default-on rule
Every new repository search/update must append a learning event. Search tools are discovery; validation remains a separate gate.

## Agent authority
The native agent may:
- classify;
- deduplicate;
- link;
- propose adapters;
- schedule tests;
- compare models;
- update indexes;
- create evidence records.

It may not silently:
- promote unverified science;
- expose secrets;
- publish IP;
- deploy contracts;
- control physical machinery;
- alter historical provenance.
