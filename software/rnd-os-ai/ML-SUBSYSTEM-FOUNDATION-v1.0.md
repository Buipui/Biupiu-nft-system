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
