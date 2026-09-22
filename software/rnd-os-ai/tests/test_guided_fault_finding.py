from biupiu_ai.guided_fault_finding import guide_fault,learn_fault,federate_fault
from biupiu_ai.learning_federation_bridge import AppendOnlyLearningLog

def test_contract():
    r=guide_fault({"fault_class":"CONTRACT","message":"schema","state_signature":"v1-v2","evidence_refs":["e"]})
    assert r.next_step=="validate schema/version/content-type"

def test_security():
    assert guide_fault({"fault_class":"SECURITY"}).state=="QUARANTINED"

def test_learning_is_bounded():
    r=learn_fault({"fault_class":"CONTRACT","state_signature":"schema-mismatch","evidence_refs":["e"]})
    assert r["failure_class"]=="interface"
    assert r["promotion_allowed"] is False

def test_federation_logs_and_remains_fail_closed(tmp_path):
    log=AppendOnlyLearningLog(tmp_path/"learning.jsonl")
    r=federate_fault(log,{"fault_id":"F-1","fault_class":"RUNTIME","target_id":"core-os","state_signature":"timeout","platform":"ci","evidence_refs":["ci-run"]})
    assert r["state"]=="TRIAGING"
    assert r["promotion_allowed"] is False
    assert len(log.read())==1
