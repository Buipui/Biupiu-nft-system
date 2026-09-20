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


## EXECUTION ATTEMPT — 20 September 2026

The host gate is prepared and committed, but this connected execution environment does not expose the user's Windows desktop, local Unity Editor, Visual Studio installation, VS Code Insider installation, or PowerShell session. Therefore no local runtime evidence can be generated here.

**SAFE RESULT:** HOST EXECUTION BLOCKED BY ENVIRONMENT BOUNDARY — NOT A FAILURE OF THE UNITY ADAPTER.

No false VERIFIED state is assigned. Repository-level Exterminate remains PASS. The next desktop evidence command is:

`powershell -ExecutionPolicy Bypass -File .\\tools\\unity6\\biupiu-unity-host-gate.ps1 -ProjectPath <isolated-unity-project>`

Use `-Build` only after the read-first inspection is reviewed.

Promotion remains **DISCOVERED/READY → RESOLVED → COMPILED → SMOKE-TESTED → EXTERMINATE-PASS → VERIFIED**.


## DESKTOP-HANDOFF NEXT GATE — READY

The repository-side gate is complete. The only remaining execution dependency is the user's local Windows host. The committed PowerShell harness must be run there because GitHub cannot access local Unity/VS/VS Code installations.

Evidence required for promotion:
1. Unity version and executable path.
2. VS / VS Code Insider and C# tooling versions.
3. ProjectVersion.txt and package manifests.
4. Compile/build exit code and log.
5. Scene/HMI smoke-test result.
6. Exterminate/conflict scan result.
7. Repository round-trip evidence.

Until these are returned, runtime status remains NOT VERIFIED.
