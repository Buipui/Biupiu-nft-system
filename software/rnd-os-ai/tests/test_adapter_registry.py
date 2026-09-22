from biupiu_ai.adapter_registry import (
    USABLE_ADAPTERS, adapter_ids, adapters_for_family, promotion_safe,
)


def test_registry_is_deterministic_and_nonempty():
    assert USABLE_ADAPTERS
    assert adapter_ids() == tuple(sorted(adapter_ids()))
    assert "ros2-dds" in adapter_ids()
    assert "eclipse-ditto" in adapter_ids()


def test_family_routing():
    assert any(a.adapter_id == "flower" for a in adapters_for_family("federated-ml"))
    assert any(a.adapter_id == "fmi-fmu" for a in adapters_for_family("simulation"))


def test_external_adapter_never_promotes_without_all_evidence():
    adapter = next(a for a in USABLE_ADAPTERS if a.adapter_id == "flower")
    assert not promotion_safe(adapter, provenance=True, licence=True, security=True,
                               build=True, regression=True, runtime=False,
                               human_approved=True)
    assert promotion_safe(adapter, provenance=True, licence=True, security=True,
                          build=True, regression=True, runtime=True,
                          human_approved=True)
