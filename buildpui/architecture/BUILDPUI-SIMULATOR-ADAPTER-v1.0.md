# BuildPui simulator adapter v1.0

Status: **IMPLEMENTED — AUTOMATED EXECUTION OPEN**

This adapter is the boundary between the canonical BuildPui architecture/digital-twin object envelope and the existing Python architecture simulator prototype.

## Contract

1. Validate every object against `BUILDPUI-ARCHITECTURE-SCHEMA-v1.0.schema.json`.
2. Reject malformed objects before simulation preparation.
3. Permit simulation preparation only when `evidence_state=SIMULATION-READY`.
4. Never infer engineering validation from schema validity.
5. Preserve provenance, licence, uncertainty and open-question fields unchanged.

## Scope boundary

This is a data-contract adapter, not a structural solver or regulatory approval system. Physical testing, code compliance, fire performance, durability and other engineering validation remain separate gates.

## Next gate

Run the adapter contract test in CI and then connect validated objects to the simulator's `SiteState`, `Asset` and massing pipeline.
