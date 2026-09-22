# Biupiu Adapter Manifest + Fixture Verification Matrix v1.0

Date: 20 September 2026
Status: IMPLEMENTED — repository-level specification validation; external runtime pending

| Resource | Manifest | Fixture | Deterministic reference | External runtime |
|---|---|---|---|---|
| SUNDIALS | IMPLEMENTED | IMPLEMENTED | 0.3678794412 | PENDING |
| Open3D | IMPLEMENTED | IMPLEMENTED | centroid/bounds | PENDING |
| Assimp | IMPLEMENTED | IMPLEMENTED | 3 vertices / 1 face | PENDING |
| Gazebo | IMPLEMENTED | IMPLEMENTED | gravity/reset contract | PENDING |
| Project Chrono | IMPLEMENTED | IMPLEMENTED | omega=2 rad/s | PENDING |

## Gate controls
1. Manifest and fixture identifiers must match.
2. Provenance and licence boundary are mandatory.
3. No fixture grants OS authority.
4. Unsupported or malformed input must fail closed.
5. Runtime PASS is forbidden without captured execution evidence.

## Multi-AI review
- Architect: interface fields and authority boundary retained.
- Code: manifests/fixtures are minimal and machine-readable.
- Verification: deterministic reference values are explicit.
- Security: no executable third-party payloads or privileged operations introduced.
- Research: licence state remains external/pinned-required; no ownership implied.
- Integration: manifests map to existing test-vector IDs and promotion states.

## Gate result
Repository specification/fixture layer: IMPLEMENTED.
Third-party runtime validation: PENDING.
