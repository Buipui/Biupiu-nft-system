# Biupiu UE5 CI Runbook v1.0

## Automated repository gate

The GitHub Actions workflow "Biupiu UE5 Project Validation" validates the UE5 descriptor, plugin contract, UE5 metadata, visual-asset bridge, C++ source scaffold and generated-file exclusions.

## Workstation boundary

Repository CI is not an Unreal Engine workstation. It must not claim that the UE Editor, Visual Studio C++ toolchain, Asset Registry or Movie Render Queue has executed.

## Workstation execution sequence

1. Install a supported UE5 release and Visual Studio 2022 with Game development with C++.
2. Install or enable Visual Studio Tools for Unreal Engine.
3. Open projects/BiupiuAssetStudio/BiupiuAssetStudio.uproject.
4. Generate project files.
5. Build BiupiuAssetStudioEditor in Development Editor.
6. Open the editor and confirm the startup map.
7. Import a licensed test mesh through the configured asset pipeline.
8. Confirm metadata, provenance and destination.
9. Discover the asset through Unreal Asset Registry.
10. Place the asset in a level and validate geometry, material, scale and collision.
11. Run Movie Render Queue on a short test sequence.
12. Record engine version, Visual Studio version, asset ID and result in the validation record.

## Failure handling

If a workstation step fails, capture the exact compiler, editor, import or render error before changing architecture. Fix the smallest affected layer and rerun the gate.

## Completion criterion

The complete UE5 gate is PASS only when repository CI passes and the workstation sequence has been executed successfully. Repository CI alone is a source/configuration PASS, not a full UE5 runtime PASS.
