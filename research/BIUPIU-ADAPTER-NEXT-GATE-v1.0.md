# Biupiu Adapter Next Gate v1.0

## Runtime Sandbox Gate

Required sequence:
REPRODUCE -> ISOLATE -> SANDBOX -> EXECUTE -> CAPTURE EVIDENCE -> VERIFY -> PROMOTE

Required evidence:
resource version/commit, licence state, dependency/toolchain versions, fixture hash, stdout, stderr, exit code, deterministic result, timeout/resource limits.

Fail-closed conditions:
missing provenance, ambiguous licence, unavailable dependency, unsupported privilege, malformed result, nondeterministic result, or missing evidence.

Current state:
Repository CI validation is verified; third-party runtime remains pending.
