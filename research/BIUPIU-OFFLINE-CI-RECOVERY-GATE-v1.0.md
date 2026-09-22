# Offline CI Recovery Gate v1.0

Status: IMPLEMENTED — recovery workflow added.

Purpose: execute only repository-owned deterministic validation while keeping third-party runtime validation separate.

Required CI evidence: run ID, commit SHA, runner OS, Python version, stdout/stderr, exit code.

A successful offline validation is classified as OFFLINE-REPOSITORY-PASS, not runtime VERIFIED.
