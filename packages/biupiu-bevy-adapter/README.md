# Biupiu Bevy Adapter v1.0

A small, original integration boundary for using Bevy as an optional Rust runtime inside Biupiu R&D and simulation workflows.

## Scope

The adapter exposes a Bevy Plugin entry point, a shared runtime state resource, a deterministic tick counter, a controlled message channel for simulation events, and a boundary where Digital Twin / simulator adapters can be attached later.

It deliberately does not copy Bevy source code or third-party plugins into the repository.

## Usage

Add this crate to a Rust workspace and add Bevy 0.19 as the engine dependency. The adapter can then be registered with:

    app.add_plugins(BiupiuBevyPlugin::default());

The adapter itself does not create a window, load third-party assets, access credentials, or claim that a physical simulator is connected.

## Intended departments

DIGITAL-TWIN, PHYS-SYS, CG-3D, GEOMETRY, AERO, MARINE, AUTO, ROBOTICS, ADV-MFG, AGRI, WATER, AI and COMPUTE.

## Validation

Compilation and runtime validation are separate gates. The repository currently records the source-level adapter as implemented; connected-host execution must be recorded before claiming runtime success.
