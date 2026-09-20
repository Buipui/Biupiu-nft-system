from biupiu_ai.specialist_catalog import build_specialist_registry, execute_task_graph
from biupiu_ai.specialist_federation import Task


def test_catalog_registers_resident_specialists():
    registry = build_specialist_registry()
    assert len(registry.capabilities()) == 10
    assert registry.resident("quantum")[0].capability.name == "quantum-ai"
    assert registry.resident("agriculture")[0].capability.autonomous is True


def test_cross_specialist_handoff_chain_is_explicit():
    registry = build_specialist_registry()
    results = execute_task_graph(
        registry,
        (
            Task("q1", "quantum", {"experiment": "bell"}),
            Task("e1", "engineering", {"artifact": "quantum-result"}),
            Task("a1", "agriculture", {"artifact": "engineering-result"}),
        ),
    )
    assert [r.specialist for r in results] == [
        "quantum-ai", "engineering-simulation-ai", "agriculture-ai"
    ]
    assert all(r.status == "completed" for r in results)


def test_unknown_domain_fails_closed():
    registry = build_specialist_registry()
    result = execute_task_graph(registry, (Task("x1", "unknown", {}),))
    assert result[0].status == "unresolved"
