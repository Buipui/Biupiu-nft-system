# UE5 Native Bootstrap Test Plan v1.0

## Preconditions

- Epic Games account authenticated in Epic Games Launcher.
- Unreal Engine 5.6 installed locally.
- Repository cloned with the bootstrap project and plugins present.

## Test sequence

1. Open the `.uproject` file.
2. Generate project files.
3. Compile the development target.
4. Confirm both Biupiu plugins load without errors.
5. Open the editor and inspect the Output Log.
6. Load the BL-01 fixture through the planned data adapter.
7. Confirm invalid provenance and unsupported schema states are rejected.
8. Record results, logs, engine version, and commit SHA in the build manifest.

## Current status

All tests remain `NOT_RUN` until executed in the user's local Unreal Engine environment.
