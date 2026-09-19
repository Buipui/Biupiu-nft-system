# UE5 Native Prototype Gate v1.0

## Scope

This gate adds the first native Unreal Engine module descriptors, Build.cs files, a `TwinEntityActor` C++ baseline, and a synthetic BL-01 replay fixture.

## Implemented

- `BiupiuDigitalTwin` runtime plugin descriptor and module rules.
- `ATwinEntityActor` with entity ID, schema version, and provenance status properties.
- `BiupiuSimulation` runtime plugin descriptor and module rules.
- BL-01 synthetic replay fixture with explicit units and validation state.

## Epic Games / Unreal access

A valid Epic Games account is useful for accessing the Unreal Engine launcher, source access where eligible, and local engine installation. The repository does not store Unreal Engine source code or credentials.

## Verification boundary

Repository files have been created, but compilation, editor loading, Blueprint validation, packaging, and runtime playback must be executed in the user's licensed local Unreal Engine environment. The fixture is synthetic and is not engineering validation.

## Next gate

Create a minimal `.uproject`, register both plugins, run a local Development Editor build, load the fixture, and attach the build log plus test evidence.
