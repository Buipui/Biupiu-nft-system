from biupiu_ai.specialist_federation import Result
from biupiu_ai.specialist_state import build_state_store
from biupiu_ai.learning_bridge import evaluate_result, ingest_result


def test_unvalidated_specialist_result_stays_candidate():
    store = build_state_store()
    result = Result("t1", "agriculture-ai", "completed", {"crop": "hemp"}, confidence=0.8)
    evaluation = evaluate_result(result, validation_status="screening")
    event = ingest_result(store, result, evaluation)
    assert event.outcome == "candidate"
    assert event.promotion_eligible is False


def test_validated_result_can_enter_promotion_queue():
    store = build_state_store()
    result = Result("t2", "engineering-simulation-ai", "completed", {}, confidence=0.95,
                    provenance={"model_version": "1.2"})
    evaluation = evaluate_result(
        result, evidence_class="MODEL_OUTPUT", drift_status="pass",
        regression_status="pass", provenance_ok=True,
        validation_status="independently_reviewed",
    )
    event = ingest_result(store, result, evaluation)
    assert event.outcome == "validated"
    assert event.promotion_eligible is True
    assert store.promotable_events()[0].model_version == "1.2"
