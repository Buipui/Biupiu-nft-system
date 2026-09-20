from biupiu_ai.learning_integration import route_learning_event, build_failure_learning_event

def test_core_promotion_fails_closed():
    d=route_learning_event({"target":"Biupiu Core OS","action":"PROMOTE_CORE","evidence_state":"SUPPORTED","human_approved":True})
    assert d.requires_os_validation and not d.promotion_allowed

def test_uncertain_evidence_cannot_promote():
    d=route_learning_event({"action":"PROMOTE_CORE","evidence_state":"INCONCLUSIVE"})
    assert not d.promotion_allowed

def test_failure_event_routes_into_learning():
    e=build_failure_learning_event("router","interface","adapter-contract",platform="linux")
    assert e["action"]=="LEARN"
    assert e["requires_os_validation"] is True
    assert e["failure_fingerprint"]
