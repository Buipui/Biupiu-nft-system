# Adapter Validator Execution Gate v1.0

Status: IMPLEMENTED — validator added; external runtime still pending.

The validator checks:
- five manifests exist and are valid JSON;
- manifest/test-vector identifiers match;
- provenance/licence/security/promotion fields exist;
- external resources cannot claim OS authority;
- four JSON fixtures parse;
- Assimp OBJ contains exactly 3 vertices and 1 face;
- SUNDIALS analytic reference equals exp(-k*t) within declared tolerance.

This is repository-level validation only. It does not execute SUNDIALS, Open3D, Assimp, Gazebo, or Project Chrono.

Runtime PASS remains gated on an actual supported runner with stdout/stderr, toolchain versions, dependency versions, commit SHA and exit code.
