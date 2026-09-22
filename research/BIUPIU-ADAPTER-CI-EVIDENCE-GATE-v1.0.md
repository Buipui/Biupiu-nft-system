# Biupiu Adapter CI Evidence Gate v1.0

Status: IMPLEMENTED — workflow registered; execution evidence pending.

## Purpose
Run the deterministic repository validator in GitHub Actions without claiming third-party runtime validation.

## Evidence requirements
A CI PASS must include:
- workflow run identifier;
- commit SHA;
- runner/toolchain information;
- validator stdout/stderr;
- exit code;
- successful manifest/fixture checks.

Third-party SUNDIALS/Open3D/Assimp/Gazebo/Chrono execution remains a separate gate.

## Failure handling
Any validator failure blocks promotion beyond repository validation. No external resource is promoted merely because the workflow file exists.
