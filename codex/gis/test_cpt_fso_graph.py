from cpt_fso_graph import Node, candidate_edges, corridor_graph, distance_m


def test_distance_is_symmetric_and_positive():
    a = Node("A", -33.925, 18.420, "public", "src-a")
    b = Node("B", -33.930, 18.430, "public", "src-b")
    assert distance_m(a, b) == distance_m(b, a)
    assert distance_m(a, b) > 0


def test_candidate_edges_are_deterministic():
    a = Node("A", -33.925, 18.420, "public", "src-a")
    b = Node("B", -33.926, 18.421, "public", "src-b")
    c = Node("C", -34.100, 18.700, "public", "src-c")
    edges = candidate_edges([c, b, a], 500)
    assert [(e.source, e.target) for e in edges] == [("A", "B")]


def test_graph_contains_validation_gates():
    a = Node("A", -33.925, 18.420, "public", "src-a")
    graph = corridor_graph([a], 500)
    assert graph["status"] == "research_screening"
    assert "terrain_and_building_LOS" in graph["validation_gates"]
    assert len(graph["nodes"]) == 1
