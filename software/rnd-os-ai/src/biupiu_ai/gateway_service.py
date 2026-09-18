from dataclasses import dataclass
from typing import Optional
from uuid import uuid4

from .auth_contract import validate_bearer_header
from .gateway_policy import GatewayPolicy, validate_request
from .model_context import GroundedContext
from .provider_adapter import ProviderAdapter
from .schemas import AiResult
from .gateway_state import GatewayState
from .audit_schema import DurableAuditEvent

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
    """Provider-neutral gateway with replay/rate and audit-state integration."""
    def __init__(
        self,
        provider: ProviderAdapter,
        policy: Optional[GatewayPolicy] = None,
        state: Optional[GatewayState] = None,
        client_key: str = "anonymous",
    ):
        self.provider = provider
        self.policy = policy or GatewayPolicy()
        self.state = state or GatewayState(self.policy.requests_per_minute)
        self.client_key = client_key

    def ask(
        self, *, authorization: Optional[str], task: str, evidence=None,
        dataset_versions=None, evidence_source_ids=None, dataset_version_ids=None,
        idempotency_key: Optional[str] = None,
    ) -> GatewayResponse:
        request_id = str(uuid4())
        auth = validate_bearer_header(authorization)
        if not auth.accepted:
            return self._error(request_id, "unauthorized", auth.reason)

        admission = self.state.admit(self.client_key, idempotency_key)
        if not admission.accepted:
            self.state.record(request_id, "gateway.rejected", admission.reason)
            return self._error(request_id, admission.reason, admission.reason)

        evidence = evidence or []
        dataset_versions = dataset_versions or []
        source_ids = evidence_source_ids or [e.source_id for e in evidence]
        dataset_ids = dataset_version_ids or [getattr(d, "version_id", str(d)) for d in dataset_versions]
        decision = validate_request(task, source_ids, dataset_ids, self.policy)
        if not decision.accepted:
            self.state.record(request_id, "gateway.rejected", decision.reason)
            return self._error(request_id, "invalid-request", decision.reason)

        context = GroundedContext(task, dataset_versions, evidence)
        try:
            result = self.provider.generate(context)
        except Exception as exc:
            error_type = type(exc).__name__
            self.state.record(request_id, "gateway.provider-failure", error_type)
            return self._error(request_id, "provider-failure", error_type)

        self.state.record(request_id, "gateway.accepted", "success")
        return GatewayResponse(True, request_id, result=result)

    @staticmethod
    def _error(request_id: str, code: str, message: str) -> GatewayResponse:
        return GatewayResponse(False, request_id, error=GatewayError(code, message, request_id))
