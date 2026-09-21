"""Repository-first background learning loop for Biupiu AI OS."""
from __future__ import annotations
import hashlib, json, time
from pathlib import Path
from typing import Any, Callable, Dict

class LearningDaemon:
    def __init__(self, observation_source: Callable[[], Dict[str, Any]],
                 evaluator: Callable[[Dict[str, Any]], Dict[str, Any]],
                 store: Path) -> None:
        self.observation_source = observation_source
        self.evaluator = evaluator
        self.store = store
        self.store.mkdir(parents=True, exist_ok=True)

    def cycle(self) -> Dict[str, Any]:
        observation = self.observation_source()
        evaluation = self.evaluator(observation)
        record = {
            "schema": "biupiu.learning.event.v1",
            "timestamp": time.time(),
            "observation": observation,
            "evaluation": evaluation,
            "promotion": "manual_or_policy_gate_required"
        }
        canonical = json.dumps(record, sort_keys=True, separators=(",", ":"))
        record["event_hash"] = hashlib.sha256(canonical.encode()).hexdigest()
        target = self.store / f"{int(record['timestamp'] * 1000)}.json"
        target.write_text(json.dumps(record, indent=2), encoding="utf-8")
        return record
