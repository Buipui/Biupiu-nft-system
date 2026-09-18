from biupiu_ai.sync import SyncEnvelope, validate_envelope

def test_sync_envelope():
    assert validate_envelope(SyncEnvelope("x", "experiment", "{}", 1)) == []

def test_invalid_sync_envelope():
    errors = validate_envelope(SyncEnvelope("", "", "", 0))
    assert "item_id is required" in errors
    assert "client_version must be >= 1" in errors
