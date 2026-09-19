from typing import Protocol, Sequence
from .audit_schema import DurableAuditEvent

class AuditStore(Protocol):
    def append(self, event: DurableAuditEvent) -> None: ...
    def append_batch(self, events: Sequence[DurableAuditEvent]) -> None: ...

class InMemoryAuditStore:
    """Transactional test store; production adapters can implement the same contract."""
    def __init__(self):
        self._records: list[dict] = []

    def append(self, event: DurableAuditEvent) -> None:
        self._records.append(event.to_record())

    def append_batch(self, events: Sequence[DurableAuditEvent]) -> None:
        pending = [event.to_record() for event in events]
        self._records.extend(pending)

    def snapshot(self) -> tuple[dict, ...]:
        return tuple(self._records)
