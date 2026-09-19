from biupiu_ai.audit_outbox import AuditOutbox, OutboxItem
from biupiu_ai.audit_schema import DurableAuditEvent
from biupiu_ai.audit_store import FailingAuditStore, InMemoryAuditStore, AuditStoreError

def event(i):
    return DurableAuditEvent("1.0", i, "gateway.accepted", "success", "client")

def test_ai24_deduplicates_and_flushes():
    store = InMemoryAuditStore()
    outbox = AuditOutbox(store)
    item = OutboxItem("e1", event("r1"))
    outbox.enqueue(item)
    outbox.enqueue(item)
    assert outbox.flush_one() is True
    assert len(store.snapshot()) == 1

def test_ai24_retries_without_silent_loss():
    outbox = AuditOutbox(FailingAuditStore(), max_attempts=2)
    outbox.enqueue(OutboxItem("e2", event("r2")))
    assert outbox.flush_one() is False
    try:
        outbox.flush_one()
        assert False
    except AuditStoreError:
        assert len(outbox.pending()) == 1
