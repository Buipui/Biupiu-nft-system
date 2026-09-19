from biupiu_ai.intelligence_core import dependency_closure, grounded, make_edge


def test_supported_edge_is_grounded():
    edge = make_edge("source-1", "claim-1", "SUPPORTS", "SUPPORTED", ["source-1"])
    assert grounded(edge)


def test_unsupported_edge_is_not_grounded():
    edge = make_edge("claim-1", "claim-2", "SUPPORTS", "UNSUPPORTED")
    assert not grounded(edge)


def test_dependency_closure():
    edges = [
        make_edge("A", "B", "DEPENDS_ON", "SUPPORTED"),
        make_edge("B", "C", "PRODUCES", "SUPPORTED"),
        make_edge("C", "D", "DEPENDS_ON", "SUPPORTED"),
    ]
    assert dependency_closure("A", edges) == {"A", "B", "C", "D"}
