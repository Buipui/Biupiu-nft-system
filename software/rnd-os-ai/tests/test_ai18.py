from biupiu_ai.gateway_state import GatewayState


def test_ai18_replay_is_rejected():
    state = GatewayState()
    assert state.admit("client-a", "idem-1").accepted
    decision = state.admit("client-a", "idem-1")
    assert decision.reason == "replay-detected"


def test_ai18_rate_limit_is_enforced():
    state = GatewayState(requests_per_minute=2)
    assert state.admit("client-a", "a").accepted
    assert state.admit("client-a", "b").accepted
    assert state.admit("client-a", "c").reason == "rate-limit-exceeded"


def test_ai18_audit_events_are_recorded():
    state = GatewayState()
    state.record("req-1", "gateway.accepted", "success")
    events = state.audit_snapshot()
    assert len(events) == 1
    assert events[0].request_id == "req-1"
    assert events[0].outcome == "success"
