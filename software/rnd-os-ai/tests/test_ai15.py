from biupiu_ai.auth_contract import redact_authorization, validate_bearer_header


def test_ai15_accepts_bearer_shape_without_inspecting_secret():
    decision = validate_bearer_header("Bearer secret-token")
    assert decision.accepted is True


def test_ai15_rejects_missing_or_malformed_authorization():
    assert validate_bearer_header(None).reason == "missing-authorization"
    assert validate_bearer_header("secret-token").accepted is False
    assert validate_bearer_header("Basic abc").accepted is False


def test_ai15_redacts_authorization():
    assert redact_authorization("Bearer secret-token") == "Bearer <redacted>"
    assert "secret-token" not in redact_authorization("Bearer secret-token")
