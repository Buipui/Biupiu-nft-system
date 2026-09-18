from dataclasses import dataclass

@dataclass
class SyncEnvelope:
    item_id: str
    item_type: str
    payload: str
    client_version: int

def validate_envelope(envelope: SyncEnvelope) -> list[str]:
    errors = []
    if not envelope.item_id: errors.append("item_id is required")
    if not envelope.item_type: errors.append("item_type is required")
    if not envelope.payload: errors.append("payload is required")
    if envelope.client_version < 1: errors.append("client_version must be >= 1")
    return errors
