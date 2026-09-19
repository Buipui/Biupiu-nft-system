# Biupiu Review Decision Record v1.0

Gate 09 creates the auditable decision layer between render QA and downstream World/showreel integration.

## Decision states
- PENDING
- APPROVE
- REJECT
- REQUEST_CHANGES

## Required checks
- Visual quality/integrity
- Provenance
- Evidence/claim classification
- Asset rights/licensing

A human reviewer must record the decision and notes. The system does not infer approval from file existence or render completion.

## Downstream rule
Only an explicit APPROVE with all four checks PASS may move the package to READY_FOR_DOWNSTREAM.