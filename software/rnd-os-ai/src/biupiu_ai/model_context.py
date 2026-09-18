from dataclasses import dataclass, field
from typing import List
from .storage import DatasetVersion
from .evidence import EvidenceRecord

@dataclass
class GroundedContext:
    task: str
    dataset_versions: List[DatasetVersion] = field(default_factory=list)
    evidence: List[EvidenceRecord] = field(default_factory=list)

    def source_ids(self) -> list[str]:
        return [e.source_id for e in self.evidence]
