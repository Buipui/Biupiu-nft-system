# Biupiu Open-Source Simulation Integration Gate v1.0

## Purpose
Convert useful open-source simulator capabilities into reusable Biupiu interfaces without blindly copying third-party source.

## Selected upstream references
- Gazebo gz-sim — simulation orchestration.
- ros_gz — ROS/ROS2 to Gazebo integration.
- GaussianRenderer — 3D Gaussian Splatting rendering research.
- gs-real2sim — Real2Sim research.
- DLR OAISYS — Blender/simulation research.
- rbot — AMR/ROS2/Gazebo research.

## Integration rule
Biupiu incorporates adapter functionality, not unreviewed upstream source. Upstream projects remain independently updateable and their licences/provenance remain visible.

## Adapter responsibilities
1. Detect whether a validated backend is installed.
2. Expose normalized backend status.
3. Construct argument-safe commands.
4. Reject unsafe arguments.
5. Never execute an external backend automatically.
6. Keep backend selection replaceable.
7. Preserve external repository provenance.

## Routing
Intelligence discovery -> repository registry -> licence/security gate -> adapter -> simulator -> telemetry -> Digital Twin -> validation -> authoritative OS

## Promotion
discovered-reference -> reviewed -> validated -> adapter-enabled -> production-approved

## Gate
SIM-OSS-01: ADAPTER LAYER IMPLEMENTED
