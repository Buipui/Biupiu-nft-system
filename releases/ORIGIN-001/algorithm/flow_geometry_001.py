"""BIUPIU FLOW-GEOMETRY-001

Deterministic, dependency-light prototype generator for ORIGIN-001.
This is an artwork-generation scaffold, not a validated archaeological model.
"""

from __future__ import annotations

import math
import random
from pathlib import Path


DEFAULT_SEED = 20260915


def generate_flow_points(
    width: int = 1600,
    height: int = 1600,
    paths: int = 120,
    steps: int = 180,
    step_size: float = 5.0,
    seed: int = DEFAULT_SEED,
):
    """Return deterministic streamline point sequences.

    The field combines a radial component, low-frequency directional variation,
    and bounded seeded perturbation. It is intentionally generic until validated
    research inputs are supplied.
    """
    rng = random.Random(seed)
    cx, cy = width / 2.0, height / 2.0
    output = []

    for _ in range(paths):
        angle = rng.random() * math.tau
        radius = rng.uniform(80.0, min(width, height) * 0.46)
        x = cx + math.cos(angle) * radius
        y = cy + math.sin(angle) * radius
        points = []

        for i in range(steps):
            points.append((x, y))
            dx = x - cx
            dy = y - cy
            r = max(math.hypot(dx, dy), 1.0)

            # Tangential + radial field; coefficients are artistic defaults.
            tx, ty = -dy / r, dx / r
            radial = 0.20 + 0.08 * math.sin(r / 75.0)
            wave = 0.35 * math.sin((x + y) / 180.0)
            jitter = rng.uniform(-0.08, 0.08)

            vx = tx + radial * dx / r + (wave + jitter) * 0.25
            vy = ty + radial * dy / r + (wave + jitter) * 0.25
            norm = max(math.hypot(vx, vy), 1e-9)
            x += step_size * vx / norm
            y += step_size * vy / norm

            if x < 0 or x > width or y < 0 or y > height:
                break

        output.append(points)

    return output


def export_svg(path: str = "artwork/origin-001-prototype.svg", seed: int = DEFAULT_SEED):
    """Export a deterministic vector prototype suitable for later rendering."""
    width = height = 1600
    streams = generate_flow_points(seed=seed)
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#0b1117"/>',
        '<g fill="none" stroke="#b8d8d8" stroke-opacity="0.55" stroke-width="1.2">',
    ]

    for points in streams:
        if len(points) < 2:
            continue
        d = "M " + " ".join(
            f"{x:.2f},{y:.2f}" if j == 0 else f"L {x:.2f},{y:.2f}"
            for j, (x, y) in enumerate(points)
        )
        lines.append(f'<path d="{d}"/>')

    lines.extend(['</g>', '</svg>'])
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    return output


if __name__ == "__main__":
    export_svg()
