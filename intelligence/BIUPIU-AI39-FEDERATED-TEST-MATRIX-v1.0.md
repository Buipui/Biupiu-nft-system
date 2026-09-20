# Biupiu AI-39 Federated Executable Test Matrix v1.0

Date: 20 September 2026
Parent: AI-38
Status: IMPLEMENTED / LOCAL EXECUTION PENDING

## Purpose
Turn the AI-38 federation into one deterministic test surface using the existing Biupiu machine-capability simulator and its state/provenance boundaries.

## Matrix
| ID | Domain | Test | Expected |
|---|---|---|---|
| F01 | Machine Capability | repeated 22.5 degC sample | deterministic equality |
| F02 | State Authority | inspect sample state_class | simulated, never observed |
| F03 | Limits | sample 126 | ValueError |
| F04 | Actuation | request start | PermissionError |
| F05 | Type Safety | sample non-number | ValueError |
| F06 | Federation | validate AI-38 manifest pipeline | all required stages present |
| F07 | Boundary | simulated -> observed | prohibited |
| F08 | Provenance | promotion without runtime evidence | prohibited |
| F09 | Regression | repeat F01-F05 | same results |
| F10 | Physical Safety | live actuation/HIL | not executed |

## Evidence classes
PASS = executable test result captured.
BLOCKED = test cannot execute in the available environment.
FAIL = executable test ran and violated its expected contract.

Repository presence alone is not PASS.

## Promotion
AI-39 can be PROMOTION-READY only after executable evidence is captured for F01-F09. F10 remains deliberately NOT EXECUTED unless an explicitly authorized physical test environment exists.

## Next gate
AI-40: local deterministic federation runner + machine-readable result bundle, followed by repository regression and provenance record.
