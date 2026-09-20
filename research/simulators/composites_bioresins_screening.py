"""Biupiu screening prototype: CLT laminate mechanics and simple cure kinetics.

Research tool only. Inputs must be validated experimentally before engineering use.
"""
from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class Lamina:
    e1_gpa: float
    e2_gpa: float
    nu12: float
    g12_gpa: float
    thickness_mm: float

    def reduced_stiffness(self) -> np.ndarray:
        e1, e2, g, nu = self.e1_gpa, self.e2_gpa, self.g12_gpa, self.nu12
        nu21 = nu * e2 / e1
        d = 1.0 - nu * nu21
        return np.array([[e1 / d, nu * e2 / d, 0.0],
                         [nu * e2 / d, e2 / d, 0.0],
                         [0.0, 0.0, g]])


def transformed_q(q: np.ndarray, angle_deg: float) -> np.ndarray:
    t = math.radians(angle_deg)
    m, n = math.cos(t), math.sin(t)
    q11, q12, q22, q66 = q[0, 0], q[0, 1], q[1, 1], q[2, 2]
    q16 = (q11 - q12 - 2*q66) * m**3 * n - (q22 - q12 - 2*q66) * m * n**3
    q26 = (q11 - q12 - 2*q66) * m * n**3 - (q22 - q12 - 2*q66) * m**3 * n
    qbar11 = q11*m**4 + 2*(q12+2*q66)*m*m*n*n + q22*n**4
    qbar22 = q11*n**4 + 2*(q12+2*q66)*m*m*n*n + q22*m**4
    qbar12 = (q11+q22-4*q66)*m*m*n*n + q12*(m**4+n**4)
    qbar66 = (q11+q22-2*q12-2*q66)*m*m*n*n + q66*(m**4+n**4)
    return np.array([[qbar11, qbar12, q16], [qbar12, qbar22, q26], [q16, q26, qbar66]])


def laminate_abd(lamina: Lamina, angles_deg: Iterable[float]):
    angles = list(angles_deg)
    total_t = sum(lamina.thickness_mm for _ in angles)
    z = np.linspace(-total_t / 2, total_t / 2, len(angles) + 1)
    a = np.zeros((3, 3)); b = np.zeros((3, 3)); d = np.zeros((3, 3))
    q = lamina.reduced_stiffness()
    for i, angle in enumerate(angles):
        qb = transformed_q(q, angle)
        z0, z1 = z[i], z[i + 1]
        a += qb * (z1-z0)
        b += 0.5 * qb * (z1**2-z0**2)
        d += (1/3) * qb * (z1**3-z0**3)
    return a, b, d


def nth_order_cure(alpha: float, temperature_k: float, time_s: float, k0: float, ea_j_mol: float, order: float = 1.0):
    """Single-step illustrative cure increment; calibrate constants using DSC data."""
    r = 8.314462618
    k = k0 * math.exp(-ea_j_mol / (r * temperature_k))
    return max(0.0, min(1.0, alpha + time_s * k * max(1e-12, 1-alpha)**order))


if __name__ == "__main__":
    ply = Lamina(e1_gpa=35.0, e2_gpa=6.0, nu12=0.30, g12_gpa=2.2, thickness_mm=0.25)
    a, b, d = laminate_abd(ply, [0, 45, -45, 90])
    print("A matrix (GPa·mm):\n", a)
    print("B matrix (GPa·mm²):\n", b)
    print("D matrix (GPa·mm³):\n", d)
    print("Illustrative cure alpha:", nth_order_cure(0.10, 393.15, 60.0, 1.0e5, 55000.0))
