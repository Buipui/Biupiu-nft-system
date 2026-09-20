# XENG-02 Runtime Probe Protocol v1.0

## Purpose

Turn engine registrations into measured host evidence without pretending repository architecture is workstation verification.

## Probe order

1. Detect installed application/version.
2. Detect relevant plugins/modules.
3. Record project/path identity without copying secrets.
4. Check supported interchange capabilities.
5. Check XR capability.
6. Run controlled asset import/export where the host permits it.
7. Capture geometry/material/transform hashes.
8. Return provenance and failures to Biupiu OS/DMS.

## Controlled round-trip

Source asset -> canonical manifest -> UE5 -> Unity -> Lumion -> canonical comparison.

The test asset must be deliberately simple: one mesh, one material set, one transform, one metadata payload and one Digital Twin identifier.

## Promotion

- REGISTERED: indexed only.
- INTEGRATED: adapter/contract exists.
- CONNECTED: host handshake succeeded.
- VERIFIED: controlled runtime test passed with evidence.
- BLOCKED: a required check failed.
- DEPRECATED: provider superseded.

## Safety

The probe may inspect installed software and project metadata but must not modify projects, execute arbitrary downloaded binaries, bypass licences, or expose credentials.

## Current limitation

This repository tool can establish source-level probes and protocol. Actual workstation discovery and runtime verification require the connected desktop environment.
