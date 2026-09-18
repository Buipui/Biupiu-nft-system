from dataclasses import dataclass, field
from typing import List

@dataclass
class ReplicationRecord:
    experiment_id: str
    environment: str
    outcome: str
    dataset_id: str
    deviations: List[str] = field(default_factory=list)

class ReplicationTracker:
    def summarize(self, records: List[ReplicationRecord]) -> dict:
        supported = sum(r.outcome == "supported" for r in records)
        unsupported = sum(r.outcome == "unsupported" for r in records)
        inconclusive = sum(r.outcome == "inconclusive" for r in records)
        return {
            "count": len(records),
            "supported": supported,
            "unsupported": unsupported,
            "inconclusive": inconclusive,
            "independent_environments": len({r.environment for r in records}),
        }
