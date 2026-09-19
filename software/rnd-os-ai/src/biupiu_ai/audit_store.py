from typing import Protocol, Sequence
from .audit_schema import DurableAuditEvent

class AuditStoreError(RuntimeError):
    """Raised when an audit event cannot be durably accepted by a store."""


class AuditStore(Protocol):
    def append(self, event: DurableAuditEvent) -> None: ...
    def append_batch(self, events: Sequence[DurableAuditEvent]) -> None: ...

    def readiness(self) -> bool: ...


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

    def readiness(self) -> bool:
        return True


class FailingAuditStore:
    """Deterministic failure fixture for gateway safety tests."""
    def append(self, event: DurableAuditEvent) -> None:
        raise AuditStoreError("audit-store-unavailable")

    def append_batch(self, events: Sequence[DurableAuditEvent]) -> None:
        raise AuditStoreError("audit-store-unavailable")

    def readiness(self) -> bool:
        return False
