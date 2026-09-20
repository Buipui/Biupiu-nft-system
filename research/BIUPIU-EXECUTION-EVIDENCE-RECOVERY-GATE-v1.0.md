# Execution Evidence Recovery Gate v1.0

Status: RECOVERY — prior execution-evidence branch returned API 404 on read-back.

Recovery procedure:
1. Confirm base branch exists.
2. Recreate evidence artifact from confirmed base.
3. Read back the artifact immediately.
4. Do not infer execution success from creation.
5. Query workflow evidence separately.

No runtime promotion is allowed without actual runner evidence.
