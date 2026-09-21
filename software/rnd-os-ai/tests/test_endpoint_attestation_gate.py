import json
from pathlib import Path

def test_endpoint_attestation_contract():
    p = Path("security/BIUPIU-ENDPOINT-ATTESTATION-GATE-v1.0.md")
    assert p.exists()
    text = p.read_text(encoding="utf-8")
    for token in (
        "endpoint_id",
        "scanner_engine",
        "signature_or_rule_version",
        "detection_result",
        "event_ingestion_result",
        "quarantine_or_block_result",
        "recovery_result",
        "audit_event_hash",
        "PENDING",
    ):
        assert token in text

def test_no_synthetic_pass_policy():
    text = Path("security/BIUPIU-ENDPOINT-ATTESTATION-GATE-v1.0.md").read_text(encoding="utf-8")
    assert "No synthetic PASS values are permitted." in text
