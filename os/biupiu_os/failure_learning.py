import hashlib
import json
from dataclasses import asdict, dataclass


@dataclass
class FailureRecord:
    execution_id: str
    module: str
    category: str
    signature: str
    issues: list[str]
    inputs_digest: str


class FailureLearningStore:
    """In-memory failure evidence store; it does not alter scientific models."""

    def __init__(self):
        self.records: list[FailureRecord] = []

    @staticmethod
    def _digest(inputs):
        payload = json.dumps(inputs, sort_keys=True, default=str, separators=(",", ":"))
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    @staticmethod
    def _category(status, warnings):
        text = " ".join(warnings).upper()
        if status == "physics_failed" or "PHYSICS_CHECK:" in text:
            return "physics"
        if status == "failed" and "EXECUTION_ERROR:" in text:
            return "execution"
        if "INPUT" in text or "SCHEMA" in text:
            return "input"
        return "unknown"

    def record(self, execution_id, module, status, warnings, inputs):
        if status == "completed":
            return None
        issues = sorted(set(str(item) for item in warnings)) or [status]
        category = self._category(status, issues)
        signature_payload = "|".join([module, category, *issues])
        signature = hashlib.sha256(signature_payload.encode("utf-8")).hexdigest()[:16]
        item = FailureRecord(execution_id, module, category, signature, issues, self._digest(inputs))
        self.records.append(item)
        return item

    def recurring(self, min_count=2):
        counts = {}
        for item in self.records:
            counts[item.signature] = counts.get(item.signature, 0) + 1
        return [item for item in self.records if counts[item.signature] >= min_count]

    def summary(self):
        signatures = {item.signature for item in self.records}
        recurring_signatures = {item.signature for item in self.recurring()}
        return {
            "total_failures": len(self.records),
            "unique_signatures": len(signatures),
            "recurring_signatures": len(recurring_signatures),
        }

    def to_dicts(self):
        return [asdict(item) for item in self.records]
