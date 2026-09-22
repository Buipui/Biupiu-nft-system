"""Safe provider-neutral adapters for validated simulation backends.

Adapters probe local executables and construct argument-safe commands.
They never install, vendor, or execute third-party backends automatically.
"""

from dataclasses import dataclass
from shutil import which
from typing import Optional, Tuple


@dataclass(frozen=True)
class AdapterResult:
    backend: str
    available: bool
    executable: Optional[str]
    command: Tuple[str, ...]
    status: str


class SimulatorAdapter:
    def __init__(self, backend: str, executable: str):
        if not backend or not executable:
            raise ValueError("backend and executable are required")
        self.backend, self.executable = backend, executable

    def probe(self) -> AdapterResult:
        path = which(self.executable)
        return AdapterResult(
            self.backend,
            path is not None,
            path,
            (path,) if path else (),
            "ready" if path else "not-installed",
        )

    def command(self, *args: str) -> Tuple[str, ...]:
        if any(not isinstance(a, str) for a in args):
            raise TypeError("adapter arguments must be strings")
        if any("\x00" in a for a in args):
            raise ValueError("NUL bytes are not permitted")
        path = which(self.executable)
        if path is None:
            raise RuntimeError(f"{self.backend} executable is not installed")
        return (path, *args)


GAZEBO = SimulatorAdapter("Gazebo", "gz")
CHRONO = SimulatorAdapter("Project Chrono", "chrono")
OPENSTUDIO = SimulatorAdapter("OpenStudio", "openstudio")
ENERGYPLUS = SimulatorAdapter("EnergyPlus", "energyplus")
OPENSIM = SimulatorAdapter("OpenSim", "opensim")


def backend_matrix() -> dict[str, AdapterResult]:
    """Return non-executing availability probes for registered simulator backends."""
    return {
        "gazebo": GAZEBO.probe(),
        "chrono": CHRONO.probe(),
        "openstudio": OPENSTUDIO.probe(),
        "energyplus": ENERGYPLUS.probe(),
        "opensim": OPENSIM.probe(),
    }
