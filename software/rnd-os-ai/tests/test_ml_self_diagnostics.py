from biupiu_ai.ml.self_diagnostics import diagnose_and_propose, diagnose_adaptation_bounds, diagnose_quantum_baseline

def test_ml_self_diagnostics_core_bounds():
    assert diagnose_adaptation_bounds().state == "PASS"
    assert diagnose_quantum_baseline().state == "PASS"

def test_ml_self_healing_is_bounded_and_fail_closed():
    report = diagnose_and_propose()
    assert report.overall_state in {"HEALTHY", "DEGRADED_REPAIR_PROPOSED"}
    assert report.promotion_allowed is False
    assert all(not r.promotion_allowed for r in report.repairs)

def test_repair_requires_validation_regression_and_human_approval():
    from biupiu_ai.ml.self_diagnostics import propose_repair, apply_validated_repair
    p = propose_repair("demo", "reversible repair", "FAILED")
    assert p.requires_validation and p.requires_regression and p.requires_human_approval
    assert not p.promotion_allowed
    q = apply_validated_repair(p, validation_passed=True, regression_passed=True, human_approved=True)
    assert q.promotion_allowed
