from biupiu_ai.audit_store import InMemoryAuditStore
from biupiu_ai.gateway_service import GatewayService
from biupiu_ai.schemas import AiResult

class FakeProvider:
    def generate(self, context):
        return AiResult("ok", "supported-by-current-evidence", [])

def test_ai21_gateway_persists_success_audit():
    store = InMemoryAuditStore()
    response = GatewayService(FakeProvider(), audit_store=store, client_key="client-a").ask(
        authorization="Bearer token", task="test"
    )
    assert response.ok
    records = store.snapshot()
    assert records[-1]["request_id"] == response.request_id
    assert records[-1]["event"] == "gateway.accepted"

def test_ai21_gateway_persists_replay_error():
    store = InMemoryAuditStore()
    service = GatewayService(FakeProvider(), audit_store=store, client_key="client-a")
    service.ask(authorization="Bearer token", task="test", idempotency_key="same")
    response = service.ask(authorization="Bearer token", task="test", idempotency_key="same")
    assert response.error.code == "replay-detected"
    assert store.snapshot()[-1]["error_code"] == "replay-detected"
