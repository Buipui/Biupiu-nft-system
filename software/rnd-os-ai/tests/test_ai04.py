from biupiu_ai.evidence import EvidenceEngine, EvidenceRecord
from biupiu_ai.replication import ReplicationRecord, ReplicationTracker

def test_conflicting_evidence_is_not_collapsed():
    records = [
        EvidenceRecord("S1", "supported", "claim", "primary"),
        EvidenceRecord("S2", "contradictory", "claim", "primary", ["different conditions"]),
    ]
    result = EvidenceEngine().assess(records)
    assert result.state == "conflicted"

def test_replication_summary():
    records = [
        ReplicationRecord("E1", "lab-a", "supported", "D1"),
        ReplicationRecord("E1", "lab-b", "supported", "D2"),
        ReplicationRecord("E1", "lab-c", "inconclusive", "D3"),
    ]
    result = ReplicationTracker().summarize(records)
    assert result["count"] == 3
    assert result["independent_environments"] == 3
