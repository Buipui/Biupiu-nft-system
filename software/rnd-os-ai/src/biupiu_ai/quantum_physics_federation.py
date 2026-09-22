"""Native federation contracts for QuTiP and OpenFermion.

External packages remain optional providers. This module deliberately keeps
the Biupiu contract dependency-free so semantic checks and tests do not require
third-party installation.
"""
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class QuantumProviderContract:
    provider_id: str
    source: str
    license: str
    capabilities: Tuple[str, ...]
    state: str = "INTEGRATED"
    runtime_required: bool = True


PROVIDERS = (
    QuantumProviderContract(
        "qutip",
        "https://github.com/qutip/qutip",
        "BSD-3-Clause",
        (
            "open-quantum-systems",
            "hamiltonian-evolution",
            "master-equation",
            "collapse-operators",
        ),
    ),
    QuantumProviderContract(
        "openfermion",
        "https://github.com/quantumlib/OpenFermion",
        "Apache-2.0",
        (
            "fermionic-operators",
            "qubit-hamiltonians",
            "quantum-algorithm-compilation",
            "electronic-structure",
        ),
    ),
)


def list_quantum_providers() -> tuple[QuantumProviderContract, ...]:
    return PROVIDERS


def quantum_provider_smoke_test() -> bool:
    ids = {provider.provider_id for provider in PROVIDERS}
    return (
        ids == {"qutip", "openfermion"}
        and all(provider.capabilities for provider in PROVIDERS)
        and all(provider.state == "INTEGRATED" for provider in PROVIDERS)
    )
