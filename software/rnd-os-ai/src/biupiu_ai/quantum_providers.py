"""Provider registry for the Biupiu quantum federation.

Adapters are capability declarations, not implicit execution permissions.
Qiskit is the IBM-oriented provider; PennyLane is the framework-neutral
hybrid/differentiable provider. Both remain simulator-first and fail-closed.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class QuantumProvider:
    provider_id: str
    package: str
    role: str
    execution_modes: Tuple[str, ...]
    capabilities: Tuple[str, ...]
    hardware_enabled: bool = False


QISKIT = QuantumProvider(
    provider_id="qiskit",
    package="qiskit-machine-learning",
    role="IBM quantum circuits, kernels and QNNs",
    execution_modes=("simulator", "hardware"),
    capabilities=("quantum-kernel", "quantum-neural-network", "benchmarking"),
)

PENNYLANE = QuantumProvider(
    provider_id="pennylane",
    package="pennylane",
    role="hybrid quantum-classical programming and differentiation",
    execution_modes=("simulator", "hardware"),
    capabilities=("hybrid-differentiation", "quantum-neural-network", "benchmarking"),
)

PROVIDERS = (PENNYLANE, QISKIT)


def provider_registry() -> Tuple[QuantumProvider, ...]:
    """Stable provider registry; hardware remains disabled by default."""
    return PROVIDERS


def provider_for_capability(capability: str) -> Tuple[QuantumProvider, ...]:
    """Return providers that advertise a capability without activating them."""
    return tuple(
        provider for provider in PROVIDERS if capability in provider.capabilities
    )
