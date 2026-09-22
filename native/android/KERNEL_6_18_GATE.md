# Android 17 6.18 GKI Gate

Locked release: android17-6.18-2026-09_r3
Release date: 2026-09-17
Upstream SHA prefix: ee03b8f987e082acff09

## Rules

- Treat GKI as the kernel baseline.
- Preserve Android kernel ABI requirements.
- Prefer existing LSM/SELinux, lockdown, module-signing and integrity facilities.
- No custom kernel module until the user-visible/native requirement is demonstrated and the module passes build, ABI, security and runtime review.
- Kernel modifications remain a separate gate from user-space Buipui modules.
