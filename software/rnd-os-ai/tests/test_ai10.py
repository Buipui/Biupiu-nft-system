from biupiu_ai.ai10_gateway import GroundedAiService
from biupiu_ai.model_provider import EvidenceGroundedDevelopmentProvider
from biupiu_ai.storage import DatasetVersion
from biupiu_ai.evidence import EvidenceRecord

def test_grounded_response_carries_citations():
    service = GroundedAiService(EvidenceGroundedDevelopmentProvider())
    evidence = [EvidenceRecord("S1", "supported", "claim", "primary")]
    result = service.answer("analyse claim", [DatasetVersion("D1",1,"hash","2026-09-18T00:00:00Z","user")], evidence)
    assert result.evidence_state == "grounded-development"
    assert result.citations == ["S1"]

def test_no_context_is_insufficient():
    result = GroundedAiService(EvidenceGroundedDevelopmentProvider()).answer("analyse")
    assert result.evidence_state == "insufficient-evidence"
