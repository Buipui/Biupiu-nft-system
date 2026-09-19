from biupiu_ai.self_healing import FailureEvent, RemediationRule, SelfHealingController, failure_signature

def controller_for(signature):
    rule = RemediationRule(
        rule_id="FIX-001", signature=signature, action="PATCH_CODE", risk="LOW",
        allowed_components=frozenset({"learning"}), max_files=2, max_attempts=3, requires_approval=False,
    )
    return SelfHealingController([rule], protected_files=frozenset({'software/rnd-os-ai/src/biupiu_ai/learning.py'}))

def test_verified_repair_is_learned():
    event = FailureEvent("F-001", "learning", "ValueError", "bad state")
    c = controller_for(failure_signature('learning', 'ValueError', 'bad state'))
    result = c.attempt(event, executor=lambda r,e:['candidate.py'], verifier=lambda e,f:True, rollback=lambda f:None, regression_test_added=True)
    assert result.tests_passed and result.state == 'LEARNED'
    assert result.learning_record is not None

def test_failed_repair_rolls_back():
    event = FailureEvent("F-002", "learning", "RuntimeError", "boom")
    c = controller_for(failure_signature('learning', 'RuntimeError', 'boom'))
    rolled=[]
    result = c.attempt(event, executor=lambda r,e:['candidate.py'], verifier=lambda e,f:False, rollback=lambda f:rolled.extend(f), regression_test_added=True)
    assert result.state == 'ROLLED_BACK' and result.rolled_back and rolled == ['candidate.py']

def test_protected_file_is_rejected():
    event = FailureEvent("F-003", "learning", "TypeError", "bad type")
    c = controller_for(failure_signature('learning', 'TypeError', 'bad type'))
    result = c.attempt(event, executor=lambda r,e:['software/rnd-os-ai/src/biupiu_ai/learning.py'], verifier=lambda e,f:True, rollback=lambda f:None, regression_test_added=True)
    assert result.state == 'ROLLED_BACK'

def test_circuit_breaker_escalates():
    event = FailureEvent("F-004", "learning", "IOError", "disk")
    c = controller_for(failure_signature('learning', 'IOError', 'disk'))
    for _ in range(3):
        result = c.attempt(event, executor=lambda r,e:['candidate.py'], verifier=lambda e,f:False, rollback=lambda f:None, regression_test_added=True)
    assert result.state == 'ESCALATED'

def test_code_patch_requires_regression_test():
    event = FailureEvent("F-005", "learning", "AssertionError", "regression")
    c = controller_for(failure_signature('learning', 'AssertionError', 'regression'))
    result = c.attempt(event, executor=lambda r,e:['candidate.py'], verifier=lambda e,f:True, rollback=lambda f:None, regression_test_added=False)
    assert result.state == 'ROLLED_BACK'