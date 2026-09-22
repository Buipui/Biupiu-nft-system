# Biupiu Endpoint Attestation & Deployment Gate v1.0

Status: IMPLEMENTED — deployment evidence pending

## Purpose
Prepare a non-destructive evidence contract for running the Biupiu anti-malware validation gate on real authorized endpoints.

## Required endpoint record
- endpoint_id
- operator_id
- operating_system
- architecture
- hostname_or_asset_tag
- scanner_engine
- scanner_version
- signature_or_rule_version
- last_update_timestamp
- validation_timestamp
- workflow_run_id
- test_artifact: EICAR standard safe test string only
- detection_result
- event_ingestion_result
- quarantine_or_block_result
- recovery_result
- audit_event_hash
- final_gate_status

## Pass criteria
PASS requires measured evidence for engine availability, current rules, safe test detection, Biupiu event ingestion, quarantine/block, recovery, audit provenance, and clean-file regression.

Missing evidence MUST remain PENDING. No synthetic PASS values are permitted.

## Safety constraints
- Never download, execute, or store live malware.
- Use only the standard EICAR test artifact for endpoint detection validation.
- Do not delete files automatically.
- Quarantine is the default containment action.
- Endpoint deployment and testing require an authorized operator.
- This repository gate does not claim that an endpoint has been tested.

## Evidence states
- NOT_STARTED
- PENDING
- PASS
- FAIL
- BLOCKED

## Current state
Architecture and repository validation are implemented. Real endpoint deployment, EICAR execution, scanner telemetry, quarantine/recovery evidence, and independent assessment remain PENDING until an authorized endpoint runner supplies measured evidence.
