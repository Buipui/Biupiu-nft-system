from dataclasses import dataclass
from typing import Protocol, Optional

from .model_provider import ModelProvider
from .model_context import GroundedContext
from .schemas import AiResult


@dataclass(frozen=True)
class ProviderConfig:
    provider_id: str
    endpoint: Optional[str] = None
    api_key_env: Optional[str] = None
    enabled: bool = False


@dataclass(frozen=True)
class ProviderHealth:
    provider_id: str
    configured: bool
    enabled: bool
    reason: str


class ProviderAdapter(Protocol):
    def health(self) -> ProviderHealth: ...
    def generate(self, context: GroundedContext) -> AiResult: ...


class FailClosedProviderAdapter:
    """Production boundary: never fabricates a remote-model response.

    A real provider must be explicitly configured and implemented behind this
    interface. Secrets are referenced by environment-variable name only.
    """

    def __init__(self, config: ProviderConfig):
        self.config = config

    def health(self) -> ProviderHealth:
        configured = bool(self.config.provider_id and self.config.endpoint and self.config.api_key_env)
        if not configured:
            return ProviderHealth(self.config.provider_id, False, False, "provider configuration incomplete")
        if not self.config.enabled:
            return ProviderHealth(self.config.provider_id, True, False, "provider disabled")
        return ProviderHealth(self.config.provider_id, True, True, "adapter boundary ready")

    def generate(self, context: GroundedContext) -> AiResult:
        health = self.health()
        if not health.enabled:
            citations = context.source_ids()
            return AiResult(
                "External model execution is not enabled; no remote response was generated.",
                "provider-disabled",
                citations,
            )
        raise NotImplementedError("Remote transport must be implemented by a provider-specific adapter.")
