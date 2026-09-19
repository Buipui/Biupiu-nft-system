"""PHYS-SYS-01 smoke tests for the private R&D physics kernel."""
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("physics_kernel",ROOT/"private-rd-centre/engine/physics_kernel.py")
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

body=m.RigidBody6DoF(10,2,3,4,m.Vec3(0,0,0),m.Vec3(0,0,0),m.Vec3(0,0,0))
body.step(m.Vec3(10,0,0),m.Vec3(2,0,0),1)
assert body.velocity_mps.x == 1.0
assert body.angular_rate_rps.x == 1.0

thermal=m.LumpedThermalModel(300,100,10)
thermal.step(100,300,1)
assert thermal.temperature_k == 301.0

rot=m.RotatingMachine(2)
rot.step(10,2,1)
assert rot.angular_speed_rad_s == 4.0

print("PHYS-SYS-01 smoke tests: PASS")
