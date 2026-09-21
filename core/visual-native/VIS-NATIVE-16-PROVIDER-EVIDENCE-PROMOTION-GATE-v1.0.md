# VIS-NATIVE-16 — Provider Evidence and Promotion Gate v1.0

Status: SOURCE IMPLEMENTATION COMPLETE / HOST EXECUTION IN PROGRESS

## Implemented
- Provider validation now invokes the native adapter instead of treating supplied canonical text as runtime evidence.
- Captures discovered, linked, runtime_probe, repeat_hash and repeat_pass.
- Promotion states are fail-closed:
  - 1 CONTRACT_ONLY
  - 2 HOST_READY
  - 3 REGRESSION_PASS
- Repeated provider execution must produce identical canonical bytes before REGRESSION_PASS.
- Validation smoke now checks runtime evidence for linked OpenUSD and preserves CONTRACT_ONLY behavior when unavailable.

## Evidence policy
No provider is promoted merely because a compile definition exists. Runtime execution and repeated deterministic output are required.

## Current limitation
The repository connector has not supplied a completed workflow result for this latest commit yet. Therefore VERIFIED is not claimed.

## Next gate
VIS-NATIVE-17 — CI/provider matrix reporting and persisted evidence artifacts, including explicit PASS/FAIL/SKIPPED results for each optional SDK.
