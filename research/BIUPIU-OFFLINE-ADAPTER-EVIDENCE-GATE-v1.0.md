# Offline Adapter Evidence Gate v1.0

Purpose: provide an executable validation path independent of GitHub Actions availability.

The validator checks the repository-owned manifests and deterministic fixtures only. It deliberately does not import or execute SUNDIALS, Open3D, Assimp, Gazebo, or Project Chrono.

Evidence classification:
- OFFLINE-REPOSITORY-PASS: valid only for repository-owned validation.
- CI-PASS: requires GitHub Actions run evidence.
- RUNTIME-PASS: requires actual third-party toolchain execution evidence.

Promotion rule: OFFLINE-REPOSITORY-PASS cannot promote an external adapter to runtime VERIFIED.
