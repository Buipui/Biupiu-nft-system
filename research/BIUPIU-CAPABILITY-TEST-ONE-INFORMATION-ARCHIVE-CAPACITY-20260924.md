# BIUPIU CAPABILITY TEST ONE — INFORMATION ARCHIVE CAPACITY

**Task-ID:** CAP-ARCHIVE-001-20260924  
**Protocol:** BPU.PROTOCOL.QAISP.MI.1.0  
**Purpose:** First governed capability test for cataloguing repository information into the multidimensional metadata/knowledge-graph model and determining measurable information-storage capacity.

## Test objective
Use the native Biupiu information architecture to represent repository knowledge without treating the chat transcript as the authoritative store.

### Native pipeline
Repository Source -> DigiCat Discovery -> QAISP Metadata -> Multidimensional Graph -> DigiFile Evidence -> Hash/Manifest -> Optional Blockchain Commitment

## What is being measured
1. Source inventory capacity — number of repository artifacts that can be catalogued.
2. Metadata capacity — number of metadata fields/relations represented per artifact.
3. Graph capacity — number of nodes and typed edges representable by the schema.
4. Evidence capacity — provenance, hashes, tests, uncertainty and validation records per object.
5. Lineage capacity — parent/child/supersession relationships.
6. Quantum/physics capacity — equations, models, assumptions, simulations, classical baselines and QPU evidence states.
7. Archive commitment capacity — deterministic manifest and graph-root hashes suitable for blockchain anchoring.

## Test One archive unit
An Archive Unit = 1 source object + metadata record + graph node set + typed relationships + evidence/provenance references + content hash + lineage + validation state.

An Archive Unit does not require the source payload itself to be copied into the graph. Large/private/raw objects can remain in authoritative storage while the graph stores metadata, identifiers, hashes and references.

## Native capacity model
For a repository containing N source objects:
- Minimum graph nodes: N.
- Actual graph nodes: N + entity/concept/evidence/system/experiment nodes.
- Graph edges: E, where each relationship is independently typed and attributable.
- Metadata records: M, where M >= N.
- Evidence records: V, where V >= 0 and may exceed N because one object can have multiple evidence events.
- Lineage records: L, where L >= 0.
- Manifest size is proportional to the number and complexity of indexed objects, not to the raw scientific information represented by them.

## Test One execution boundary
The accessible GitHub connector was used as the canonical repository interface for this test.
The current tool path does not expose a complete recursive repository byte/object inventory in one operation. Therefore this first archive test records the capability and evidence model without inventing a total repository byte count.

### Evidence state
- QAISP protocol: SOURCE IMPLEMENTED
- Machine-readable QAISP schema: SOURCE IMPLEMENTED
- Archive capability specification: REGISTERED
- Repository-wide recursive byte count: OPEN
- Complete repository graph materialization: OPEN
- Local filesystem capacity benchmark: OPEN
- Database/graph-engine benchmark: OPEN
- Live blockchain anchoring benchmark: OPEN
- QPU execution: NOT REQUIRED FOR THIS TEST

## Capacity interpretation
This test establishes that the architecture can treat repository information as a multidimensional graph with independently addressable metadata, provenance, evidence and lineage.
It does not establish a numerical maximum for the repository or graph database.

A future execution benchmark must record:
bytes_before -> objects_indexed -> metadata_records -> graph_nodes -> graph_edges -> bytes_after -> compression_ratio -> bytes_per_archive_unit -> indexing_time -> retrieval_time -> hash_time -> anchor_payload_size

From those measurements the native engine can calculate:
- archive_density = archive_units / stored_bytes
- metadata_density = metadata_fields / archive_unit
- graph_density = graph_edges / graph_nodes
- evidence_density = evidence_records / archive_unit

## Safety/governance
- No information is deleted to improve the graph.
- Superseded information remains linked through lineage.
- Translation is not validation.
- Metadata extraction is not scientific verification.
- A hash is an integrity identifier, not proof of truth.
- Blockchain anchoring is a commitment, not scientific validation.
- Quantum simulation is not QPU evidence.
- Unknown/conflicting information remains explicitly classified.
- Private/confidential/raw research remains outside public blockchain payloads.

## Archive target
TEST ONE = establish the canonical Archive Unit, capacity metrics and measurement contract before attempting a full repository archive.

**Status:** REGISTERED / PROTOCOL-ALIGNED / MEASUREMENT OPEN