# Biupiu Downstream Asset Registry v1.0

Gate 11 establishes the canonical registration boundary between an explicitly approved handoff package and downstream Biupiu World assets.

## Registration rule

An asset may enter REGISTERED only when the originating handoff contains:
- approval.decision = APPROVE
- visual = PASS
- provenance = PASS
- evidence = PASS
- asset_rights = PASS
- an actual source asset exists and can be hashed.

Anything else remains PENDING or BLOCKED. No script infers approval.

## Integrity and audit

Each asset receives a stable BPU-WORLD-* ID and records its Digital Twin, handoff, provenance, claim/evidence state, downstream targets and SHA-256 integrity hashes.

The registry is append-only; duplicate asset IDs are rejected rather than overwritten.

## Downstream targets
- BIUPIU_WORLD
- SHOWREEL
- DIGITAL_TWIN_CATALOG
