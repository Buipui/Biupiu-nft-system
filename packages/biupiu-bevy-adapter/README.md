# Biupiu Bevy Adapter v1.1

Optional Bevy runtime boundary for Biupiu OS simulation workflows.

## Kernel capabilities
- simulation identity and lifecycle;
- entity registration with duplicate protection;
- start/pause/step controls;
- deterministic ticks;
- measurement capture;
- simulation events;
- Bevy plugin boundary;
- deterministic replay regression coverage.

The kernel is renderer- and domain-neutral. Domain systems enter through versioned adapters.

## Safety
Simulation starts explicitly. Unknown measurement targets and duplicate entity IDs are rejected. Third-party engines/assets are not copied into this adapter. Physical actuation and hardware-in-the-loop require separate validation. Source tests do not prove connected GPU/runtime/physical execution.

## Validation
Use `cargo test --manifest-path packages/biupiu-bevy-adapter/Cargo.toml` on CI or a connected Rust host. Until an actual result exists, runtime status remains NOT VERIFIED.
