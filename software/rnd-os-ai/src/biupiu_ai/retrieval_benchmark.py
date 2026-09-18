from dataclasses import dataclass
from typing import List

@dataclass
class RetrievalCase:
    case_id: str
    query: str
    expected_source_ids: List[str]

@dataclass
class RetrievalScore:
    case_id: str
    retrieved_source_ids: List[str]
    recall: float

class RetrievalBenchmark:
    def score(self, case: RetrievalCase, retrieved_source_ids: List[str]) -> RetrievalScore:
        expected = set(case.expected_source_ids)
        retrieved = set(retrieved_source_ids)
        recall = 1.0 if not expected else len(expected & retrieved) / len(expected)
        return RetrievalScore(case.case_id, list(retrieved_source_ids), recall)
