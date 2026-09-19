# Biupiu Digital Twin — UE5 Bootstrap Setup v1.0

## Purpose

Provides the first project descriptor for local Unreal Engine verification.

## Local setup

1. Install Unreal Engine 5.6 through the Epic Games Launcher.
2. Clone the repository and open `BiupiuDigitalTwin.uproject`.
3. Confirm the `BiupiuDigitalTwin` and `BiupiuSimulation` plugins are detected.
4. Generate project files using the local Unreal Engine tooling.
5. Compile the project in an installed development environment.
6. Open the editor and validate plugin loading before adding scenes or assets.

## Boundaries

The descriptor is a bootstrap contract. Repository creation does not prove that the local engine version, plugin placement, compiler toolchain, or editor runtime are configured correctly. Record actual results in the build manifest after local testing.
