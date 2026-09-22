from biupiu_ai.guided_fault_finding import guide_fault,learn_fault
def test_contract(): r=guide_fault({"fault_class":"CONTRACT","message":"schema","state_signature":"v1-v2","evidence_refs":["e"]}); assert r.next_step=="validate schema/version/content-type"
def test_security(): assert guide_fault({"fault_class":"SECURITY"}).state=="QUARANTINED"
def test_learning_is_bounded(): assert learn_fault({"fault_class":"runtime","state_signature":"timeout"})["promotion_allowed"] is False
