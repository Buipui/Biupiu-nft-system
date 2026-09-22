# BIUPIU Adapter Specification + Deterministic Test Vector Gate v1.0

Date: 20 September 2026
Status: IMPLEMENTED — specification/test-vector layer; runtime execution pending

## Objective
Turn capability contracts into deterministic adapter specifications that can later be executed on a supported build runner without granting external resources OS authority.

## Common adapter contract
- input_schema
- output_schema
- units
- coordinate_frame
- version
- provenance
- licence_boundary
- dependency_manifest
- timeout/resource_limits
- error_contract
- deterministic_seed where applicable
- test_vector_id
- expected_result_tolerance
- evidence_location
- promotion_state

## Test vector families

### SUNDIALS
Capability: ODE/DAE/nonlinear/time integration.
Vector SUNDIALS-TV-001: exponential decay dy/dt=-k*y, y(0)=1, k=0.5, t=2.
Expected analytic result: y(2)=exp(-1)=0.3678794412.
Checks: solver convergence, tolerance handling, deterministic output, invalid-state handling.

### Open3D
Capability: point-cloud/3D geometry.
Vector OPEN3D-TV-001: four points forming a unit tetrahedral test set.
Checks: point count, centroid, bounding box, transform round-trip and deterministic serialization.

### Assimp
Capability: model import/interchange.
Vector ASSIMP-TV-001: minimal triangle mesh fixture with 3 vertices and 1 face.
Checks: vertex count, face count, normals/material presence where fixture provides them, import/export round-trip and malformed-file rejection.

### Gazebo
Capability: robotics/sensor/physics simulation.
Vector GAZEBO-TV-001: single rigid body in a gravity world with deterministic initial pose and zero initial velocity.
Checks: world load, physics step, gravity direction, pose evolution, sensor/message schema and deterministic reset.

### Project Chrono
Capability: multibody dynamics.
Vector CHRONO-TV-001: single mass-spring-damper system with known analytic response.
Checks: initial-condition acceptance, time integration, energy/response tolerance, deterministic repeated run and invalid-parameter rejection.

## Cross-disciplinary Digital Twin test
DT-TWIN-TV-001:
One canonical object is represented in geometry, physics, identity/provenance and telemetry layers.
Checks:
1. identifier remains stable;
2. units remain explicit;
3. coordinate frame is explicit;
4. source provenance survives adapter translation;
5. failed/unsupported fields fail closed;
6. downstream department routing does not change source authority.

## Security tests
SEC-ADAPTER-TV-001:
- attempt unsupported privilege request;
- attempt ambiguous licence state;
- attempt malformed schema;
- attempt out-of-range resource request;
- attempt provenance omission.

Expected result: reject/contain, emit structured error, preserve provenance and leave OS authority unchanged.

## Promotion rule
REFERENCE -> ADAPTER-READY -> SANDBOXED -> INTEGRATED -> VERIFIED -> PROMOTED

No executable promotion from this document alone.

## Runtime evidence rule
A test vector is PASS only when stdout/stderr, toolchain versions, dependency versions, commit SHA and exit code are captured from an actual supported runner.

Current status:
- specifications: IMPLEMENTED
- deterministic vectors: IMPLEMENTED
- runtime execution: PENDING
- CI execution: PENDING

## Next gate
Build the first machine-readable adapter manifests and fixture files, then run them on a supported runner.
