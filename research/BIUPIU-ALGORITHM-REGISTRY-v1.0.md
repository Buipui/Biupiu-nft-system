# Biupiu Algorithm Registry v1.0

**Updated:** 16 September 2026  
**Rule:** historical algorithm records are immutable; improvements create new versions.

| Algorithm ID | Version | Research | NFT/Release | Domain | Status |
|---|---|---|---|---|---|
| BIU-ALG-GEO-FLOW-001 | 0.1.0 | BIU-ANC-001 / BIU-GEO-001 | BIU-NFT-0001 / ORIGIN-001 | Computational flow geometry | Prototype |

## Registration fields for future algorithms

- Algorithm ID
- Semantic version
- Parent algorithm/version, if forked or evolved
- Research ID(s)
- NFT/release ID(s)
- Domain and geometry family
- Source repository path
- Git commit
- Dependencies
- Parameters schema
- Seed policy
- Input-data references
- Evidence status
- Validation status
- Output formats
- Asset hash(es)
- Metadata/release-manifest hash
- Licence/IP status
- Created/updated date

## Versioning policy

- **PATCH**: implementation correction that does not intentionally alter the algorithmic model; regenerate/revalidate affected artifacts as required.
- **MINOR**: backward-compatible algorithm capability or parameter/model extension.
- **MAJOR**: materially different algorithmic model or incompatible generation lineage.

A released NFT always points to the exact algorithm version used for generation. Never replace a historical version in place.

## First registered family

`BIU-ALG-GEO-FLOW-001` is the network's first algorithm family. It is the registered lineage of the ORIGIN-001 `FLOW-GEOMETRY-001` prototype. The current implementation remains explicitly an artistic/computational scaffold and not an archaeological validation.
