from dataclasses import dataclass
from typing import Optional
from .audit_schema import DurableAuditEvent
from .audit_outbox import AuditOutbox, OutboxItem
from .audit_store import AuditStore

@dataclass(frozen=True)
class ProvenanceDecision:
    accepted: bool
    reason: str

def validate_resource_provenance(resource_ids, registry) -> ProvenanceDecision:
    for resource_id in resource_ids or []:
        resource = registry.get_resource(resource_id)
        if resource is None:
            return ProvenanceDecision(False, "unknown-resource")
        if not resource.source or not resource.license:
            return ProvenanceDecision(False, "incomplete-resource-provenance")
    return ProvenanceDecision(True, "provenance-valid")

class TransactionalAuditBoundary:
    """Queues audit events before delivery and exposes explicit delivery status."""
    def __init__(self, store: AuditStore, max_attempts: int = 3):
        self.outbox = AuditOutbox(store, max_attempts)

    def submit(self, event: DurableAuditEvent) -> bool:
        return self.outbox.enqueue(OutboxItem(event.request_id, event))

    def flush_one(self) -> bool:
        return self.outbox.flush_one()

    def pending(self):
        return self.outbox.pending()
