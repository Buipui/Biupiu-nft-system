"""Deterministic algorithm-to-blockchain commitment bridge."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from hashlib import sha256
from typing import Mapping, Any
import json

@dataclass(frozen=True)
class AlgorithmCommitment:
    algorithm_id: str
    version: str
    code_digest: str
    evidence_digest: str
    metadata_digest: str
    commitment: str

def digest(value: Any) -> str:
    return sha256(json.dumps(value, sort_keys=True, default=str).encode()).hexdigest()

def create_commitment(algorithm_id: str, version: str, *, code: str,
                      evidence: Mapping[str, Any], metadata: Mapping[str, Any]) -> AlgorithmCommitment:
    code_digest, evidence_digest, metadata_digest = digest(code), digest(evidence), digest(metadata)
    commitment = digest({"algorithm_id": algorithm_id, "version": version,
                         "code_digest": code_digest, "evidence_digest": evidence_digest,
                         "metadata_digest": metadata_digest})
    return AlgorithmCommitment(algorithm_id, version, code_digest, evidence_digest,
                               metadata_digest, commitment)

def release_record(commitment: AlgorithmCommitment, *, network: str = "UNDEPLOYED") -> dict[str, Any]:
    return {"schema": "biupiu.algorithm.release.v1", "network": network,
            "status": "OFFCHAIN_COMMITMENT", **asdict(commitment),
            "promotion_rule": "verified-evidence + licence + security + regression + human/release authority"}
