# Biupiu Intelligence Architecture v1.3
Date: 2026-09-19

This v1.3 extension adds Microsoft Discovery-compatible task-graph orchestration to the existing v1.2 architecture.

The task graph is subordinate to Biupiu evidence, provenance and human promotion controls.

New operating loop:
INTAKE -> DECOMPOSE -> BUILD TASK GRAPH -> RETRIEVE -> CROSS-LINK -> IDENTIFY GAPS/CONTRADICTIONS -> ROUTE SPECIALIST -> SIMULATE/EXPERIMENT -> EVALUATE -> LEARN -> PROMOTE

Failed, incomplete, stale and contradicted branches remain visible and queryable rather than being silently discarded.

External tools remain blocked until licence/provenance/security review. Irreversible actions require the existing human-controlled OS boundary.

Implementation module: software/rnd-os-ai/src/biupiu_ai/discovery_architecture.py
