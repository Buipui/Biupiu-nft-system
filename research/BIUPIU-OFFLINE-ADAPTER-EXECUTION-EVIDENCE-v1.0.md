# Offline Adapter Execution Evidence v1.0

Status: EXECUTION GATE

This record is populated only by an actual supported runner. Until then all fields remain PENDING.

Required evidence:
- workflow_run_id
- commit_sha
- runner_os
- python_version
- stdout
- stderr
- exit_code
- validator_result

Classification:
OFFLINE-REPOSITORY-PASS = validator passes repository-owned checks.
CI-PASS = GitHub Actions reports successful execution.
RUNTIME-PASS = external adapter executes successfully with pinned dependency evidence.
