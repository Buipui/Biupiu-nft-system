from typing import Protocol
from .schemas import AiContext, AiResult

class AiProvider(Protocol):
    def generate(self, context: AiContext) -> AiResult: ...

class DeterministicProvider:
    """Development provider used until a real model/API is configured."""
    def generate(self, context: AiContext) -> AiResult:
        citations = [x.source_id for x in context.evidence]
        return AiResult(
            answer=("Development AI response. Retrieved evidence must be reviewed "
                    "before conclusions are treated as established findings."),
            evidence_state="development",
            citations=citations,
        )
