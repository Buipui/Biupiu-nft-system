from dataclasses import dataclass
import hashlib
import hmac
import os
from typing import Optional

@dataclass
class AuthContext:
    subject: str
    scopes: tuple[str, ...] = ()

class DevelopmentTokenVerifier:
    """Development-only verifier. Production identity must use a real IdP/API gateway."""

    def __init__(self, expected_token: Optional[str] = None):
        self.expected_token = expected_token or os.getenv("BIUPIU_DEV_TOKEN", "")

    def verify(self, token: str) -> Optional[AuthContext]:
        if not self.expected_token:
            return None
        if hmac.compare_digest(token, self.expected_token):
            return AuthContext(subject="development-user", scopes=("ai:read", "experiment:write"))
        return None
