"""Safe provider-neutral adapters for validated simulation backends."""
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
        self.backend, self.executable = backend, executable

    def probe(self) -> AdapterResult:
        path = which(self.executable)
        return AdapterResult(self.backend, path is not None, path,
                             (path,) if path else (),
                             "ready" if path else "not-installed")

    def command(self, *args: str) -> Tuple[str, ...]:
        if any("\x00" in a for a in args):
            raise ValueError("NUL bytes are not permitted")
        path = which(self.executable)
        if path is None:
            raise RuntimeError(f"{self.backend} executable is not installed")
        return (path, *args)

GAZEBO = SimulatorAdapter("Gazebo", "gz")
PYTHON = SimulatorAdapter("Python", "python")

def backend_matrix() -> dict[str, AdapterResult]:
    return {"gazebo": GAZEBO.probe(), "python": PYTHON.probe()}
