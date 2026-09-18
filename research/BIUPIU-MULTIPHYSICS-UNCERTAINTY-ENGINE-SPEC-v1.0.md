# Biupiu Multi-Physics Candidate Evaluation & Uncertainty Engine v1.0

Gate: BM-09
Status: EXECUTED / architecture stage

CANDIDATE -> INPUT VALIDATION -> AERO LOADS -> STRUCTURAL -> MODAL/BUCKLING -> FATIGUE PROXY -> THERMAL/MOISTURE -> MANUFACTURING VARIABILITY -> UNCERTAINTY PROPAGATION -> RESULT RECORD -> PARETO/TEST QUEUE

BM-09 evaluates candidates across coupled physics while preserving provenance and uncertainty.

Rules:
- Every module records model version, assumptions, solver/version, discretisation version, boundary conditions and input provenance.
- Missing upstream inputs cannot be silently substituted.
- Unknown data remain unknown and block claims requiring them.
- Estimated, literature-derived, measured and model-derived values remain distinct.
- Sensitivity and uncertainty are retained with their methods.
- Failed numerical runs remain auditable.

Modules: aerodynamic loading; structural response; modal/buckling; fatigue proxy; thermal sensitivity; moisture sensitivity; manufacturing variability.

Uncertainty classes: measurement, batch/material, manufacturing, environmental, model-form, numerical/discretisation and parameter uncertainty.

Outputs: RUN_ID, CANDIDATE_ID, module versions, input snapshot, provenance, deterministic results, uncertainty results, sensitivity results, blocked/failed modules, evidence state and Digital Twin version.

Evidence boundary: R&D workflow only; no certification or production allowables.

Next: BM-10 — Automated Pareto Frontier & Test-Selection Engine.
