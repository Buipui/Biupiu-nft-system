"""Optional ML backend registry for Biupiu Intelligence.

No third-party package is required to import this module. Backend availability
is probed without importing/executing the package. This keeps the Core OS and
the deterministic Intelligence foundation portable and fail-closed.
"""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from typing import Tuple


@dataclass(frozen=True)
class BackendSpec:
    backend_id: str
    package: str
    import_name: str
    license: str
    capabilities: Tuple[str, ...]
    integration_mode: str
    source: str


BACKENDS = (
    BackendSpec(
        "SKLEARN", "scikit-learn", "sklearn", "BSD-3-Clause",
        ("classical", "classification", "regression", "clustering", "preprocessing", "evaluation"),
        "optional-adapter", "https://github.com/scikit-learn/scikit-learn",
    ),
    BackendSpec(
        "XGBOOST", "xgboost", "xgboost", "Apache-2.0",
        ("tabular", "classification", "regression", "ranking"),
        "optional-adapter", "https://github.com/dmlc/xgboost",
    ),
    BackendSpec(
        "LIGHTGBM", "lightgbm", "lightgbm", "MIT",
        ("tabular", "classification", "regression", "ranking", "distributed"),
        "optional-adapter", "https://github.com/lightgbm-org/LightGBM",
    ),
    BackendSpec(
        "RIVER", "river", "river", "BSD-3-Clause",
        ("online", "streaming", "incremental", "concept-drift"),
        "optional-adapter", "https://github.com/online-ml/river",
    ),
    BackendSpec(
        "PYTORCH", "torch", "torch", "BSD-3-Clause-plus-third-party-notices",
        ("deep-learning", "vision", "sequence", "representation-learning", "scientific-ml"),
        "optional-adapter", "https://github.com/pytorch/pytorch",
    ),
    BackendSpec(
        "TORCHRL", "torchrl", "torchrl", "MIT",
        ("reinforcement-learning", "simulation", "control"),
        "optional-adapter", "https://github.com/pytorch/rl",
    ),
    BackendSpec(
        "TRANSFORMERS", "transformers", "transformers", "Apache-2.0",
        ("nlp", "multilingual", "language-models", "representation-learning"),
        "optional-adapter", "https://github.com/huggingface/transformers",
    ),
    BackendSpec(
        "FAISS", "faiss-cpu/faiss-gpu", "faiss", "MIT",
        ("vector-search", "nearest-neighbour", "retrieval"),
        "optional-adapter", "https://github.com/facebookresearch/faiss",
    ),
    BackendSpec(
        "NETWORKX", "networkx", "networkx", "BSD-3-Clause",
        ("graphs", "knowledge-graph", "dependency-analysis"),
        "optional-adapter", "https://github.com/networkx/networkx",
    ),
    BackendSpec(
        "OPTUNA", "optuna", "optuna", "MIT",
        ("hyperparameter-optimization", "search", "study-management"),
        "optional-adapter", "https://github.com/optuna/optuna",
    ),
    BackendSpec(
        "ONNX", "onnx", "onnx", "Apache-2.0",
        ("model-interchange", "portable-inference"),
        "optional-adapter", "https://github.com/onnx/onnx",
    ),
    BackendSpec(
        "ONNXRUNTIME", "onnxruntime", "onnxruntime", "MIT",
        ("portable-inference", "edge-inference"),
        "optional-adapter", "https://github.com/microsoft/onnxruntime",
    ),
    BackendSpec(
        "MLFLOW", "mlflow", "mlflow", "Apache-2.0",
        ("experiment-tracking", "model-registry", "evaluation-lineage"),
        "optional-adapter", "https://github.com/mlflow/mlflow",
    ),
    BackendSpec(
        "OPACUS", "opacus", "opacus", "Apache-2.0",
        ("differential-privacy", "private-training"),
        "optional-adapter", "https://github.com/meta-pytorch/opacus",
    ),
    BackendSpec(
        "PYSYFT", "syft", "syft", "Apache-2.0",
        ("federated-learning", "privacy-research", "remote-data-science", "datasite-access"),
        "research-adapter", "https://github.com/OpenMined/PySyft",
    ),
    BackendSpec(
        "FLOWER", "flwr", "flwr", "Apache-2.0",
        ("federated-learning", "federated-analytics", "secure-aggregation", "simulation"),
        "research-adapter", "https://github.com/flwrlabs/flower",
    ),
    BackendSpec(
        "GYMNASIUM", "gymnasium", "gymnasium", "MIT",
        ("reinforcement-learning", "environment-interface", "simulation"),
        "optional-adapter", "https://github.com/Farama-Foundation/Gymnasium",
    ),
)


def get_backend(backend_id: str) -> BackendSpec | None:
    wanted = backend_id.strip().upper()
    return next((b for b in BACKENDS if b.backend_id == wanted), None)


def probe_backend(backend_id: str) -> bool:
    backend = get_backend(backend_id)
    if backend is None:
        raise ValueError(f"unknown ML backend: {backend_id}")
    try:
        return importlib.util.find_spec(backend.import_name) is not None
    except (ImportError, ModuleNotFoundError, ValueError):
        return False
