from biupiu_ai.quantum_providers import (
    PENNYLANE,
    QISKIT,
    provider_for_capability,
    provider_registry,
)


def test_provider_registry_is_stable():
    assert provider_registry() == (PENNYLANE, QISKIT)
    assert all(not provider.hardware_enabled for provider in provider_registry())


def test_qiskit_capabilities():
    assert "quantum-kernel" in QISKIT.capabilities
    assert "quantum-neural-network" in QISKIT.capabilities


def test_pennylane_hybrid_capability():
    assert "hybrid-differentiation" in PENNYLANE.capabilities


def test_capability_routing_does_not_activate_hardware():
    providers = provider_for_capability("quantum-neural-network")
    assert {p.provider_id for p in providers} == {"pennylane", "qiskit"}
    assert all(not p.hardware_enabled for p in providers)
