from dataclasses import replace

from biupiu_ai.learning import make_learning_record, verify_learning_record


def test_learning_record_is_deterministically_verifiable():
    record = make_learning_record(
        learning_id="L-001",
        target_type="REPOSITORY_CHANGE",
        target_id="core-maintenance",
        input_refs=["commit:example"],
        evidence_state="SUPPORTED",
        knowledge_class="REPOSITORY_CHANGE",
        result_version="1.0.1",
        observed_outcome="index synchronized",
        next_action="REVIEW",
        created_at="2026-09-19T00:00:00+00:00",
    )
    assert verify_learning_record(record)


def test_tampering_is_detected():
    record = make_learning_record(
        learning_id="L-002",
        target_type="EXPERIMENT",
        target_id="EXP-001",
        input_refs=["dataset:001"],
        evidence_state="INCONCLUSIVE",
        knowledge_class="FAILURE",
        result_version="1.0",
        observed_outcome="model error increased",
        next_action="CALIBRATE",
        created_at="2026-09-19T00:00:00+00:00",
    )
    tampered = replace(record, observed_outcome="tampered")
    assert not verify_learning_record(tampered)
