# Failure Learning Gate v1.1

Status: IMPLEMENTED — repository integration complete.

## Purpose
Capture failed simulator executions as structured evidence so recurring failure signatures can be identified without silently modifying scientific models.

## Recorded fields
- execution ID
- module
- failure category
- deterministic failure signature
- warning/issue list
- input digest

## Governance
- Successful executions are not recorded as failures.
- Repeated signatures are surfaced as recurring.
- Recurrence is evidence for investigation, not proof of causation.
- The store does not automatically change scientific models, parameters, or remediation logic.

## Verification
Unit tests cover repeated physics failures and successful execution exclusion.

Next gate: persistent failure history, signature clustering, remediation proposals, and explicit human approval workflow.
