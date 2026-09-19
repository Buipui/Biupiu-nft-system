from __future__ import annotations

"""Biupiu computational geometry primitives.
Original implementation, inspired by published geometric problem-solving patterns.
External theorem provers remain optional adapters.
"""

from dataclasses import dataclass
from math import hypot
from typing import Iterable

EPS = 1e-12

@dataclass(frozen=True)
class Point2:
    x: float
    y: float

def distance(a: Point2, b: Point2) -> float:
    return hypot(a.x - b.x, a.y - b.y)

def orientation(a: Point2, b: Point2, c: Point2) -> int:
    det = (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)
    if det > EPS: return 1
    if det < -EPS: return -1
    return 0

def collinear(a: Point2, b: Point2, c: Point2) -> bool:
    return orientation(a, b, c) == 0

@dataclass(frozen=True)
class Segment2:
    a: Point2
    b: Point2

def polygon_area(points: Iterable[Point2]) -> float:
    pts = list(points)
    if len(pts) < 3: return 0.0
    return 0.5 * abs(sum(
        pts[i].x * pts[(i+1) % len(pts)].y -
        pts[(i+1) % len(pts)].x * pts[i].y
        for i in range(len(pts))
    ))
