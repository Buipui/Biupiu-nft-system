"""Automated regression tests for the Biupiu composite screening prototype.

These tests verify mathematics and invariants only. They do not validate material
properties, cure constants, fatigue life, crashworthiness, or production safety.
"""
import math
import numpy as np

from composites_bioresins_screening import Lamina, laminate_abd, nth_order_cure, transformed_q


def test_reduced_stiffness_is_symmetric_and_positive_diagonal():
    ply = Lamina(35.0, 6.0, 0.30, 2.2, 0.25)
    q = ply.reduced_stiffness()
    assert np.allclose(q, q.T)
    assert np.all(np.diag(q) > 0)


def test_transformed_q_zero_degrees_matches_input():
    ply = Lamina(35.0, 6.0, 0.30, 2.2, 0.25)
    q = ply.reduced_stiffness()
    assert np.allclose(transformed_q(q, 0.0), q)


def test_transformed_q_ninety_swaps_longitudinal_and_transverse_axes():
    ply = Lamina(35.0, 6.0, 0.30, 2.2, 0.25)
    q = ply.reduced_stiffness()
    q90 = transformed_q(q, 90.0)
    assert math.isclose(q90[0, 0], q[1, 1], rel_tol=1e-10, abs_tol=1e-10)
    assert math.isclose(q90[1, 1], q[0, 0], rel_tol=1e-10, abs_tol=1e-10)
    assert math.isclose(q90[2, 2], q[2, 2], rel_tol=1e-10, abs_tol=1e-10)


def test_symmetric_layup_has_negligible_b_matrix():
    ply = Lamina(35.0, 6.0, 0.30, 2.2, 0.25)
    _, b, _ = laminate_abd(ply, [0.0, 45.0, -45.0, 90.0, 90.0, -45.0, 45.0, 0.0])
    assert np.max(np.abs(b)) < 1e-12


def test_abd_thickness_scaling_is_consistent():
    ply = Lamina(35.0, 6.0, 0.30, 2.2, 0.25)
    a1, _, _ = laminate_abd(ply, [0.0])
    a2, _, _ = laminate_abd(ply, [0.0, 0.0])
    assert np.allclose(a2, 2.0 * a1)


def test_cure_increment_is_bounded_and_monotonic_for_positive_rate():
    low = nth_order_cure(0.10, 393.15, 60.0, 1.0e5, 55000.0)
    high = nth_order_cure(0.10, 393.15, 120.0, 1.0e5, 55000.0)
    assert 0.10 <= low <= 1.0
    assert low <= high <= 1.0
