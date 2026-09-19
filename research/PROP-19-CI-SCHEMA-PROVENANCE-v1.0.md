# PROP-19 — CI, Schema Cross-Validation & Evidence Provenance v1.0

## Executed
Added repository automation for the PROP-17/18 evidence-governance layer.

### Controls
- GitHub Actions workflow executes evidence regression tests.
- PROP-15 dataset is checked against the microturbine test-data schema.
- Validation and certification states require explicit measured-evidence completeness and review.
- A dedicated provenance dataset is reserved for future traceable measured records.

### Current state
PROP-15 contains no measurements, so the system continues to report no physical validation. PROP-19 does not fabricate measurements, signatures, or certification.

### Provenance rule
Future records should preserve test ID, source/instrument identity, measurement timestamp, raw-data reference/hash, processing version, uncertainty, reviewer identity/status, and evidence status. Cryptographic signing can be added when the actual measured-data ingestion workflow is established.

### Scope
This is repository CI/data-governance infrastructure only. It does not constitute hardware, flight, marine, road, or production certification.

## Next gate
PROP-20: establish a controlled measured-data ingestion format and provenance manifest, then exercise the CI path with synthetic test fixtures clearly labelled as synthetic.
