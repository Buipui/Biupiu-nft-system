from biupiu_ai.math_problem_solver import Problem, classify_problem

def test_biology_and_quantum_taxonomy():
    tags = classify_problem(Problem(
        "bio-q",
        "optimize a quantum algorithm for protein folding from a genome-derived sequence",
        "biology",
        ("constraint: multi-omics",),
    ))
    assert "biology" in tags
    assert "molecular" in tags
    assert "quantum_algorithm" in tags
    assert "optimization" in tags
    assert "multi_omics" in tags
