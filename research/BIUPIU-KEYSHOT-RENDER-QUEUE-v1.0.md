# Biupiu KeyShot Render Queue v1.0

## Architecture
R&D OS Render Queue -> Job Contract -> Adapter -> Licensed KeyShot -> Output Registry

### Adapter targets
- Local Windows KeyShot adapter: first implementation target.
- AWS Deadline Cloud for KeyShot: optional future distributed adapter.

### Job lifecycle
1. Validate asset and provenance.
2. Validate render profile.
3. Create job manifest.
4. Dispatch to selected adapter.
5. Track queued/running/completed/failed state.
6. Register output and provenance.
7. Link output to Showcase, Digital Twin and Showreel records.

### Distributed rendering boundary
AWS Deadline Cloud integration remains optional. The repository stores only the interface contract and metadata; proprietary KeyShot installation and cloud credentials remain external.

### Initial acceptance tests
- Reject unsupported source/output formats.
- Reject missing asset/profile identifiers.
- Require provenance metadata for external assets.
- Support deterministic job IDs.
- Preserve source asset ID through output registration.
