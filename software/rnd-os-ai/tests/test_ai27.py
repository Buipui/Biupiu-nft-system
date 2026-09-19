from biupiu_ai.gateway_service import GatewayService
from biupiu_ai.gateway_policy import GatewayPolicy
from biupiu_ai.provider_adapter import ProviderHealth
from biupiu_ai.schemas import AiResult
from biupiu_ai.audit_store import InMemoryAuditStore, FailingAuditStore

class StubProvider:
    def __init__(self, error=None):
        self.error = error
    def health(self):
        return ProviderHealth("stub", True, True, "ready")
    def generate(self, context):
        if self.error:
            raise self.error
        return AiResult("ok", "grounded-development", ["NASA-FPRIME"])

def make(store=None, provider=None, rpm=30):
    return GatewayService(provider or StubProvider(), GatewayPolicy(requests_per_minute=rpm),
                           client_key="ai27-client", audit_store=store or InMemoryAuditStore())

def ask(service, **kwargs):
    return service.ask(authorization="Bearer test-token", task="photonics",
                       evidence_source_ids=["NASA-FPRIME"], **kwargs)

def test_ai27_authentication_failure():
    response = make().ask(authorization=None, task="photonics", evidence_source_ids=["NASA-FPRIME"])
    assert not response.ok and response.error.code == "unauthorized"

def test_ai27_provenance_rejection():
    response = make().ask(authorization="Bearer test-token", task="photonics",
                           evidence_source_ids=["UNKNOWN"])
    assert not response.ok and response.error.code == "invalid-provenance"

def test_ai27_provider_execution_and_audit():
    store = InMemoryAuditStore()
    response = ask(make(store))
    assert response.ok
    assert len(store.snapshot()) == 1

def test_ai27_provider_failure():
    response = ask(make(provider=StubProvider(RuntimeError("provider-down"))))
    assert not response.ok and response.error.code == "provider-failure"

def test_ai27_replay_control():
    service = make()
    first = ask(service, idempotency_key="same-request")
    second = ask(service, idempotency_key="same-request")
    assert first.ok
    assert not second.ok and second.error.code == "replay-detected"

def test_ai27_rate_control():
    service = make(rpm=1)
    first = ask(service)
    second = ask(service)
    assert first.ok
    assert not second.ok and second.error.code == "rate-limit-exceeded"

def test_ai27_audit_store_failure_fails_closed():
    response = ask(make(FailingAuditStore()))
    assert not response.ok and response.error.code == "audit-store-unavailable"
