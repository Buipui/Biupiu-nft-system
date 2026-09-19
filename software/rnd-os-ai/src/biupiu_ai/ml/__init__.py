"""Biupiu Intelligence machine-learning subsystem.

The core package is dependency-light. Third-party ML frameworks are optional
adapters selected at runtime after provenance, licence, compatibility and
resource checks.
"""

from .backends import BACKENDS, BackendSpec, probe_backend
from .engine import MLRequest, MLRoute, route_ml_request
from .metrics import (
    accuracy,
    brier_score,
    mae,
    mse,
    precision_at_k,
    recall_at_k,
)
from .multilingual import SearchProfile, build_search_profile

__all__ = [
    "BACKENDS", "BackendSpec", "MLRequest", "MLRoute", "SearchProfile",
    "accuracy", "brier_score", "mae", "mse", "precision_at_k", "recall_at_k",
    "probe_backend", "route_ml_request", "build_search_profile",
]
