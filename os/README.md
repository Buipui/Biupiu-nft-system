# Biupiu OS Core v0.1

First executable orchestration layer for Biupiu OS. This branch is intentionally isolated from main.

Implemented: deterministic kernel, capability registry, evidence guard, environment state, audit ledger, discovery of existing simulator modules, regression tests.

Integration targets: UE5 MassEntity, Unity Entities/DOTS, Project Chrono, Gazebo, OpenFOAM, hardware protocols and departmental simulators.

Verification rule: simulated/planned output cannot silently become validated/certified output. Native external-engine integrations remain unverified until their actual runtime and a repeatable test are available.

External open-source components stay behind adapters and retain their applicable licenses.
