from math_solver import MathSolver, Problem, Candidate

def test_solver_records_failure_without_crashing():
    def failing(problem):
        raise ValueError("expected test failure")

    record = MathSolver([failing]).solve(Problem("x + 1 = 2"))
    assert record.status == "unsolved"
    assert record.verification["solver_failures"][0]["error_type"] == "ValueError"


def test_solver_accepts_verified_candidate():
    def solver(problem):
        return Candidate("test", 1, residual=0.0)

    def verify(problem, candidates):
        return {"verified": bool(candidates and candidates[0].residual == 0.0)}

    record = MathSolver([solver], verify).solve(Problem("x = 1"))
    assert record.status == "verified_candidate"
