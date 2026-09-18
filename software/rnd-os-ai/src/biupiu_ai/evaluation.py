from dataclasses import dataclass
from typing import List
from .model_context import GroundedContext
from .model_provider import ModelProvider

@dataclass
class EvaluationCase:
    case_id: str
    task: str
    expected_source_ids: List[str]
    expected_state: str

@dataclass
class EvaluationResult:
    case_id: str
    grounded: bool
    state_match: bool
    missing_sources: List[str]

class GroundingEvaluator:
    def evaluate(self, provider: ModelProvider, case: EvaluationCase, context: GroundedContext) -> EvaluationResult:
        result = provider.generate(context)
        missing = [s for s in case.expected_source_ids if s not in result.citations]
        return EvaluationResult(
            case.case_id,
            grounded=not missing,
            state_match=result.evidence_state == case.expected_state,
            missing_sources=missing,
        )
