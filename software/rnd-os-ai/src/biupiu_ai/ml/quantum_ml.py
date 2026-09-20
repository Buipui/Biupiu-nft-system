"""Optional quantum-machine-learning boundary with a classical-safe fallback.

The fallback evaluates the exact fidelity kernel of a separable single-qubit
angle-encoding feature map:
K(x,y) = product_i cos^2((x_i-y_i)/2).

This gives Biupiu a deterministic kernel experiment without pretending that a
classical emulation is a quantum-advantage result. Qiskit/PennyLane backends are
optional adapters and must pass separate environment and reproducibility gates.
"""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
import math
from typing import Sequence, Tuple


@dataclass(frozen=True)
class QuantumBackendStatus:
    backend: str
    available: bool
    mode: str
    reason: str


def probe_quantum_backends() -> Tuple[QuantumBackendStatus, ...]:
    candidates = (
        ("QISKIT_ML", "qiskit_machine_learning"),
        ("PENNYLANE", "pennylane"),
        ("CUDA_Q", "cudaq"),
    )
    out = []
    for backend, package in candidates:
        try:
            available = importlib.util.find_spec(package) is not None
        except (ImportError, ModuleNotFoundError, ValueError):
            available = False
        out.append(
            QuantumBackendStatus(
                backend,
                available,
                "native-adapter" if available else "classical-fallback",
                "optional dependency",
            )
        )
    return tuple(out)


def fidelity_quantum_kernel(x: Sequence[float], y: Sequence[float]) -> float:
    """Evaluate a separable angle-encoding quantum fidelity kernel."""
    if len(x) != len(y) or not x:
        raise ValueError("feature vectors must have equal non-zero length")
    value = 1.0
    for a, b in zip(x, y):
        value *= math.cos((float(a) - float(b)) / 2.0) ** 2
    return value


def quantum_kernel_matrix(samples: Sequence[Sequence[float]]) -> Tuple[Tuple[float, ...], ...]:
    if not samples:
        raise ValueError("samples are required")
    return tuple(
        tuple(fidelity_quantum_kernel(a, b) for b in samples)
        for a in samples
    )


def kernel_nearest_label(
    train_x: Sequence[Sequence[float]],
    train_y: Sequence[str],
    query: Sequence[float],
) -> str:
    """Simple interpretable Q-kernel baseline for proof-of-concept experiments."""
    if len(train_x) != len(train_y) or not train_x:
        raise ValueError("training samples and labels must be non-empty and aligned")
    scores = [
        (fidelity_quantum_kernel(x, query), label)
        for x, label in zip(train_x, train_y)
    ]
    return max(scores, key=lambda item: item[0])[1]
