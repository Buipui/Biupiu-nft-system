# Open-Source Simulator Resource Audit — 2026-09-19

## Result
The audit identified usable open-source foundations and references for Biupiu World plus the independent department simulators.

### World integration
Bevy provides a modular data-oriented Rust engine, but its repository warns of active development and breaking API changes. It is therefore an optional runtime/technology reference rather than a mandatory replacement.

Godotiles provides large-world streaming, adaptive terrain LOD, altitude queries, fog/shadow handling and large-world shifting. This is relevant to a scalable World layer, subject to provider/imagery licensing.

Godot USD provides an OpenUSD interoperability path and smoke/regression testing. It is an interoperability reference, not a reason to duplicate the World asset store.

### Marine
VRX is Apache-2.0 and supports USV simulation. Current documentation recommends modern Gazebo Sim and ROS 2.

gz-maritime separates wave physics and rendering, including Gerstner and FFT wave providers. This maps directly to the Biupiu World requirement that the same sea state be shared consistently between visual rendering and simulation.

VORC provides another open maritime simulation foundation.

### Automotive
CARLA is an open-source autonomous-driving simulator and provides open digital assets for its intended research use. The RWTH CARLA fork provides a modular simulation-core reference.

### Cross-domain
The repository already contains a reusable physics-adapter concept at packages/biupiu-physics-engine/ and a private R&D physics kernel. The new matrix extends the existing architecture rather than replacing it.

## Legal and technical gate
Open source does not mean unrestricted asset reuse. Each repository/file still requires licence compatibility and provenance recording. Commercial games such as Farming Simulator, Assetto Corsa, BeamNG.drive and Microsoft Flight Simulator remain benchmarks unless their specific SDK/content licences permit the intended use.

## Implementation decision
Adopt architecture, APIs, schemas, adapters and permissively licensed code where compatible. Do not wholesale-copy third-party repositories or proprietary assets into Biupiu World.

## Next technical gate
Build World integration adapters and department manifests first. Then connect one validated vertical slice per department rather than attempting a monolithic simulator.
