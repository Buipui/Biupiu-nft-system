from biupiu_ai.intelligence_core import (
    AgentTask,
    route_task,
    validate_agent_result,
    dependency_closure,
    make_edge,
)


def test_routes_ai_task_to_intelligence():
    task = AgentTask(
        task_id="T-001",
        objective="analyse agent orchestration",
        domains=("AI", "COMPUTE"),
        irreversible=False,
        evidence_refs=("OPENAI-AGENTS-PY",),
    )
    decision = route_task(task)
    assert "AI" in decision.domains
    assert decision.requires_human_approval is False


def test_irreversible_task_requires_human_approval():
    task = AgentTask(
        task_id="T-002",
        objective="publish an IP release",
        domains=("AI", "BLOCKCHAIN"),
        irreversible=True,
        evidence_refs=("OPENAI-EVALS",),
    )
    decision = route_task(task)
    assert decision.requires_human_approval is True


def test_result_rejects_missing_provenance():
    assert validate_agent_result(
        evidence_refs=(),
        evidence_state="SUPPORTED",
        human_approved=False,
        irreversible=False,
    ) is False


def test_dependency_closure_remains_deterministic():
    edges = [
        make_edge("A", "B", "DEPENDS_ON", "SUPPORTED"),
        make_edge("B", "C", "PRODUCES", "SUPPORTED"),
    ]
    assert dependency_closure("A", edges) == {"A", "B", "C"}
