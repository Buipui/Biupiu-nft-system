# Biupiu Digital Filing Cabinet v1.0
Status: SOURCE IMPLEMENTED / RUNTIME INDEXER PENDING

A standalone filing subsystem for papers, datasets, code references, patents, technical documents and other resources. It is linked to Biupiu Intelligence, Digital Orchestra, Native Coding Matrix, OS/DMS, Digital Twin and Federation through contracts and identifiers, but remains independently governed.

Principle: linked systems, independent authority. The Cabinet owns filing/index metadata; source systems retain authority over their own artifacts.

Lifecycle:
INGEST -> IDENTIFY -> HASH -> CATALOGUE -> CLASSIFY -> CROSS-LINK -> VERIFY -> RETAIN/QUARANTINE

Canonical metadata:
artifact_id, title, artifact_type, authors, source_uri, source_commit, language, licence, publication_date, retrieved_at, domain, capability_ids, evidence_state, validation_level, implementation_state, authority_system, parent_id, related_ids, supersedes, security_class, retention, notes.

Paper-specific fields:
DOI, journal, publisher, abstract_digest, keywords, citation_metadata.

Rules:
- Original source metadata is preserved.
- Language never determines trust.
- Unknown licence/provenance is quarantined.
- A catalogue record does not imply scientific validation.
- The Cabinet never becomes execution authority.
- Cross-links reference systems without merging their hierarchies.
