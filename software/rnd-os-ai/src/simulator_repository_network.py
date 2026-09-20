"""Biupiu Intelligence Network: validated simulator/graphics repository registry.

Discovery entries remain external references until licence, security, compatibility,
and technical validation gates approve incorporation. This module is deliberately
provider-neutral and does not execute external code.
"""
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class RepositoryResource:
    name: str
    url: str
    domains: Tuple[str, ...]
    source_language: str
    status: str = "discovered-reference"

RESOURCES = (
    RepositoryResource("Gazebo", "https://github.com/gazebosim/gz-sim", ("robotics","simulation","physics"), "multilingual"),
    RepositoryResource("ROS-Gazebo bridge", "https://github.com/gazebosim/ros_gz", ("robotics","ros2","simulation"), "multilingual"),
    RepositoryResource("DISCOVERSE", "https://github.com/DISCOVERSE/DISCOVERSE", ("robotics","mujoco","real2sim2real"), "Chinese/Japanese"),
    RepositoryResource("GaussianRenderer", "https://github.com/discoverse-dev/GaussianRenderer", ("graphics","3dgs","mujoco"), "Chinese/Japanese"),
    RepositoryResource("GS-Real2Sim", "https://github.com/discoverse-dev/gs-real2sim", ("3dgs","digital-twin","mujoco"), "Chinese/Japanese"),
    RepositoryResource("DLR OAISYS", "https://github.com/DLR-RM/oaisys", ("outdoor-simulation","blender","planetary-robotics"), "German"),
    RepositoryResource("rbot", "https://github.com/rlxai/rbot", ("amr","ros2","gazebo","navigation"), "multilingual"),
    RepositoryResource("Unity EntityComponentSystemSamples", "https://github.com/Unity-Technologies/EntityComponentSystemSamples", ("unity6","ecs","physics","graphics","netcode"), "C#"),
    RepositoryResource("Unity Robotics Hub", "https://github.com/Unity-Technologies/Unity-Robotics-Hub", ("unity6","robotics","ros2","urdf","simulation"), "C#"),
    RepositoryResource("Unity UI Toolkit examples", "https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples", ("unity6","graphics","hmi","ui"), "C#"),
    RepositoryResource("Unity DesktopSamples", "https://github.com/Unity-Technologies/DesktopSamples", ("unity6","desktop","integration"), "C#"),
)

SEARCH_PROTOCOLS = (
    "German",
    "Japanese",
    "Chinese",
    "South Korean",
    "Russian",
)

ROUTING = {
    "robotics": ("ROB-01", "DIGITAL-TWIN", "AI-TRAINING"),
    "simulation": ("SIM-CORE", "DIGITAL-TWIN", "VALIDATION"),
    "graphics": ("GRAPHICS", "COMPUTATIONAL-GEOMETRY"),
    "3dgs": ("COMPUTATIONAL-VISION", "DIGITAL-TWIN"),
    "aerospace": ("AEROSPACE", "VIRTUAL-HANGAR"),
    "unity6": ("WORLD", "GRAPHICS", "HMI", "DIGITAL-TWIN"),
}

def search_candidates(domain: str) -> list[RepositoryResource]:
    return [r for r in RESOURCES if domain in r.domains]

def validation_required(resource: RepositoryResource) -> bool:
    return resource.status != "validated-incorporated"
