from dataclasses import dataclass
from .audit_schema import DurableAuditEvent
from .audit_store import AuditStore, AuditStoreError

@dataclass(frozen=True)
class OutboxItem:
    event_id: str
    event: DurableAuditEvent
    attempts: int = 0

class AuditOutbox:
    """Deterministic outbox boundary with bounded retry and no silent loss."""
    def __init__(self, store: AuditStore, max_attempts: int = 3):
        self.store = store
        self.max_attempts = max_attempts
        self._pending: list[OutboxItem] = []

    def enqueue(self, item: OutboxItem) -> None:
        if any(existing.event_id == item.event_id for existing in self._pending):
            return
        self._pending.append(item)

    def flush_one(self) -> bool:
        if not self._pending:
            return True
        item = self._pending[0]
        try:
            self.store.append(item.event)
        except AuditStoreError:
            if item.attempts + 1 >= self.max_attempts:
                raise
            self._pending[0] = OutboxItem(item.event_id, item.event, item.attempts + 1)
            return False
        self._pending.pop(0)
        return True

    def pending(self) -> tuple[OutboxItem, ...]:
        return tuple(self._pending)
