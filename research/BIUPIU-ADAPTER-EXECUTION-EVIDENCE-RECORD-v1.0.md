# Adapter Execution Evidence Record v1.0

State: PENDING_EXECUTION

This record is intentionally non-authoritative until populated by an actual supported runner.

Required fields:
- workflow_run_id: PENDING
- commit_sha: PENDING
- runner_os: PENDING
- python_version: PENDING
- stdout: PENDING
- stderr: PENDING
- exit_code: PENDING
- validator_result: PENDING

Classification rules:
- Repository read-back is not execution evidence.
- Workflow definition is not execution evidence.
- OFFLINE-REPOSITORY-PASS does not imply external runtime PASS.
- Missing evidence blocks promotion.
