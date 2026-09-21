"""Biupiu default resource-learning logger.

Pure standard-library reference implementation. It records hashes/metadata, never raw secrets,
and deliberately separates discovery from validation/promotion.
"""
from dataclasses import dataclass, asdict
from hashlib import sha256
import json
from pathlib import Path
from time import time

@dataclass
class LearningEvent:
    sequence: int
    direction: str
    event_type: str
    source_ref: str
    content_hash: str
    model_version: str
    evidence_state: str
    validation_status: str
    confidence: float

def digest(value: str) -> str:
    return sha256(value.encode("utf-8")).hexdigest()

class ResourceLearningAgent:
    def __init__(self, log_path="intelligence/learning-events.jsonl"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        self.sequence = 0

    def record(self, direction, event_type, source_ref, content,
               model_version="unknown", evidence_state="discovered",
               validation_status="pending", confidence=0.0):
        self.sequence += 1
        e = LearningEvent(self.sequence, direction, event_type, source_ref,
                          digest(content), model_version, evidence_state,
                          validation_status, float(confidence))
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(e), sort_keys=True) + "\n")
        return e
