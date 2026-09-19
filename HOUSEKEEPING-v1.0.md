# Biupiu Repository Housekeeping v1.0

**Date:** 2026-09-19  
**Purpose:** Establish a repeatable housekeeping, bug-extermination, research-cleanup and release-integrity gate.

## Scope

This gate covers:
- repository structure and machine-readable metadata hygiene;
- duplicate/stale/ambiguous research records;
- TODO/FIXME tracking without modifying third-party/vendor code;
- Python/JavaScript/TypeScript/Kotlin/JSON/Markdown hygiene checks;
- provenance and version metadata preservation;
- audit-log integrity;
- release/index consistency;
- explicit separation of verified facts, research leads, assumptions and visualization-only material.

## Safety boundaries

Housekeeping must not silently delete research or vendor material. Suspected duplicates, stale records and conflicts are reported for review. Third-party/vendor code is not modified merely because it contains TODO comments.

No visual render is treated as engineering evidence unless an appropriate validated simulation or physical test provides that evidence.

## Required housekeeping result

Each release should record:
1. repository state checked;
2. checks executed;
3. findings;
4. fixes actually applied;
5. unresolved items;
6. provenance/research updates;
7. next recommended gate.

## Release principle

The repository is cumulative: historical material remains discoverable while current material is versioned and linked. New information should update or supersede prior records only when provenance and evidence support the change.
