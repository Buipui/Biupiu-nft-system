from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

@dataclass
class ProvenanceEvent:
    object_id: str
    event_type: str
    source_id: Optional[str]
    actor: str
    timestamp: str
    note: str

def make_event(object_id: str, event_type: str, actor: str, note: str, source_id: Optional[str] = None) -> ProvenanceEvent:
    return ProvenanceEvent(object_id, event_type, source_id, actor, datetime.now(timezone.utc).isoformat(), note)
