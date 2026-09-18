from biupiu_ai.ai10_gateway import GroundedAiService
from biupiu_ai.evidence import EvidenceRecord
from biupiu_ai.model_provider import EvidenceGroundedDevelopmentProvider
from biupiu_ai.provider_adapter import FailClosedProviderAdapter, ProviderConfig
from biupiu_ai.retrieval_benchmark import RetrievalBenchmark, RetrievalCase


def test_ai13_provider_fails_closed_without_remote_credentials():
    adapter = FailClosedProviderAdapter(ProviderConfig("test-provider"))
    health = adapter.health()
    assert health.configured is False
    assert health.enabled is False


def test_ai13_end_to_end_grounded_pipeline():
    case = RetrievalCase("AI13-C1", "photonics", ["WITS-001", "RG-002"])
    retrieved = ["WITS-001", "RG-002"]
    score = RetrievalBenchmark().score(case, retrieved)
    assert score.recall == 1.0

    evidence = [
        EvidenceRecord(
            source_id="WITS-001",
            evidence_state="supported",
            claim="Structured-light optical communication can be studied as a research hypothesis.",
            provenance="repository evidence fixture",
        )
    ]
    result = GroundedAiService(EvidenceGroundedDevelopmentProvider()).answer(
        "Assess the photonics research object.",
        evidence=evidence,
    )
    assert result.citations == ["WITS-001"]
    assert result.evidence_state == "grounded-development"
