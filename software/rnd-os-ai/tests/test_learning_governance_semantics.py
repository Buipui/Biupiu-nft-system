from biupiu_ai.learning import (
    LearningEvidence, FailurePattern, score_governed_learning_candidate,
    can_promote_learning,
)


def test_learning_promotion_defaults_to_fail_closed_on_licence():
    pattern = FailurePattern("x", 2, 2, 2, ("linux",), False, 4)
    assert not can_promote_learning(
        pattern, provenance_verified=True, human_approved=True
    )


def test_drift_penalty_reduces_candidate_model_disagreement():
    low = score_governed_learning_candidate(
        "low", LearningEvidence(
            verified_fix=1, regression_safety=1, provenance_quality=1,
            uncertainty_reduction=1, recurrence=1, drift_penalty=0
        )
    )
    high = score_governed_learning_candidate(
        "high", LearningEvidence(
            verified_fix=1, regression_safety=1, provenance_quality=1,
            uncertainty_reduction=1, recurrence=1, drift_penalty=1
        )
    )
    assert high.score < low.score
    assert high.model_disagreement < low.model_disagreement
