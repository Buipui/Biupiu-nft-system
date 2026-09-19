# Visual Studio + Unreal Engine 5 Integration

## Supported baseline

Microsoft documents Visual Studio 2022 17.7+ with Unreal Engine 5.0+ for Visual Studio Tools for Unreal Engine.

## Workstation components

- Game development with C++ workload
- Visual Studio Tools for Unreal Engine
- Visual Studio debugger tools for Unreal Engine Blueprints
- Unreal Engine Test Adapter
- Windows SDK
- HLSL Tools when shader development requires them

## Microsoft plugin

Official source: microsoft/vc-ue-extensions.

Project-level installation is the preferred first Biupiu configuration because it keeps the asset studio portable and isolated. Engine-level installation can be evaluated after compatibility validation across Biupiu projects.

## Configuration gate

Open the UE project in Visual Studio, select Project > Configure Tools for Unreal Engine, refresh the integration status and verify Unreal Build Tool, targets, Blueprint support, Visual Studio Integration Tool and Test Adapter status as applicable.

## Build gate

Build the BiupiuAssetStudioEditor target from Visual Studio Developer PowerShell. Microsoft also documents building the integration plugin with MSBuild against an installed or source UE engine.

This repository does not redistribute Visual Studio or Microsoft's plugin binaries.
