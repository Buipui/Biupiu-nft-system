from biupiu_ai.evidence import EvidenceRecord
from biupiu_ai.model_context import GroundedContext
from biupiu_ai.provider_harness import ProviderHarnessPolicy, ProviderTestHarness
from biupiu_ai.schemas import AiResult


def test_ai14_harness_accepts_grounded_provider_result():
    context = GroundedContext(
        "test task",
        evidence=[EvidenceRecord("S1", "supported", "test claim", "fixture")],
    )
    harness = ProviderTestHarness(ProviderHarnessPolicy())

    response = harness.invoke(
        context,
        lambda _: AiResult("grounded", "supported-by-current-evidence", ["S1"]),
    )

    assert response.ok is True
    assert response.error is None
    assert response.result.citations == ["S1"]


def test_ai14_harness_rejects_missing_citations():
    context = GroundedContext(
        "test task",
        evidence=[EvidenceRecord("S1", "supported", "test claim", "fixture")],
    )
    response = ProviderTestHarness(ProviderHarnessPolicy()).invoke(
        context,
        lambda _: AiResult("ungrounded", "supported-by-current-evidence", []),
    )

    assert response.ok is False
    assert response.error == "missing-citations"


def test_ai14_harness_contains_provider_failure():
    context = GroundedContext("test task")
    response = ProviderTestHarness(ProviderHarnessPolicy()).invoke(
        context,
        lambda _: (_ for _ in ()).throw(TimeoutError("simulated timeout")),
    )

    assert response.ok is False
    assert response.error == "provider-error:TimeoutError"
