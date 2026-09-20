from biupiu_ai.federation_registry import AgentSystem, FederationPolicy, eligible_for_activation, capability_names

def test_unverified_adapter_is_not_eligible():
    s = AgentSystem("candidate", "test", ("x",), "adapter")
    assert not eligible_for_activation(s, FederationPolicy(), security=True)

def test_all_gates_are_required():
    s = AgentSystem("candidate", "test", ("x",), "adapter")
    assert eligible_for_activation(s, FederationPolicy(), provenance=True, license=True, security=True, regression=True, human_approved=True)

def test_capabilities_are_deterministic():
    assert "retrieval" in capability_names()
