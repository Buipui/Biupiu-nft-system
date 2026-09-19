from biupiu_ai.audit_store import AuditStoreError, FailingAuditStore, InMemoryAuditStore

def test_ai22_ready_store_reports_ready():
    assert InMemoryAuditStore().readiness() is True

def test_ai22_failed_store_reports_not_ready():
    store = FailingAuditStore()
    assert store.readiness() is False
    try:
        store.append(None)
        assert False
    except AuditStoreError:
        assert True

def test_ai22_failure_is_explicit():
    store = FailingAuditStore()
    try:
        store.append(None)
        assert False
    except AuditStoreError as exc:
        assert str(exc) == "audit-store-unavailable"
