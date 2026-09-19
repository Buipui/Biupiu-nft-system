# Biupiu Bevy Adapter v1.1

Original Biupiu integration boundary for Bevy as an optional Rust runtime inside Biupiu OS simulation workflows.

## OS-SIM kernel

The adapter provides simulation identity, entity registration, start/pause/step controls, deterministic ticks, measurement capture, simulation events, a Bevy plugin boundary and deterministic replay tests.

The kernel is renderer- and domain-neutral. Automotive, aerospace, marine, agriculture, robotics and manufacturing models enter through versioned adapters rather than modifying the OS core.

## Safety boundaries

- Simulation is explicitly started.
- Duplicate entity identifiers are rejected.
- Measurements for unknown entities are rejected.
- Third-party engines and assets are not copied into the repository by this adapter.
- Physical actuation and hardware-in-the-loop remain outside this core until separately validated.
- Source-level tests are not equivalent to connected GPU, runtime or physical validation.

## Validation

Use cargo test with the adapter manifest on a connected Rust host. Until CI or a connected-host result is observed, runtime execution remains NOT VERIFIED.
