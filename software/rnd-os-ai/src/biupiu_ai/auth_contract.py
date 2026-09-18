from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class AuthDecision:
    accepted: bool
    reason: str


def validate_bearer_header(
    authorization: Optional[str],
    *,
    expected_scheme: str = "Bearer",
) -> AuthDecision:
    if not authorization:
        return AuthDecision(False, "missing-authorization")
    parts = authorization.split(" ", 1)
    if len(parts) != 2 or parts[0] != expected_scheme or not parts[1].strip():
        return AuthDecision(False, "invalid-authorization-format")
    return AuthDecision(True, "bearer-token-present")


def redact_authorization(authorization: Optional[str]) -> str:
    if not authorization:
        return "<none>"
    parts = authorization.split(" ", 1)
    if len(parts) != 2:
        return "<redacted>"
    return f"{parts[0]} <redacted>"
