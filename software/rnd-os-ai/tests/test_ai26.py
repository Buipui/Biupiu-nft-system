from biupiu_ai.audit_schema import DurableAuditEvent
from biupiu_ai.open_resource_registry import OPEN_RESOURCES
from biupiu_ai.transactional_audit import TransactionalAuditBoundary, validate_resource_provenance
from biupiu_ai.audit_store import InMemoryAuditStore

class Registry:
    @staticmethod
    def get_resource(resource_id):
        return next((r for r in OPEN_RESOURCES if r.resource_id == resource_id), None)

def test_ai26_provenance_accepts_registered_resource():
    assert validate_resource_provenance(["NASA-FPRIME"], Registry()).accepted

def test_ai26_provenance_rejects_unknown_resource():
    assert not validate_resource_provenance(["UNKNOWN"], Registry()).accepted

def test_ai26_transactional_audit_boundary_deduplicates_request_event():
    boundary = TransactionalAuditBoundary(InMemoryAuditStore())
    event = DurableAuditEvent("1.0", "req-26", "gateway.accepted", "success", "client")
    assert boundary.submit(event) is True
    assert boundary.submit(event) is False
    assert boundary.flush_one() is True
    assert boundary.pending() == ()
