from typing import Protocol
from .model_context import GroundedContext
from .schemas import AiResult

class ModelProvider(Protocol):
    def generate(self, context: GroundedContext) -> AiResult: ...

class EvidenceGroundedDevelopmentProvider:
    def generate(self, context: GroundedContext) -> AiResult:
        citations = context.source_ids()
        if not context.evidence and not context.dataset_versions:
            return AiResult("Insufficient repository evidence for a grounded response.", "insufficient-evidence", citations)
        return AiResult("Development grounded response: review the cited evidence and versioned datasets before drawing conclusions.", "grounded-development", citations)
