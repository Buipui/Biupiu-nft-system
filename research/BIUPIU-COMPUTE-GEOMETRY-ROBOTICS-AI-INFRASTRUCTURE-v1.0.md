# BIUPIU COMPUTE / GEOMETRY / ROBOTICS / AI INFRASTRUCTURE UPGRADE v1.0

**Date:** 19 September 2026  
**Status:** Active architecture

## Objective

Strengthen the shared computational foundation so computational geometry, robotics, AI, mathematics and digital twins can exchange models without creating disconnected implementations.

## Architecture

`MATH → COMPUTE → GEOMETRY → AI → ROBOTICS → DIGITAL-TWIN → EXPERIMENT → LEARNING`

with shared provenance, testing, dependency and safety gates.

## Computational geometry upgrade

Add a geometry capability layer covering:

- robust 2D/3D primitives;
- triangulation and tessellation;
- Voronoi/Delaunay methods;
- convex hulls;
- mesh generation/remeshing;
- Boolean geometry;
- point clouds and spatial indexing;
- signed/implicit geometry;
- topology and manifold checks;
- parametric CAD representations;
- geometry-to-physics interfaces.

CGAL is the principal external reference for robust computational-geometry algorithms. Its current release information lists CGAL 6.2.1 as stable and 6.1.3 as a September 2026 release. Licence boundaries must be checked before redistribution.

## Robotics upgrade

Create a common robotics adapter boundary for:

- robot description/state;
- kinematics and inverse kinematics;
- dynamics;
- collision checking;
- motion planning;
- trajectory generation;
- perception;
- localisation/mapping;
- navigation;
- actuator/control interfaces;
- simulation-to-real calibration.

MoveIt 2 is the primary manipulation/kinematics reference and Nav2 the navigation reference. Both are open-source frameworks with documented APIs and test infrastructure.

## AI upgrade

AI infrastructure should support:

- deterministic preprocessing;
- model registry and versioning;
- feature/data lineage;
- inference adapters;
- optimisation and surrogate-model interfaces;
- uncertainty and confidence records;
- experiment tracking;
- evaluation/benchmarking;
- human approval gates;
- rollback/version comparison.

The AI layer must preserve the existing FACT / MODEL_OUTPUT / HYPOTHESIS / SIMULATION_RESULT / MEASUREMENT / FAILURE distinctions.

## Infrastructure improvements

1. Shared schema/version contracts.
2. Stable adapter interfaces rather than wholesale third-party code copies.
3. Dependency manifests with licence/provenance.
4. Reproducible environment declarations.
5. Unit, integration and smoke-test gates.
6. Deterministic seeds where stochastic tests permit.
7. Input/output validation at department boundaries.
8. Read-only research ingestion before promotion.
9. Digital-twin interfaces for sensor/model/telemetry exchange.
10. Automatic repository housekeeping on changes.
11. Clear separation of private R&D, public research and customer-facing systems.
12. Rollback-safe releases.

## External-resource rule

Third-party repositories are **reference/dependency candidates**, not automatic imports. Code can enter the executable stack only after licence, provenance, security, dependency and compatibility checks.

## No-brick rule

A new dependency must not replace a working internal implementation until:

- compatibility is demonstrated;
- regression tests pass;
- rollback path exists;
- provenance is recorded.

## Integration targets

- `codex/geometry/`
- `codex/math/`
- `codex/ai/`
- `codex/robotics/`
- `codex/digital_twin/`
- `research/`
- `private-rd-centre/`
- `simulators/`

## Result

This upgrade establishes MATH as the quantitative foundation and turns geometry, AI, robotics and digital twins into interoperable computational layers rather than isolated research streams.
