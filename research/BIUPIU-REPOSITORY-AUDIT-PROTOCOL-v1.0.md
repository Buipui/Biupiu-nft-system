# Biupiu Repository Audit Protocol v1.0

**Effective:** 19 September 2026
**Purpose:** Make repository audits measurable for both the owner and the Biupiu learning/algorithm layer.

## Audit lifecycle

DISCOVERED -> ISOLATED -> MAPPED -> IMPLEMENTED -> TESTED -> VERIFIED -> INTEGRATED -> PROMOTION-CANDIDATE -> RELEASED

An item must not be labelled IMPLEMENTED merely because it was researched or indexed.

## Required audit fields

- Audit ID
- Date
- Source/repository
- Resource or change
- Licence status
- Department/project mappings
- Algorithm ID/version where applicable
- Files changed
- Functionality added
- Tests run
- Verification result
- Dependencies
- Security/IP status
- Commercial/private boundary
- Previous state
- New state
- Next gate
- Commit SHA
- Human approval requirement

## Rules

1. Preserve historical audit records.
2. Never silently replace an earlier algorithm version.
3. Separate research evidence from implementation evidence.
4. Record failed tests and unresolved conflicts.
5. Do not claim runtime/model execution unless it actually occurred.
6. Third-party code remains external until licence and security review passes.
7. Private R&D cannot be promoted automatically.
8. Production/customer-facing changes require explicit release approval.

## Standard audit sequence

Repository snapshot -> change detection -> dependency/licence scan -> resource isolation -> department mapping -> implementation -> tests -> verification -> index update -> progress record -> commit/read-back -> next gate
