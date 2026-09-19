# Biupiu UE5 Visual Asset Bridge v1.0

## Purpose

Connect the UE5 asset pipeline to the repository's existing visual-asset manifest and provenance system without making Unreal the engineering source of truth.

## Contract

The existing visual-asset manifest remains authoritative for source, licence, provenance, files, pipeline and Biupiu cross-links. UE5 metadata adds destination-specific information.

Mapping:
- visual manifest asset_id -> UE asset_id
- visual manifest source -> UE source
- visual manifest licence -> UE IP status
- visual manifest provenance -> UE provenance
- visual manifest pipeline.targets -> UE targets
- visual manifest biupiu_links -> UE department/project links
- UE asset_path -> destination Content Browser path

## Import boundary

Unreal's Interchange Framework is the controlled import boundary. Interchange is customizable and supports C++, Blueprint and Python pipelines. The bridge records the import contract and provenance instead of embedding machine-specific editor state. 

## Asset discovery

After import, Unreal's Asset Registry can discover and validate project assets. Repository metadata remains the provenance authority.

## Safety rules

1. Never overwrite a source-of-truth asset merely because an UE export exists.
2. Do not place unverified, restricted or excluded source material into distributable builds.
3. Preserve source revision and transformation history.
4. Keep large generated UE binaries out of Git.
5. Treat engine-version changes as validation events.

## Gate

The bridge passes when a visual manifest is syntactically valid, its UE destination is resolvable, licence/provenance fields exist, and the corresponding UE asset can be discovered by Asset Registry on a configured workstation.
