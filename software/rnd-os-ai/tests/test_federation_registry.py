from biupiu_ai.federation_registry import (
    AgentSystem,
    FederationPolicy,
    capability_names,
    eligible_for_activation,
)


def test_unverified_adapter_is_not_eligible():
    system = AgentSystem("candidate", "test", ("x",), "adapter")
    assert not eligible_for_activation(
        system,
        FederationPolicy(),
        security=True,
    )


def test_all_gates_are_required():
    system = AgentSystem("candidate", "test", ("x",), "adapter")
    assert eligible_for_activation(
        system,
        FederationPolicy(),
        provenance=True,
        license=True,
        security=True,
        regression=True,
        human_approved=True,
    )


def test_blocked_system_is_never_eligible():
    system = AgentSystem("blocked", "test", ("x",), "adapter", status="BLOCKED")
    assert not eligible_for_activation(
        system,
        FederationPolicy(
            require_provenance=False,
            require_license=False,
            require_security=False,
            require_regression=False,
            require_human_promotion=False,
        ),
    )


def test_capabilities_are_deterministic():
    capabilities = capability_names()
    assert capabilities == tuple(sorted(capabilities))
    assert "retrieval" in capabilities
    assert "quantum-kernels" in capabilities
