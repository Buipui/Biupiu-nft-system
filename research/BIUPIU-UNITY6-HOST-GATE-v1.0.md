# BIUPIU UNITY 6 HOST GATE v1.0

Status: PREPARED FOR DESKTOP EXECUTION

This gate is the bridge between repository integration and actual runtime verification.

## Required evidence
- Unity Editor/version detected
- Visual Studio / VS Code Insider detected
- .NET/C# tooling detected
- Unity ProjectVersion.txt
- Packages/manifest.json
- packages-lock.json when present
- Unity compile/build log
- scene/HMI smoke-test result
- Exterminate result
- repository round-trip result

## Execution
Run `tools/unity6/biupiu-unity-host-gate.ps1` from the isolated Unity adapter project.

The script is intentionally read-first. It does not modify production Biupiu projects. Build mode is explicit.

## Promotion states
DISCOVERED -> RESOLVED -> COMPILED -> SMOKE-TESTED -> EXTERMINATE-PASS -> VERIFIED

No state may be skipped from desktop evidence.

## Current repository state
Adapter contract: IMPLEMENTED
Search/registry: EXECUTED
Architecture Exterminate: PASS
Host runtime: PENDING DESKTOP EXECUTION
