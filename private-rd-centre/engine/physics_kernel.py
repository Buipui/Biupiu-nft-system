"""Biupiu private R&D physics kernel v1.0.
Small dependency-free numerical core for early digital-twin experiments.
Not a certified engineering solver.
"""
from dataclasses import dataclass
from math import isfinite

def _finite(value: float) -> float:
    value = float(value)
    if not isfinite(value):
        raise ValueError('non-finite numeric input')
    return value

@dataclass
class Vec3:
    x: float
    y: float
    z: float
    def __post_init__(self):
        self.x, self.y, self.z = map(_finite, (self.x, self.y, self.z))
    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __mul__(self, scalar):
        scalar = _finite(scalar)
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

@dataclass
class RigidBody6DoF:
    mass_kg: float
    inertia_x: float
    inertia_y: float
    inertia_z: float
    position_m: Vec3
    velocity_mps: Vec3
    angular_rate_rps: Vec3
    def __post_init__(self):
        for name in ('mass_kg', 'inertia_x', 'inertia_y', 'inertia_z'):
            value = _finite(getattr(self, name))
            if value <= 0:
                raise ValueError(f'{name} must be > 0')
            setattr(self, name, value)
    def step(self, force_n: Vec3, moment_nm: Vec3, dt_s: float):
        dt_s = _finite(dt_s)
        if dt_s <= 0:
            raise ValueError('dt_s must be > 0')
        acceleration = force_n * (1.0 / self.mass_kg)
        self.position_m = self.position_m + self.velocity_mps * dt_s
        self.velocity_mps = self.velocity_mps + acceleration * dt_s
        angular_accel = Vec3(moment_nm.x / self.inertia_x, moment_nm.y / self.inertia_y, moment_nm.z / self.inertia_z)
        self.angular_rate_rps = self.angular_rate_rps + angular_accel * dt_s

@dataclass
class LumpedThermalModel:
    temperature_k: float
    heat_capacity_j_per_k: float
    conductance_w_per_k: float
    def step(self, heat_input_w: float, ambient_k: float, dt_s: float):
        for value in (heat_input_w, ambient_k, dt_s):
            _finite(value)
        if self.heat_capacity_j_per_k <= 0 or self.conductance_w_per_k < 0:
            raise ValueError('invalid thermal parameters')
        if dt_s <= 0:
            raise ValueError('dt_s must be > 0')
        dtemp_dt = (heat_input_w - self.conductance_w_per_k * (self.temperature_k - ambient_k)) / self.heat_capacity_j_per_k
        self.temperature_k += dtemp_dt * dt_s

@dataclass
class RotatingMachine:
    inertia_kg_m2: float
    angular_speed_rad_s: float = 0.0
    def __post_init__(self):
        self.inertia_kg_m2 = _finite(self.inertia_kg_m2)
        if self.inertia_kg_m2 <= 0:
            raise ValueError('inertia_kg_m2 must be > 0')
    def step(self, drive_torque_nm: float, load_torque_nm: float, dt_s: float):
        drive_torque_nm = _finite(drive_torque_nm)
        load_torque_nm = _finite(load_torque_nm)
        dt_s = _finite(dt_s)
        if dt_s <= 0:
            raise ValueError('dt_s must be > 0')
        angular_accel = (drive_torque_nm - load_torque_nm) / self.inertia_kg_m2
        self.angular_speed_rad_s = max(0.0, self.angular_speed_rad_s + angular_accel * dt_s)
