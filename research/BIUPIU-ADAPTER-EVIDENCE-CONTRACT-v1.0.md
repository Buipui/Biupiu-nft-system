# Biupiu Adapter Evidence Contract v1.0

Status: IMPLEMENTED — evidence schema added.

A CI result may be promoted only when every required evidence field is populated from an actual workflow run.

Required:
- workflow run ID and name
- exact commit SHA
- runner OS
- toolchain versions
- validator stdout/stderr
- exit code
- manifest/fixture result

Empty, inferred, or manually asserted evidence is invalid.

## State machine
PENDING -> RUNNING -> PASSED | FAILED
PASSED + complete evidence -> REPOSITORY-VERIFIED
REPOSITORY-VERIFIED -> EXTERNAL-RUNTIME-PENDING

No CI record can promote SUNDIALS, Open3D, Assimp, Gazebo or Project Chrono to runtime VERIFIED status.
