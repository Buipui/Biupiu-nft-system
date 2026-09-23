from biupiu_biology import (
    BioPoint, collinear, distance, gc_fraction, hamming_distance,
    normalize_sequence, orientation, sequence_span,
)

def test_coordinate_primitives():
    a, b, c = BioPoint("chr1", 2), BioPoint("chr1", 5), BioPoint("chr1", 9)
    assert distance(a, b) == 3.0
    assert orientation(a, b, c) == 1
    assert collinear(a, b, c)
    assert sequence_span([a, b, c]) == 7.0

def test_sequence_primitives():
    assert normalize_sequence(" acgt ") == "ACGT"
    assert hamming_distance("ACGT", "AGGT") == 1
    assert gc_fraction("ACGT") == 0.5
