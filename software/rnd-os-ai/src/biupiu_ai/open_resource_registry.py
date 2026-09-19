from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class OpenResource:
    resource_id: str
    name: str
    source: str
    license: str
    roles: Tuple[str, ...]
    integration_mode: str


OPEN_RESOURCES = (
    OpenResource("NASA-FPRIME", "F Prime", "https://github.com/nasa/fprime", "Apache-2.0",
                 ("flight-software", "embedded", "component-architecture", "testing"), "external-reference"),
    OpenResource("NASA-CFS", "Core Flight System", "https://github.com/nasa/cFS", "Apache-2.0",
                 ("flight-software", "telemetry", "embedded"), "external-reference"),
    OpenResource("MIT-MULTICOPTER", "Computational Multicopter Design", "https://github.com/mit-gfx/multicopter_design", "GPL-2.0",
                 ("aero", "multicopter", "geometry", "simulation"), "external-reference"),
    OpenResource("MIT-DRL", "MIT Distributed Robotics Laboratory", "https://github.com/mit-drl", "varies-by-repository",
                 ("robotics", "optimization", "research"), "repository-by-repository-review"),
    OpenResource("WISP-SCIENCE", "Wisp Science", "https://github.com/xuzhougeng/wisp-science", "AGPL-3.0-only",
                 ("scientific-ai", "reproducible-research", "MCP", "data"), "external-reference"),
    OpenResource("OPENARM", "OpenArm", "https://github.com/enactic/OpenArm", "mixed-by-repository",
                 ("robotics", "physical-ai", "ROS2", "hardware"), "repository-by-repository-review"),
    OpenResource("URLAB", "Unreal Robotics Lab", "https://github.com/URLab-Sim/UnrealRoboticsLab", "Apache-2.0",
                 ("robotics", "unreal", "mujoco", "simulation"), "external-reference"),
    OpenResource("GENESIS", "Genesis World", "https://github.com/Genesis-Embodied-AI/genesis-world", "Apache-2.0",
                 ("robotics", "physics", "simulation", "embodied-ai"), "external-reference"),
    OpenResource("WEBOTS", "Webots", "https://github.com/cyberbotics/webots", "Apache-2.0",
                 ("robotics", "simulation", "ROS2", "digital-twin"), "external-reference"),
    OpenResource("IR-SIM", "IR-SIM", "https://github.com/hanruihua/ir-sim", "MIT",
                 ("robotics", "navigation", "control", "learning"), "external-reference"),
)


def get_resource(resource_id: str) -> OpenResource | None:
    return next((r for r in OPEN_RESOURCES if r.resource_id == resource_id), None)
