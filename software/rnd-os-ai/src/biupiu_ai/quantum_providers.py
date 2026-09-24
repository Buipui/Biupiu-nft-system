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
    authority_owner: str = "BIUPIU_FEDERATION_QUANTUM"
    execution_policy: str = "SIMULATOR_VALIDATE"
    learning_mode: str = "PASSIVE_OBSERVATION"
    promotion_state: str = "REFERENCE_ONLY"


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

QIR = QuantumProvider(
    provider_id="qir",
    package="QIR",
    role="LLVM-based quantum intermediate representation / compiler boundary",
    execution_modes=("simulator", "compiler"),
    capabilities=("quantum-ir", "compiler-interoperability", "llvm"),
)

OPENQASM = QuantumProvider(
    provider_id="openqasm",
    package="openqasm",
    role="hardware-independent quantum assembly / circuit IR",
    execution_modes=("simulator", "compiler", "hardware"),
    capabilities=("quantum-ir", "circuit-description", "qpu-portability"),
)

BRAKET = QuantumProvider(
    provider_id="aws-braket",
    package="amazon-braket-sdk",
    role="managed simulator and multi-provider QPU execution adapter",
    execution_modes=("simulator", "hardware"),
    capabilities=("qpu", "circuit-execution", "device-capabilities"),
)

AZURE_QUANTUM = QuantumProvider(
    provider_id="azure-quantum",
    package="azure-quantum",
    role="cloud quantum execution and QIR target boundary",
    execution_modes=("simulator", "hardware"),
    capabilities=("qpu", "qir", "provider-routing"),
)

DWAVE_LEAP = QuantumProvider(
    provider_id="dwave-leap",
    package="dwave-system",
    role="D-Wave Leap / Ocean hybrid quantum-classical adapter",
    execution_modes=("simulator", "hardware"),
    capabilities=("annealing", "hybrid-optimization", "qpu"),
)

TKET = QuantumProvider(
    provider_id="pytket",
    package="pytket",
    role="Quantinuum quantum circuit compilation and backend abstraction",
    execution_modes=("simulator", "compiler", "hardware"),
    capabilities=("quantum-compiler", "circuit-optimization", "qpu-portability"),
)

PROVIDERS = (PENNYLANE, QISKIT, QIR, OPENQASM, BRAKET, AZURE_QUANTUM, DWAVE_LEAP, TKET)


def provider_registry() -> Tuple[QuantumProvider, ...]:
    """Stable provider registry; hardware remains disabled by default."""
    return PROVIDERS


def hardware_capable_providers() -> Tuple[QuantumProvider, ...]:
    """Return hardware-capable declarations without granting execution authority."""
    return tuple(provider for provider in PROVIDERS if "hardware" in provider.execution_modes)


def provider_for_capability(capability: str) -> Tuple[QuantumProvider, ...]:
    """Return providers that advertise a capability without activating them."""
    return tuple(
        provider for provider in PROVIDERS if capability in provider.capabilities
    )
