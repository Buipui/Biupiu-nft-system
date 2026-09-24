from biupiu_ai.computational_learning_map import build_learning_map

def test_geometry_map_is_deterministic_and_graph_based():
    records = [
        {"node_id": "A", "system_id": "AI-1", "task_code": "T1", "department": "INTELLIGENCE", "evidence_level": 4, "collaboration": 1, "recurrence": 0.5, "depends_on": ["B"]},
        {"node_id": "B", "system_id": "AI-2", "task_code": "T2", "department": "ORCHESTRA", "evidence_level": 3, "collaboration": 0.5, "recurrence": 0.2},
    ]
    a = build_learning_map(records)
    b = build_learning_map(records)
    assert a == b
    assert len(a.nodes) == 2
    assert len(a.edges) == 1
