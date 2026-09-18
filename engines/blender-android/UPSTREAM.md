# Blender Android Engine Integration

Biupiu R&D OS integration record for the unofficial Android Blender fork.

## Pinned upstream
- Repository: https://github.com/Wanderson-Magalhaes/blender_for_android
- Reviewed commit: 76dc70df95ae32dcd15f3f86abfd82f4c5691140
- Purpose: Android ARM64/Vulkan Blender engine for Biupiu 3D modelling, rendering, simulation and Digital Twin visualization.

## Relevant upstream areas
- `build_files/android/` — Android build, feature profiles, packaging and dependency orchestration.
- `build_files/android/build.py` — reproducible Android build entry point.
- `build_files/android/deps/` — Android dependency cross-compilation.
- `build_files/android/apk/` — APK packaging and Java activity.
- `intern/ghost/intern/GHOST_SystemAndroid.cc` — Android platform/window/input integration.
- `source/blender/windowmanager/intern/wm_virtual_keyboard.cc` — touch/virtual keyboard support.
- `scripts/startup/` — Python-side Blender startup/add-on integration.

## Feature profiles
- Full: target high-end ARM64 Vulkan devices; retains Cycles and heavier dependencies.
- Lite: target weaker devices; reduced heavy dependencies.
- Remote: Biupiu shell controls a workstation/cloud Blender instance for workloads exceeding mobile limits.

## License/compliance
Blender and this fork are GPL-licensed. Keep upstream source separately attributable and preserve required license/source notices when distributing a derivative Blender build. Do not copy arbitrary upstream source into proprietary Biupiu modules.

## Sync policy
Pin a known-good upstream commit. Update only through an explicit engine-sync gate with build/test verification. Do not silently track upstream main.
