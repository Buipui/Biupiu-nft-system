# Biupiu Windows Development Tree v1.0

Purpose: provide a reproducible Windows development entry point for the Biupiu repository without claiming that local hardware, Unreal Engine, GPU, Android or physical-device gates are verified.

## Authority

- Repository source: Git
- Build state: generated evidence under `build/evidence/` (local-only by default)
- Runtime state: local execution evidence
- Governance: `research/LOCAL-EXECUTION-GATES-v1.0.md`
- Native system identity: `research/BIUPIU-NATIVE-SYSTEM-CATALOGUE-v1.0.json`

## Primary command

From PowerShell:

`pwsh -File .\windows\Invoke-BiupiuBuild.ps1`

The script:
1. inventories the host;
2. checks required tools;
3. runs repository semantic audit;
4. installs/validates Node dependencies;
5. compiles Solidity contracts;
6. runs contract tests;
7. builds TypeScript workspaces when a root tsconfig exists;
8. detects Unreal Engine source trees without assuming their presence;
9. writes machine-readable evidence.

A failed optional/local gate is recorded rather than converted into a false PASS.
