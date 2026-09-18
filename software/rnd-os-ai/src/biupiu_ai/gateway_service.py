from dataclasses import dataclass
from typing import Optional
from uuid import uuid4

from .auth_contract import validate_bearer_header
from .gateway_policy import GatewayPolicy, validate_request
from .model_context import GroundedContext
from .provider_adapter import ProviderAdapter
from .schemas import AiResult


@dataclass(frozen=True)
class GatewayError:
    code: str
    message: str
    request_id: str


@dataclass(frozen=True)
class GatewayResponse:
    ok: bool
    request_id: str
    result: Optional[AiResult] = None
    error: Optional[GatewayError] = None


class GatewayService:
    """Provider-neutral gateway orchestration.

    Authentication and policy are evaluated before a provider is invoked.
    The service never exposes provider secrets or provider-specific payloads.
    """

    def __init__(self, provider: ProviderAdapter, policy: Optional[GatewayPolicy] = None):
        self.provider = provider
        self.policy = policy or GatewayPolicy()

    def ask(
        self,
        *,
        authorization: Optional[str],
        task: str,
        evidence=None,
        dataset_versions=None,
        evidence_source_ids=None,
        dataset_version_ids=None,
    ) -> GatewayResponse:
        request_id = str(uuid4())
        auth = validate_bearer_header(authorization)
        if not auth.accepted:
            return self._error(request_id, "unauthorized", auth.reason)

        evidence = evidence or []
        dataset_versions = dataset_versions or []
        source_ids = evidence_source_ids or [e.source_id for e in evidence]
        dataset_ids = dataset_version_ids or [
            getattr(d, "version_id", str(d)) for d in dataset_versions
        ]
        decision = validate_request(task, source_ids, dataset_ids, self.policy)
        if not decision.accepted:
            return self._error(request_id, "invalid-request", decision.reason)

        context = GroundedContext(task, dataset_versions, evidence)
        try:
            result = self.provider.generate(context)
        except Exception as exc:
            return self._error(request_id, "provider-failure", type(exc).__name__)

        return GatewayResponse(True, request_id, result=result)

    @staticmethod
    def _error(request_id: str, code: str, message: str) -> GatewayResponse:
        return GatewayResponse(
            False,
            request_id,
            error=GatewayError(code, message, request_id),
        )
