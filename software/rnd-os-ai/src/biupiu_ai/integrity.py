import hashlib

def content_hash(payload: str) -> str:
    """Return a deterministic SHA-256 integrity hash for a dataset payload."""
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
