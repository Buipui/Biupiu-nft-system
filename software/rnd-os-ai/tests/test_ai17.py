from biupiu_ai.evidence import EvidenceRecord
from biupiu_ai.gateway_service import GatewayService
from biupiu_ai.schemas import AiResult


class FakeProvider:
    def generate(self, context):
        return AiResult("ok", "supported-by-current-evidence", context.source_ids())


class FailingProvider:
    def generate(self, context):
        raise TimeoutError("simulated")


def test_ai17_success_has_request_id_and_citations():
    response = GatewayService(FakeProvider()).ask(
        authorization="Bearer test-token",
        task="photonics",
        evidence=[EvidenceRecord("S1", "supported", "claim", "fixture")],
    )
    assert response.ok is True
    assert response.request_id
    assert response.result.citations == ["S1"]


def test_ai17_rejects_unauthenticated_request():
    response = GatewayService(FakeProvider()).ask(
        authorization=None,
        task="photonics",
    )
    assert response.ok is False
    assert response.error.code == "unauthorized"
    assert response.error.request_id == response.request_id


def test_ai17_contains_provider_failure():
    response = GatewayService(FailingProvider()).ask(
        authorization="Bearer test-token",
        task="photonics",
    )
    assert response.ok is False
    assert response.error.code == "provider-failure"
    assert response.error.message == "TimeoutError"
