# Biupiu Unreal Engine 5 Asset Studio

This module makes Unreal Engine 5 the interactive 3D asset, scene, digital-twin and real-time visualization layer of the Biupiu R&D rendering stack.

It works alongside Blender, Cinema 4D, KeyShot, Twinmotion and Redshift rather than replacing them.

## Capabilities

- Reusable UE5 3D assets
- C++ and Blueprint-enabled asset systems
- Mesh, material, texture and animation import
- Interactive scenes and digital twins
- Automotive, marine, eVTOL, helicopter and microturbine visualization
- Advanced-material and computational-art presentation
- Showreel and real-time visualization workflows

## Visual Studio

Use Visual Studio 2022 with Game development with C++ and Visual Studio Tools for Unreal Engine. Microsoft documents UE5 support, UE logging, Blueprint references, UE macros, class/module/plugin creation, debugging and Unreal test discovery.

The Microsoft Unreal Engine plugin is intentionally not vendored here. Install it on the workstation or through Visual Studio integration tooling.

## Asset pipeline

Research/R&D source -> computational model -> Blender/Cinema 4D -> FBX or glTF/USD where appropriate -> Unreal Engine 5 -> materials/lighting/Blueprints/C++ -> validation -> real-time render/showreel/digital twin.

## Setup

1. Install Unreal Engine 5.x through Epic Games Launcher or a source build.
2. Install Visual Studio 2022 with Game development with C++.
3. Enable Visual Studio Tools for Unreal Engine, Unreal Engine debugger tools, Unreal Engine Test Adapter and HLSL Tools when required.
4. Open projects/BiupiuAssetStudio/BiupiuAssetStudio.uproject.
5. Generate project files if prompted and open the solution in Visual Studio.
6. Use Project > Configure Tools for Unreal Engine and run status checks.
7. Build BiupiuAssetStudioEditor in Development Editor configuration.

## Verification gate

A workstation is ready when Unreal opens without module errors, Visual Studio discovers the C++ module, a Development Editor build succeeds, a test mesh imports, the mesh can be placed in a level, and a Movie Render Queue or packaged visualization test completes without missing dependencies.

See UNREAL5-ASSET-PIPELINE-v1.0.md and VISUAL-STUDIO-UE5-INTEGRATION.md for the controlled integration gates.
