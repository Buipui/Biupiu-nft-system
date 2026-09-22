# Biupiu UI Semantic Action Contract v1.0

Status: IMPLEMENTED — source-level contract anchor

## Purpose
Defines the semantic contract between UI actions, routing, module ownership, and governed execution.

## Action pipeline
UI observation -> semantic action ID -> route validation -> ownership check -> policy/evidence validation -> execution proposal -> independent validation -> learning evidence.

## Required action properties
- Stable action identifier.
- Owning module/department.
- Explicit target/state transition.
- Provenance or source reference where applicable.
- Validation result before governed promotion.
- Correlation/trace identifier for cross-system actions.

## Safety boundary
UI events are requests, not authority. Presentation-layer actions must not bypass Core OS/DMS validation, evidence gates, security checks, or human-approval requirements.

## Semantic equivalence
Equivalent actions across Android, web, desktop, and other clients must resolve to the same governed action meaning, acceptance/rejection class, state transition, and error class within declared version and tolerance.

## Verification boundary
This document is a source-level integration anchor. It does not certify Android devices, hardware, GPU/UE5 runtime, physical systems, or production release behavior.
