"""Deterministic Federation compatibility and software-family checks."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class SoftwareFamily:
    family_id: str
    languages: Tuple[str, ...]
    runtimes: Tuple[str, ...]
    interfaces: Tuple[str, ...]
    compatible_families: Tuple[str, ...]

SOFTWARE_FAMILIES = (
    SoftwareFamily("python-ml", ("Python",), ("CPython",), ("json", "pytest", "native-learning"),
                   ("typescript-federation", "yaml-orchestration", "cpp-native")),
    SoftwareFamily("typescript-federation", ("TypeScript",), ("Node.js",), ("json", "schema", "federation-contract"),
                   ("python-ml", "yaml-orchestration", "android-kotlin")),
    SoftwareFamily("yaml-orchestration", ("YAML",), ("Digital-Orchestra",), ("workflow", "json", "provenance"),
                   ("python-ml", "typescript-federation")),
    SoftwareFamily("cpp-native", ("C++",), ("native",), ("abi", "cmake", "json", "simulator-contract"),
                   ("python-ml", "android-kotlin")),
    SoftwareFamily("android-kotlin", ("Kotlin",), ("Android",), ("intent", "json", "native-abi", "gradle"),
                   ("typescript-federation", "cpp-native", "python-ml")),
    SoftwareFamily("ue-world", ("C++", "Blueprint"), ("Unreal-Engine",), ("openusd", "json", "twin-state"),
                   ("cpp-native", "python-ml", "typescript-federation")),
)

@dataclass(frozen=True)
class CompatibilityResult:
    source_family: str
    target_family: str
    compatible: bool
    shared_interfaces: Tuple[str, ...]
    reasons: Tuple[str, ...]

def check_family_compatibility(source: str, target: str) -> CompatibilityResult:
    src = next((x for x in SOFTWARE_FAMILIES if x.family_id == source), None)
    dst = next((x for x in SOFTWARE_FAMILIES if x.family_id == target), None)
    if src is None or dst is None:
        return CompatibilityResult(source, target, False, (), ("UNKNOWN_FAMILY",))
    shared = tuple(sorted(set(src.interfaces) & set(dst.interfaces)))
    declared = target in src.compatible_families or source in dst.compatible_families
    compatible = bool(declared and shared)
    reasons = (("DECLARED_FAMILY_COMPATIBILITY",) if declared else ("NO_DECLARED_FAMILY_COMPATIBILITY",)) + (("SHARED_INTERFACE",) if shared else ("NO_SHARED_INTERFACE",))
    return CompatibilityResult(source, target, compatible, shared, reasons)

def federation_compatibility_matrix() -> Tuple[CompatibilityResult, ...]:
    results = []
    for src in SOFTWARE_FAMILIES:
        for dst in SOFTWARE_FAMILIES:
            if src.family_id < dst.family_id:
                results.append(check_family_compatibility(src.family_id, dst.family_id))
    return tuple(results)

def compatible_family_pairs() -> Tuple[Tuple[str, str], ...]:
    return tuple((r.source_family, r.target_family) for r in federation_compatibility_matrix() if r.compatible)
