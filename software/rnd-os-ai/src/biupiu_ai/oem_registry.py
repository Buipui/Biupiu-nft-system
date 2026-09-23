"""Provider-neutral OEM/runtime compatibility registry.

Entries describe integration boundaries and evidence state; registration never
implies that a physical device or accelerator has been tested.
"""
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class RuntimeBinding:
    family: str
    runtime: str
    interface: str
    platforms: tuple[str, ...]
    acceleration: tuple[str, ...]
    fallback: str
    evidence_status: str = "REGISTERED"


@dataclass
class OEMRegistry:
    _bindings: dict[str, RuntimeBinding]

    def __init__(self) -> None:
        self._bindings = {}

    def register(self, binding: RuntimeBinding) -> None:
        if not binding.family.strip() or not binding.runtime.strip():
            raise ValueError("family and runtime are required")
        key = f"{binding.family}:{binding.runtime}"
        if key in self._bindings:
            raise ValueError(f"binding already registered: {key}")
        self._bindings[key] = binding

    def get(self, family: str, runtime: str) -> RuntimeBinding:
        return self._bindings[f"{family}:{runtime}"]

    def by_family(self, family: str) -> tuple[RuntimeBinding, ...]:
        return tuple(sorted(
            (x for x in self._bindings.values() if x.family == family),
            key=lambda x: x.runtime,
        ))

    def manifest(self) -> tuple[RuntimeBinding, ...]:
        return tuple(sorted(self._bindings.values(), key=lambda x: (x.family, x.runtime)))


def canonical_registry() -> OEMRegistry:
    """Return the current external-harvest compatibility baseline."""
    registry = OEMRegistry()
    entries: Sequence[RuntimeBinding] = (
        RuntimeBinding("Qualcomm", "ONNX Runtime QNN EP", "ExecutionProvider",
                       ("Android", "Windows"), ("NPU", "GPU", "CPU"), "CPU/software"),
        RuntimeBinding("Intel", "ONNX Runtime OpenVINO EP", "ExecutionProvider",
                       ("Windows", "Linux"), ("CPU", "GPU", "NPU"), "CPU"),
        RuntimeBinding("NVIDIA", "ONNX Runtime CUDA EP", "ExecutionProvider",
                       ("Windows", "Linux"), ("GPU",), "CPU"),
        RuntimeBinding("AMD", "ONNX Runtime MIGraphX EP", "ExecutionProvider",
                       ("Windows", "Linux"), ("GPU",), "CPU"),
        RuntimeBinding("Epic", "Unreal NNE", "NNE",
                       ("Windows", "Linux", "Android", "iOS"), ("GPU", "CPU"), "CPU/reference"),
        RuntimeBinding("Khronos", "OpenXR", "XR",
                       ("Windows", "Android", "Linux"), ("GPU",), "non-XR simulation"),
    )
    for entry in entries:
        registry.register(entry)
    return registry
