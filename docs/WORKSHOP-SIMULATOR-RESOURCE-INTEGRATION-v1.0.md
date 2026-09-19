# Workshop Simulator Resource Integration v1.0

## Research outcome
The research pass identified useful open-source references for mechanic simulation, vehicle physics, diagnostics and Unreal-based validation. The strongest architectural matches are CarMechanic, Automation DIY, SODA.Sim, CARLA/OpenADS, OAS-Engine and Rigs of Rods.

## What was integrated into Biupiu
- A license-aware external resource registry.
- A reusable workshop lifecycle.
- Automotive and hangar as the two reference implementations.
- Department-wide simulator registry.
- Shared component/procedure/measurement/fault/validation contracts.
- Digital-twin revision and provenance requirements.
- Failure-learning loop with verification gates.

## What was deliberately not copied
No third-party proprietary models, manufacturer manuals, textures, sounds or code were copied into the repository. External projects are used as research references pending license-by-license review.

## Next implementation gate
Connect these contracts to the existing UE5 asset-generation/digital-twin work, then create department adapters and automated tests before introducing large third-party dependencies.
