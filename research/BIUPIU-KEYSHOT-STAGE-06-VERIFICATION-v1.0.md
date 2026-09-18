# Biupiu KeyShot Stage 6 Verification v1.0

Date: 2026-09-18

## Stage 6 — Verified source/license findings (2026-09-18)

- **keyshot-dev/configurations:** verified as a public keyshot-dev repository, but its contents are Digizuite/DAM configuration definitions rather than a KeyShot renderer integration. **Reference only; not adopted.**
- **keyshot-dev/scripts:** verified as Digizuite/DAM SQL migration and maintenance scripts. **Excluded from the KeyShot package.**
- **keyshot-dev/integration-api-examples:** verified as Digizuite SDK/API examples and not a KeyShot rendering integration. **Excluded.**
- **SimonTek27/kseditor:** verified as an Assetto Corsa/ksEditor project with a GPL-3.0 license. It is not the KeyShot renderer and will not be imported into Biupiu. **External reference only.**
- **aws-deadline/deadline-cloud-for-keyshot:** verified as a directly relevant KeyShot submitter/plugin project for AWS Deadline Cloud, with KeyShot bridge/submitter components. **Accepted as a future external distributed-rendering integration candidate; do not copy wholesale.**
- **jasonengcc/KeyShot-Studio-Materials:** repository provenance/licensing is insufficiently established for redistribution. **No assets will be bundled.**

### Stage 6 decision
The Biupiu KeyShot package remains metadata/adapter architecture only. No proprietary KeyShot software, license files, activation material, or third-party material libraries are copied into the repository.

### Next gate
Define a Biupiu render-job contract and an optional AWS Deadline adapter for distributed rendering.