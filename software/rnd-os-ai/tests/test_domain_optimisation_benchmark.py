from biupiu_ai.domain_optimisation_benchmark import grid_search

def test_common_optimiser_geometry_and_biology_encodings():
    geometry = grid_search("geometry", [1.0, 1.5, 2.0, 2.5], lambda x: x * x, 4.0)
    biology = grid_search("biology", [0.25, 0.5, 0.75, 1.0], lambda x: x, 0.75)
    assert geometry.verified
    assert biology.verified
    assert geometry.evaluations == biology.evaluations == 4
