from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class RetrievalItem:
    source_id: str
    title: str
    excerpt: str
    evidence_state: str = "unclassified"

@dataclass
class AiContext:
    task: str
    research_object_id: Optional[str] = None
    evidence: List[RetrievalItem] = field(default_factory=list)

@dataclass
class AiResult:
    answer: str
    evidence_state: str
    citations: List[str] = field(default_factory=list)
    hypotheses: List[str] = field(default_factory=list)
