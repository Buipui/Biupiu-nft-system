import pytest

from biupiu_ai.audit_store import FailingAuditStore, InMemoryAuditStore
from biupiu_ai.gateway_service import GatewayService
from biupiu_ai.open_resource_registry import OPEN_RESOURCES
from biupiu_ai.provider_adapter import ProviderHealth
from biupiu_ai.schemas import AiResult

NASA = "NASA-FPRIME"
AUTH = "Bearer test-token"

class StubProvider:
    def __init__(self, answer="stub-response"):
        self.answer = answer
        self.calls = 0
    def health(self):
        return ProviderHealth("stub", True, True, "test")
    def generate(self, context):
        self.calls += 1
        return AiResult(self.answer, "grounded", context.source_ids())

def test_ai27_authentication_gate_rejects_missing_header():
    p = StubProvider()
    response = GatewayService(p).ask(authorization=None, task="test", evidence_source_ids=[NASA])
    assert not response.ok
    assert response.error.code == "unauthorized"
    assert p.calls == 0

def test_ai27_end_to_end_accepts_valid_request_and_audits():
    p = StubProvider()
    store = InMemoryAuditStore()
    response = GatewayService(p, audit_store=store).ask(
        authorization=AUTH, task="test", evidence_source_ids=[NASA], idempotency_key="req-27")
    assert response.ok
    assert response.result.answer == "stub-response"
    assert p.calls == 1
    assert any(r["event"] == "gateway.accepted" for r in store.snapshot())

def test_ai27_unknown_provenance_blocks_provider():
    p = StubProvider()
    response = GatewayService(p).ask(
        authorization=AUTH, task="test", evidence_source_ids=["UNKNOWN"])
    assert not response.ok
    assert response.error.code == "invalid-provenance"
    assert p.calls == 0

def test_ai27_audit_failure_fails_closed_before_provider():
    p = StubProvider()
    response = GatewayService(p, audit_store=FailingAuditStore()).ask(
        authorization=AUTH, task="test", evidence_source_ids=[NASA])
    assert not response.ok
    assert response.error.code == "audit-store-unavailable"
    assert p.calls == 0

def test_ai27_provider_failure_is_audited_and_returned():
    class BrokenProvider(StubProvider):
        def generate(self, context):
            self.calls += 1
            raise RuntimeError("provider-down")
    p = BrokenProvider()
    store = InMemoryAuditStore()
    response = GatewayService(p, audit_store=store).ask(
        authorization=AUTH, task="test", evidence_source_ids=[NASA])
    assert not response.ok
    assert response.error.code == "provider-failure"
    assert any(r["event"] == "gateway.provider-failure" for r in store.snapshot())

def test_ai27_replay_idempotency_is_blocked():
    p = StubProvider()
    service = GatewayService(p)
    first = service.ask(authorization=AUTH, task="test", evidence_source_ids=[NASA], idempotency_key="same")
    second = service.ask(authorization=AUTH, task="test", evidence_source_ids=[NASA], idempotency_key="same")
    assert first.ok
    assert not second.ok
    assert second.error.code == "replay-detected"
    assert p.calls == 1
