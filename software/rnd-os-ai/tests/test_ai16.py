from biupiu_ai.gateway_policy import (
    GatewayPolicy,
    provider_cost_allowed,
    staging_provider_allowed,
    validate_request,
)


def test_ai16_request_limits():
    policy = GatewayPolicy(max_input_chars=10, max_evidence_sources=1, max_dataset_versions=1)
    assert validate_request("short", ["S1"], ["D1"], policy).accepted
    assert validate_request("", [], [], policy).reason == "empty-task"
    assert validate_request("01234567890", [], [], policy).reason == "task-too-large"
    assert validate_request("x", ["S1", "S2"], [], policy).reason == "too-many-evidence-sources"


def test_ai16_cost_limit():
    policy = GatewayPolicy(max_cost_units=2)
    assert provider_cost_allowed(2, policy)
    assert not provider_cost_allowed(3, policy)


def test_ai16_staging_requires_all_security_controls():
    kwargs = dict(
        authenticated=True,
        transport_secure=True,
        privacy_reviewed=True,
        rate_limit_configured=True,
        cost_limit_configured=True,
        provider_enabled=True,
    )
    assert staging_provider_allowed(**kwargs)
    kwargs["privacy_reviewed"] = False
    assert not staging_provider_allowed(**kwargs)
