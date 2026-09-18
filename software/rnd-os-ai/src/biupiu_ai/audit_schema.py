from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class DurableAuditEvent:
    schema_version: str
    request_id: str
    event: str
    outcome: str
    client_key: str
    error_code: Optional[str] = None

    def to_record(self) -> dict:
        return {
            "schema_version": self.schema_version,
            "request_id": self.request_id,
            "event": self.event,
            "outcome": self.outcome,
            "client_key": self.client_key,
            "error_code": self.error_code,
        }
