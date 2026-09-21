from biupiu_ai.native_system_harness import build_initial_harness

def test_initial_harvest_and_events_are_deterministic():
    harness = build_initial_harness()
    snapshot = harness.snapshot()
    assert snapshot["harvest_count"] == 9
    assert snapshot["event_count"] == 3
    assert all(event["digest"] for event in snapshot["events"])

def test_release_requires_all_gates():
    harness = build_initial_harness()
    assert not harness.release_ready(tests_passed=True, provenance_verified=True, human_approved=False)
    assert not harness.release_ready(tests_passed=False, provenance_verified=True, human_approved=True)
    assert harness.release_ready(tests_passed=True, provenance_verified=True, human_approved=True)
