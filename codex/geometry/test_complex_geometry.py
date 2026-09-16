import math

from complex_geometry import hourglass, nested_spirals, nested_wave, stacked_tori, torus, vortex_ring, helix


def test_torus_is_deterministic_and_correct_size():
    a = torus(4.0, 1.0, 8, 6)
    b = torus(4.0, 1.0, 8, 6)
    assert a == b
    assert len(a) == 48


def test_stacked_tori_count():
    assert len(stacked_tori(3, 4.0, 1.0, 2.0)) == 3 * 64 * 32


def test_helix_endpoints():
    points = helix(2.0, 3.0, 1.0, 11)
    assert len(points) == 11
    assert math.isclose(points[0][0], 2.0)
    assert math.isclose(points[-1][0], 2.0)


def test_nested_spirals():
    result = nested_spirals([1.0, 2.0], 2.0, 10)
    assert len(result) == 2
    assert len(result[0]) == 10


def test_hourglass_profile():
    result = hourglass([-1.0, 0.0, 1.0], 1.0, 2.0)
    assert result[1] == (1.0, 0.0, 0.0)
    assert result[0][0] == result[2][0]


def test_nested_wave_zero_at_origin():
    result = nested_wave([0.0], [1.0, 2.0], [3.0, 5.0])
    assert math.isclose(result[0], 0.0)


def test_vortex_ring_closed_geometry():
    result = vortex_ring(5.0, 0.5, 32)
    assert len(result) == 32
    assert math.isclose(result[0][0], 5.0)
