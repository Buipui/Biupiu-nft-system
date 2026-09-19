from biupiu_ai.math_problem_solver import Problem, VerificationLevel, classify_problem, verify_invariants, verify_residual

def test_classification():
    p = Problem('p1', 'minimize a constrained polygon mesh', 'geometry', ('constraint: positive scale',))
    tags = classify_problem(p)
    assert 'geometry' in tags and 'optimization' in tags

def test_residual_acceptance():
    r = verify_residual('p2', 0.001, 0.01)
    assert r.level is VerificationLevel.NUMERICAL and r.accepted()

def test_residual_rejection():
    assert not verify_residual('p3', 0.1, 0.01).accepted()

def test_invariants():
    r = verify_invariants('p4', {'x': 2}, [lambda v: v['x'] > 0])
    assert r.level is VerificationLevel.DETERMINISTIC and r.accepted()