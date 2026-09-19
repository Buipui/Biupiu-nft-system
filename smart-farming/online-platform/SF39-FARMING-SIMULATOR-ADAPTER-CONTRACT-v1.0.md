# SF39 — Farming Simulator Adapter Contract v1.0

## Purpose
Define a simulator-neutral contract so Farming Simulator resources can feed Biupiu Smart Farming without coupling the World to a proprietary runtime.

## Adapter stages
1. Discover external simulator/resource.
2. Verify source identity and licence.
3. Map source fields/actions to Biupiu canonical schema.
4. Validate units/ranges.
5. Apply policy and safety constraints.
6. Emit normalised telemetry.
7. Record provenance.
8. Run scenario validation.
9. Promote only validated results to Biupiu World.

## Canonical interfaces
- FarmStateProvider
- FieldStateProvider
- WeatherProvider
- SoilStateProvider
- MachineryStateProvider
- IrrigationController
- AutonomousTaskProvider
- ScenarioRunner
- TelemetryRecorder

## Fail-closed rules
Unknown fields are ignored rather than guessed. Invalid units/ranges reject a record. Unverified external assets cannot be promoted to World content. External commands cannot bypass the policy layer.

**Status: CONTRACT REGISTERED. Runtime implementation remains host-validation gated.**
