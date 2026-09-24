# ML Subsystem Foundation v1.0

The machine-learning subsystem is an optional capability layer under Biupiu Intelligence.

Components:
- biupiu_ai/ml/backends.py
- biupiu_ai/ml/engine.py
- biupiu_ai/ml/metrics.py
- biupiu_ai/ml/multilingual.py
- tests/test_ml_subsystem.py

Design:
- dependency-light core
- optional external ML backends
- evidence required before routing
- licence/provenance metadata
- multilingual query expansion
- deterministic baseline metrics
- drift screening
- learning-record integration
- Core OS remains authoritative

External code is not automatically installed or copied.


## Self-diagnostics / self-healing extension — 2026-09-24

Added `biupiu_ai/ml/self_diagnostics.py` as a bounded diagnostic and repair coordinator.

Diagnostic coverage:
- learning-record provenance/hash integrity
- continual-adaptation parameter bounds
- quantum-ML classical-safe baseline invariants
- optional ML backend registry/availability
- fail-closed repair proposal generation

Self-healing contract:
DETECT → CLASSIFY → QUARANTINE → PROPOSE REVERSIBLE REPAIR → VALIDATE → REGRESSION → HUMAN/CORE APPROVAL → APPLY.

The repair coordinator never silently rewrites authoritative code or model policy, never promotes an unverified repair, and never performs physical actuation.

State:
SOURCE IMPLEMENTED
TESTS ADDED
CI WORKFLOW UPDATED
FRESH CI RESULT: PENDING
HOST/DEVICE RUNTIME: OPEN
