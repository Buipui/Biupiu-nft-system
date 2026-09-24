from biupiu_ai.quantum_providers import (
    BRAKET,
    AZURE_QUANTUM,
    DWAVE_LEAP,
    OPENQASM,
    PENNYLANE,
    QIR,
    QISKIT,
    TKET,
    hardware_capable_providers,
    provider_for_capability,
    provider_registry,
)


def test_provider_registry_is_stable():
    assert provider_registry() == (
        PENNYLANE,
        QISKIT,
        QIR,
        OPENQASM,
        BRAKET,
        AZURE_QUANTUM,
        DWAVE_LEAP,
        TKET,
    )
    assert all(not provider.hardware_enabled for provider in provider_registry())


def test_provider_capability_boundaries():
    assert "quantum-kernel" in QISKIT.capabilities
    assert "quantum-neural-network" in QISKIT.capabilities
    assert "hybrid-differentiation" in PENNYLANE.capabilities
    assert "quantum-ir" in QIR.capabilities
    assert "quantum-ir" in OPENQASM.capabilities
    assert "qpu" in BRAKET.capabilities
    assert "qpu" in AZURE_QUANTUM.capabilities
    assert "annealing" in DWAVE_LEAP.capabilities
    assert "quantum-compiler" in TKET.capabilities


def test_capability_routing_does_not_activate_hardware():
    providers = provider_for_capability("quantum-neural-network")
    assert {p.provider_id for p in providers} == {"pennylane", "qiskit"}
    assert all(not p.hardware_enabled for p in providers)


def test_quantum_ai_governance_is_fail_closed():
    assert all(p.execution_policy == "SIMULATOR_VALIDATE" for p in provider_registry())
    assert all(p.learning_mode == "PASSIVE_OBSERVATION" for p in provider_registry())
    assert all(p.promotion_state == "REFERENCE_ONLY" for p in provider_registry())
    assert all(p.authority_owner == "BIUPIU_FEDERATION_QUANTUM" for p in provider_registry())


def test_hardware_capability_does_not_equal_hardware_execution():
    declared = hardware_capable_providers()
    assert {p.provider_id for p in declared} == {
        "qiskit",
        "pennylane",
        "openqasm",
        "aws-braket",
        "azure-quantum",
        "dwave-leap",
        "pytket",
    }
    assert all(not p.hardware_enabled for p in declared)
