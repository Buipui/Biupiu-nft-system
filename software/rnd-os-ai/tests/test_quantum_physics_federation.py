from biupiu_ai.quantum_physics_federation import (
    quantum_provider_smoke_test,
    list_quantum_providers,
)


def test_quantum_provider_registry_smoke():
    assert quantum_provider_smoke_test()


def test_quantum_provider_contracts_have_provenance():
    providers = list_quantum_providers()
    assert {p.provider_id for p in providers} == {"qutip", "openfermion"}
    assert all(p.source.startswith("https://") for p in providers)
    assert all(p.license for p in providers)
