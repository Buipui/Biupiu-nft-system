from biupiu_ai.evaluation import EvaluationCase, GroundingEvaluator
from biupiu_ai.model_context import GroundedContext
from biupiu_ai.model_provider import EvidenceGroundedDevelopmentProvider
from biupiu_ai.evidence import EvidenceRecord

def test_grounding_evaluation():
    evidence = [EvidenceRecord("S1", "supported", "claim", "primary")]
    context = GroundedContext("test", [], evidence)
    case = EvaluationCase("C1", "test", ["S1"], "grounded-development")
    result = GroundingEvaluator().evaluate(EvidenceGroundedDevelopmentProvider(), case, context)
    assert result.grounded
    assert result.state_match

def test_missing_source_is_detected():
    context = GroundedContext("test", [], [])
    case = EvaluationCase("C2", "test", ["S1"], "insufficient-evidence")
    result = GroundingEvaluator().evaluate(EvidenceGroundedDevelopmentProvider(), case, context)
    assert not result.grounded
    assert result.state_match
