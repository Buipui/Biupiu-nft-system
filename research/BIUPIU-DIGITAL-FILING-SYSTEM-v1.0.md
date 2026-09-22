# BIUPIU DIGITAL FILING SYSTEM v1.0

Status: IMPLEMENTED AT REPOSITORY SCHEMA LEVEL / RUNTIME INDEXER PENDING

## Canonical filing dimensions
system; department/domain; capability; artifact type; language; source/provenance; licence; evidence state; validation level; implementation state; authority owner; dependencies; cross-links; supersession; security classification; retention.

## Artifact classes
RESEARCH | CODE | PATTERN | ADAPTER | DEPENDENCY | SCHEMA | CONTRACT | DATASET | MODEL | SIMULATOR | ASSET | TEST | BUILD | RELEASE | INCIDENT | LEARNING | GOVERNANCE

## Lifecycle
INGEST -> HASH -> PROVENANCE -> CLASSIFY -> INDEX -> LINK -> VALIDATE -> QUARANTINE/PROMOTE -> RETAIN

## External-language lane
Language is metadata, not a trust level. Translation assists discovery; original URI/title/commit/licence/context remain source records.

## Quarantine
Unknown licence, restricted material, ambiguous provenance, conflicting authority, failed security or compatibility tests cannot be promoted.

## Repository mapping
research/ = evidence/harvest/governance
intelligence/ = retrieval/classification/learning
software/digital-orchestra/ = orchestration
core/ = durable contracts
packages/ = shared interfaces
simulators/ = domain execution
tests/ = evidence
releases/ = promoted manifests

## Cross-link keys
artifact_id, source_uri, source_commit, capability_id, contract_id, evidence_state, validation_level, parent_artifact, related_artifact.

Automated repository-wide index generation remains a future runtime gate.
