# Biupiu Godot × MIT × GitHub Integration v1.0

Date: 2026-09-19

## Purpose
Integrate Godot as a repository-backed simulation/visualisation adapter for Biupiu OS, Digital Twin, graphics, robotics, aerospace, marine, automotive, workshop and showreel systems without making Godot the authoritative system of record.

## Reviewed source set
- Godot Engine: https://github.com/godotengine/godot — MIT.
- Official Godot demos: https://github.com/godotengine/godot-demo-projects — MIT.
- Godot TPS demo: https://github.com/godotengine/tps-demo — mixed licensing; code MIT, assets separately licensed.
- Godot licence guidance: https://docs.godotengine.org/en/latest/about/complying_with_licenses.html
- MIT 2.12 Introduction to Robotics — actuators, control, sensors, kinematics, dynamics, vision, navigation and system integration.
- MIT 6.801 Machine Vision — image formation, motion vision, filtering, photogrammetry/stereo and computational vision.
- MIT 6-4210 Robotic Manipulation — perception, 3D geometry, planning, kinematics, trajectory generation, dynamics and control.
- MIT 16.412J Cognitive Robotics — monitoring, scheduling, planning, multi-agent collaboration, risk and autonomy.
- MIT ACL GitHub: https://github.com/mit-acl — planning, localisation, trajectory optimisation and verification research.
- MIT RSS GitHub: https://github.com/mit-rss — ROS, visual servoing, localisation and path-planning course resources.

## Integration rule
Third-party code is not copied into Biupiu merely by indexing it. Only resources whose licence, provenance, dependency and security gates pass may be vendored or adapted.

Godot is an adapter/runtime target beneath Biupiu OS contracts.

## Architecture
Biupiu OS -> Godot adapter -> Godot runtime
                         -> Digital Twin scene
                         -> robotics/vehicle visualisation
                         -> workshop/hangar scenarios
                         -> synthetic-data/render jobs
                         -> showreel/export targets

Biupiu AI -> OS validation/audit -> Godot adapter -> runtime

Godot must not bypass authoritative provenance, access-control, audit or release gates.

## Capability map
- scene
- physics
- robotics
- xr
- compute
- networking
- mobile
- render
- provenance

## Asset/licence boundary
Godot engine code and official demo-project code can be considered for MIT-compatible integration subject to preserving notices. Third-party demo assets are never assumed MIT. Every asset retains its upstream licence and attribution.

## Gate
**GODOT-MIT-01: EXECUTED — Godot source set, official demos, MIT resources, licence boundary, capability mapping and executable adapter contract registered.**

Runtime compilation, Godot editor execution, scene import and hardware/GPU validation remain environment-validation gates.
