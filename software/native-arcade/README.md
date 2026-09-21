# Biupiu Native Arcade & Modding Station v0.1

## Status

**REGISTERED — IMPLEMENTATION PROTOTYPE ADDED — VERIFICATION PENDING**

This module is a native, rights-aware orchestration layer for future Biupiu World arcades and creator stations. It does not bundle third-party ROMs, copyrighted game data, or arbitrary executable mods.

## Components

- `types.ts` — platform-neutral contracts
- `registry.ts` — in-memory resource registry with fail-closed rights checks
- `MODDING-STATION.md` — Unreal/Unity/Biupiu creator workflow

## Design rule

The runtime may register and inspect a resource while refusing distribution or launch when rights, compatibility, security, or approval requirements are incomplete.

## Planned adapters

- Unreal Engine
- Unity
- DOSBox / ScummVM / MAME-compatible research adapters, subject to licence review
- Biupiu-native runtime

## Verification still required

- unit tests
- sandboxed execution design
- signed manifests
- dependency scanning
- platform-specific launch adapters
- legal review of each external title/resource
- Unreal and Unity integration tests
