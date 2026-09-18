# Premiere Pro Adapter

## Target

Premiere Pro UXP is the primary integration target for new development. Adobe's official UXP sample repository is the reference implementation.

## Planned Biupiu commands

- create/open project
- import registered media
- assemble sequence
- place markers
- attach research/evidence metadata
- ingest transcript data
- export/render
- return output hash and provenance record

Legacy CEP/PProPanel examples may inform compatibility work but are not the default architecture.

## Validation gate

No live execution is claimed until a local Premiere Pro + UXP Developer Tool environment is available and the adapter passes import → sequence → export → hash verification.
