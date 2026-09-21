from biupiu_ai.specialist_state import (
    Handoff, LearningEvent, ModuleOwnership, SpecialistIdentity, build_state_store
)


def test_identity_and_module_ownership():
    store = build_state_store()
    store.register_identity(SpecialistIdentity("agriculture-ai", "1.0", ("agriculture", "water")))
    store.bind_module(ModuleOwnership("agriculture-ai", "FARM-SIM-01", "farm.md", "verified", "1.0"))
    assert store.ownership[0].module_id == "FARM-SIM-01"


def test_learning_requires_validation_for_promotion():
    store = build_state_store()
    store.register_identity(SpecialistIdentity("engineering-simulation-ai", "1.0", ("engineering",)))
    store.record_learning(LearningEvent("l1", "engineering-simulation-ai", "t1", "candidate", model_version="1.1", promotion_eligible=True))
    store.record_learning(LearningEvent("l2", "engineering-simulation-ai", "t2", "validated", model_version="1.2", promotion_eligible=True))
    assert [e.event_id for e in store.promotable_events()] == ["l2"]


def test_handoff_is_closed_until_explicitly_approved():
    store = build_state_store()
    store.register_identity(SpecialistIdentity("agriculture-ai", "1.0", ("agriculture",)))
    store.register_identity(SpecialistIdentity("engineering-simulation-ai", "1.0", ("engineering",)))
    denied = Handoff("t1", "agriculture-ai", "engineering-simulation-ai", "materials calculation")
    assert store.request_handoff(denied) is False
    approved = Handoff("t2", "agriculture-ai", "engineering-simulation-ai", "materials calculation", ("FARM-SIM-01",), True)
    assert store.request_handoff(approved) is True
