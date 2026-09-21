"""Biupiu native-system execution harness."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from hashlib import sha256
import json
from typing import Any, Iterable, Mapping

@dataclass(frozen=True)
class HarvestCandidate:
    path: str
    role: str
    status: str = "candidate"
    licence_review: str = "required"
    runtime_verified: bool = False
    def id(self) -> str:
        return sha256(self.path.encode("utf-8")).hexdigest()[:16]

@dataclass(frozen=True)
class ExecutionEvent:
    event_type: str
    target: str
    status: str
    payload: Mapping[str, Any]
    def digest(self) -> str:
        body = json.dumps(asdict(self), sort_keys=True, separators=(",", ":"))
        return sha256(body.encode("utf-8")).hexdigest()

class NativeSystemHarness:
    """Deterministic composition layer for Biupiu OS + AI + simulators."""
    def __init__(self) -> None:
        self.harvest: dict[str, HarvestCandidate] = {}
        self.events: list[ExecutionEvent] = []

    def harvest_resources(self, candidates: Iterable[HarvestCandidate]) -> list[str]:
        added = []
        for candidate in candidates:
            key = candidate.id()
            if key not in self.harvest:
                self.harvest[key] = candidate
                added.append(key)
        return added

    def record(self, event_type: str, target: str, status: str, **payload: Any) -> str:
        event = ExecutionEvent(event_type, target, status, payload)
        self.events.append(event)
        return event.digest()

    def release_ready(self, *, tests_passed: bool, provenance_verified: bool,
                      human_approved: bool) -> bool:
        return tests_passed and provenance_verified and human_approved

    def snapshot(self) -> dict[str, Any]:
        return {
            "harvest_count": len(self.harvest),
            "event_count": len(self.events),
            "harvest": [asdict(x) for x in self.harvest.values()],
            "events": [asdict(x) | {"digest": x.digest()} for x in self.events],
        }

CANONICAL_HARVEST = (
    HarvestCandidate("core/multilang/", "core ABI / Rust / C++ boundary"),
    HarvestCandidate("apps/shared/runtime/", "department runtime / service gateway"),
    HarvestCandidate("software/rnd-os-ai/src/biupiu_ai/native_runtime.py", "AI native runtime"),
    HarvestCandidate("software/rnd-os-ai/src/biupiu_ai/learning.py", "governed learning"),
    HarvestCandidate("software/rnd-os-ai/src/biupiu_ai/ml/engine.py", "ML task routing"),
    HarvestCandidate("software/rnd-os-ai/src/biupiu_ai/learning_daemon.py", "background learning loop"),
    HarvestCandidate("intelligence/BIUPIU-OS-RESOURCE-CONSOLIDATION-SMOKE.py", "resource consolidation smoke test"),
    HarvestCandidate("research/BIUPIU-OS-SIMULATOR-KERNEL-v1.0.md", "simulator kernel contract"),
    HarvestCandidate("research/BIUPIU-AUTONOMOUS-AI-RESOURCE-UPDATE-2026-09-21.md", "autonomous AI resource candidates"),
)

def build_initial_harness() -> NativeSystemHarness:
    harness = NativeSystemHarness()
    harness.harvest_resources(CANONICAL_HARVEST)
    harness.record("HARVEST", "native-core", "accepted", rule="metadata-first",
                   promotion="licence+security+compatibility+tests")
    harness.record("BIND", "os-ai-boundary", "accepted", authority="OS",
                   ai_mode="propose/simulate/learn")
    harness.record("BIND", "simulator-kernel", "accepted",
                   flow="CREATE->LOAD->REGISTER->RUN->EVENT->MEASURE->VALIDATE->PROVENANCE->REPLAY->RELEASE")
    return harness
