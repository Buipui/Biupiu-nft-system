from dataclasses import replace
from biupiu_ai.learning import (FailureObservation,can_promote_learning,fingerprint_failure,
    make_learning_record,score_learning_candidate,summarize_failure_pattern,update_drift_state,verify_learning_record)

def test_learning_record_is_deterministically_verifiable():
    r=make_learning_record("L-001","REPOSITORY_CHANGE","core",["commit:example"],"SUPPORTED","REPOSITORY_CHANGE","1.0.1","index synchronized",created_at="2026-09-19T00:00:00+00:00")
    assert verify_learning_record(r)

def test_tampering_is_detected():
    r=make_learning_record("L-002","EXPERIMENT","EXP-001",["dataset:001"],"INCONCLUSIVE","FAILURE","1.0","model error increased",next_action="CALIBRATE",created_at="2026-09-19T00:00:00+00:00")
    assert not verify_learning_record(replace(r,observed_outcome="tampered"))

def test_repeated_failure_stalls_without_new_evidence():
    fp=fingerprint_failure("runtime","same-state",target_id="core",platform="linux")
    xs=[FailureObservation("core","runtime",fp,"same-state",False,False,platform="linux")]*2
    p=summarize_failure_pattern(xs)
    assert p.stalled and p.learning_level==1

def test_verified_fix_and_cross_regression_becomes_reusable():
    fp=fingerprint_failure("interface","adapter-contract",target_id="router")
    xs=[FailureObservation("router","interface",fp,"adapter-contract",True,True,platform="windows"),
        FailureObservation("router","interface",fp,"adapter-contract-v2",True,True,platform="linux")]
    p=summarize_failure_pattern(xs)
    assert p.learning_level==4
    assert can_promote_learning(p,provenance_verified=True,human_approved=True)

def test_drift_detector_is_incremental():
    s=None
    for v in (0.10,0.11,0.12,0.30): s=update_drift_state(s,v,alpha=.5,threshold=.50)
    assert s.count==4 and s.ewma_error>s.baseline_error and s.drift_detected

def test_candidate_score_is_bounded():
    r=score_learning_candidate("candidate-1",information_gain=1,uncertainty_reduction=.8,model_disagreement=.5,feasibility=.9,regression_safety=1)
    assert 0<r.score<=1 and r.information_gain==1


def test_multilingual_learning_record_preserves_locale_metadata():
    from biupiu_ai.learning import make_multilingual_learning_record, verify_learning_record
    record = make_multilingual_learning_record(
        "mlang-001",
        "language-selector",
        "zh-Hant-TW",
        "zh",
        "fallback chain verified",
        input_refs=("harvest://foreign-language-20260922",),
    )
    assert verify_learning_record(record)
    assert "locale=zh-Hant-TW" in record.input_refs
    assert "source_language=zh" in record.input_refs
    assert record.target_type == "MULTILINGUAL_ROUTING"
