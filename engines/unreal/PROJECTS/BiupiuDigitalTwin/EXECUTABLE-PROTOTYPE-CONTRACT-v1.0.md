# Biupiu Digital Twin Executable Prototype Contract v1.0

## Prototype target
BL-01 Blade Micro-Turbine digital-twin visualization with a single versioned simulation-result fixture.

## Required runtime entities
- TwinEntity actor
- TwinMetadata component
- Provenance component
- SimulationResult component
- Optional Telemetry component for replay mode

## Required UI states
- Loading / schema validation
- Valid dataset
- Missing provenance
- Unsupported schema version
- Invalid units or incomplete result
- Replay / paused / completed

## Acceptance checks
1. Entity ID and schema version are visible.
2. Source dataset and commit are traceable.
3. Units and validation state are shown.
4. Invalid or incomplete data is rejected visibly.
5. The scene cannot imply engineering validation beyond the source dataset.

## Implementation boundary
This contract is intended to be implemented as native UE5 C++/Blueprint code in a licensed local UE environment. No generated UE binaries are committed by this gate.
