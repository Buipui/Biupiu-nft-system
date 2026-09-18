from dataclasses import dataclass, field
from typing import List

@dataclass
class EvidenceRecord:
    source_id: str
    evidence_state: str
    claim: str
    provenance: str
    limitations: List[str] = field(default_factory=list)
    confidence_note: str = ""

@dataclass
class EvidenceAssessment:
    state: str
    supporting_sources: List[str]
    contradicting_sources: List[str]
    limitations: List[str]
    replication_count: int

class EvidenceEngine:
    """Evidence-state engine; it does not convert model output into fact."""

    def assess(self, records: List[EvidenceRecord], replication_count: int = 0) -> EvidenceAssessment:
        supporting = [r.source_id for r in records if r.evidence_state in {"primary", "replicated", "supported"}]
        contradicting = [r.source_id for r in records if r.evidence_state in {"contradictory", "unsupported"}]
        limitations = [x for r in records for x in r.limitations]
        if contradicting and supporting:
            state = "conflicted"
        elif replication_count > 0 and supporting:
            state = "replicated-support"
        elif supporting:
            state = "supported-by-current-evidence"
        else:
            state = "insufficient-evidence"
        return EvidenceAssessment(state, supporting, contradicting, limitations, replication_count)
