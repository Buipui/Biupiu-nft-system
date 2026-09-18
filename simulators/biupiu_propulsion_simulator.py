"""Biupiu propulsion concept simulator v0.1.

Educational mean-value model only. Not a controller, safety system, or
substitute for engine dyno, HV validation, CFD, NVH, or vehicle testing.
"""
from dataclasses import dataclass
from math import pi

@dataclass
class Engine:
    peak_kw: float = 210.0
    peak_rpm: float = 4000.0
    drivetrain_eff: float = 0.94
    generator_eff: float = 0.93

@dataclass
class Motor:
    peak_kw: float
    inverter_eff: float = 0.97
    motor_eff: float = 0.94

@dataclass
class Vehicle:
    mass_kg: float = 1450.0
    rolling_coeff: float = 0.012
    drag_coeff: float = 0.30
    frontal_area_m2: float = 1.9
    wheel_radius_m: float = 0.33
    air_density: float = 1.225
    gravity: float = 9.81

class PropulsionSimulator:
    def __init__(self, engine=None, front_motors=None, vehicle=None):
        self.engine = engine or Engine()
        self.front_motors = front_motors or [Motor(75.0), Motor(75.0)]
        self.vehicle = vehicle or Vehicle()

    def engine_power(self, rpm, throttle=1.0):
        # Smooth illustrative torque curve; replace with dyno data later.
        normalized = max(0.0, min(1.0, rpm / self.engine.peak_rpm))
        torque_factor = max(0.35, 1.0 - 0.35 * (normalized - 0.55) ** 2)
        return self.engine.peak_kw * throttle * torque_factor * min(1.0, rpm / 900.0)

    def road_load_kw(self, speed_kph, grade=0.0):
        v = speed_kph / 3.6
        aero = 0.5 * self.vehicle.air_density * self.vehicle.drag_coeff * self.vehicle.frontal_area_m2 * v**3
        rolling = self.vehicle.mass_kg * self.vehicle.gravity * self.vehicle.rolling_coeff * v
        grade_force = self.vehicle.mass_kg * self.vehicle.gravity * grade * v
        return max(0.0, (aero + rolling + grade_force) / 1000.0)

    def run_point(self, rpm, throttle, speed_kph, battery_assist_kw=0.0, grade=0.0):
        engine_kw = self.engine_power(rpm, throttle)
        engine_to_wheels = engine_kw * self.engine.drivetrain_eff
        generator_kw = engine_kw * self.engine.generator_eff
        motor_available = sum(m.peak_kw * m.inverter_eff * m.motor_eff for m in self.front_motors)
        electric_kw = min(max(0.0, battery_assist_kw), motor_available)
        wheel_kw = engine_to_wheels + electric_kw
        road_kw = self.road_load_kw(speed_kph, grade)
        return {
            "engine_kw": round(engine_kw, 2),
            "generator_electrical_kw": round(generator_kw, 2),
            "front_motor_wheel_kw": round(electric_kw, 2),
            "wheel_power_kw": round(wheel_kw, 2),
            "road_load_kw": round(road_kw, 2),
            "net_acceleration_power_kw": round(wheel_kw - road_kw, 2),
            "nominal_peak_combined_kw": round(engine_to_wheels + motor_available, 2),
        }

if __name__ == "__main__":
    sim = PropulsionSimulator()
    for rpm, speed in [(900, 0), (2000, 60), (3000, 120), (4000, 200)]:
        print(sim.run_point(rpm, 1.0, speed, battery_assist_kw=150.0))
