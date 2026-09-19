# Biupiu Intelligence Layer v1.0

## Purpose
A repository-native intelligence layer that converts indexed evidence into research questions, cross-links, evidence-gap analysis and proposed next tests.

## Required outputs
- evidence state
- known/unknown distinction
- related research objects
- prior tests and failures
- cross-department overlaps
- candidate experiments
- data gaps
- IP-review flags
- next-action queue

## Guardrails
The intelligence layer must preserve provenance, identify uncertainty, distinguish sourced facts from inference, and never present an unperformed experiment as a completed result.

## Initial query families
`WHAT-IS-KNOWN`, `WHAT-IS-UNKNOWN`, `WHAT-FAILED`, `WHAT-CAN-BE-TESTED`, `WHAT-OVERLAPS`, `WHAT-IS-NOVEL`, `WHAT-NEEDS-IP-REVIEW`, `WHAT-NEEDS-REPLICATION`.

## Multitask-safe development protocol — 2026-09-19

### 1. Repository as authoritative archive
The repository is the durable project record. Chat is treated as an active workspace, not the authoritative long-term archive. Completed work must be registered in the repository before the related chat is considered ready for closure.

### 2. Gate lifecycle
Every active project/workstream should expose an explicit state:
- `IN-PROGRESS`: gates remain outstanding.
- `IMPLEMENTED`: changes have been made but verification is incomplete.
- `COMPLETE-ALL-GATES-PASSED`: implementation, integration, validation, indexing/registration and repository persistence have all been verified.
- `DEFERRED`: intentionally postponed.
- `BLOCKED`: an external dependency or unresolved defect prevents completion.

A project must not be marked complete merely because code or documentation was written.

### 3. Multitask-safe cross-task bug fixing
When workstreams overlap, fixes may be applied across tasks only when the change is demonstrably compatible with existing contracts and does not silently remove or overwrite unrelated functionality.

Cross-task fixes must:
1. identify the affected module(s);
2. preserve existing interfaces unless a deliberate versioned change is required;
3. check dependent paths/contracts;
4. record the reason for the change;
5. register the change against every affected workstream;
6. leave unresolved conflicts visible rather than masking them.

### 4. Conflict-resolution and learning preservation
After a task reaches implementation/validation, conflicts should be resolved deliberately rather than by destructive cleanup. Preserve:
- the original problem;
- the attempted solution;
- observed failure or compatibility issue;
- resolution;
- affected modules;
- verification status;
- lessons that should influence future development.

This information is intelligence-layer data and should remain queryable rather than being lost in chat history.

### 5. Change logging
Material architectural, integration, bug-fix, gate, compatibility and workflow decisions should be logged in the repository. Logs should favor structured facts and provenance over conversational narrative.

Each meaningful entry should capture, where available:
- timestamp/date;
- workstream;
- change;
- rationale;
- affected components;
- dependencies;
- validation performed;
- unresolved risks;
- gate state;
- next action;
- commit/reference identifier.

### 6. Chat closure rule
When a project is `COMPLETE-ALL-GATES-PASSED` and its final state/index/changes are registered in the repository, the active chat may be closed and a fresh chat started. The completion message should explicitly state that all gates have passed and the repository contains the durable record.

### 7. Integrity rule
Do not claim that a gate, test, repository write, build, or integration has succeeded unless it has actually been performed and verified. If a tool or environment prevents verification, record the state as incomplete or blocked.

## Current protocol registration — 2026-09-19
The user requested that multitasking be treated as a normal operating mode. Cross-task bug fixes should be conservative and compatibility-aware while other work is active. After a task is completed, conflicts should be resolved deliberately so that the system's accumulated learning is preserved.

The current operational change is registered here as an intelligence-system process update. No unperformed code/test result is being represented as completed.

## Repository context observed during registration
The active repository is `Buipui/Biupiu-nft-system`, default branch `main`. The repository already contains intelligence-layer, DMS, modular runtime, application, research, smart-farming and world-development structures, including multiple validation workflows. This document extends the intelligence-layer operating rules without declaring those broader workstreams complete.

## Next-action queue
- Apply this gate/state protocol consistently to active workstreams.
- Register material cross-task fixes in the repository as they occur.
- Preserve conflict history and learning outcomes during reconciliation.
- Close chats only after the relevant project reaches `COMPLETE-ALL-GATES-PASSED` with repository registration and verification.
