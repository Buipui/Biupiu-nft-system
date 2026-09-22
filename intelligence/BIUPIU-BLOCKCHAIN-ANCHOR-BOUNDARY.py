"""Deterministic blockchain-anchor boundary for Biupiu provenance checkpoints.

This module creates and verifies anchor records; it does not hold keys, submit
transactions, or claim on-chain finality. Payloads stay off-chain by default.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
import hashlib, json
from typing import Mapping, Sequence

ANCHOR_STATES={"CANDIDATE","SUBMITTED","INCLUDED","VERIFIED","REJECTED","QUARANTINED"}

def canonical_hash(value: object) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def merkle_root(items: Sequence[str]) -> str:
    layer=[canonical_hash(x) for x in items]
    if not layer: return canonical_hash("")
    while len(layer)>1:
        if len(layer)%2: layer.append(layer[-1])
        layer=[canonical_hash(layer[i]+layer[i+1]) for i in range(0,len(layer),2)]
    return layer[0]

@dataclass(frozen=True)
class AnchorRecord:
    anchor_id:str
    checkpoint_root:str
    chain_id:str
    transaction_ref:str|None
    inclusion_proof:str|None
    state:str
    payload_policy:str
    provenance_refs:tuple[str,...]

def make_anchor_candidate(anchor_id:str, checkpoint_root:str, *, chain_id:str,
                          provenance_refs:Sequence[str]) -> AnchorRecord:
    if not anchor_id.strip() or not checkpoint_root.strip() or not chain_id.strip():
        raise ValueError("anchor identity, checkpoint root and chain id are required")
    if not provenance_refs: raise ValueError("provenance_refs are required")
    return AnchorRecord(anchor_id,checkpoint_root,chain_id,None,None,"CANDIDATE","OFF_CHAIN_ROOT_ONLY",tuple(provenance_refs))

def verify_anchor(record: AnchorRecord) -> bool:
    if record.state=="VERIFIED":
        return bool(record.transaction_ref and record.inclusion_proof and record.provenance_refs)
    return record.state in {"CANDIDATE","SUBMITTED","INCLUDED","REJECTED","QUARANTINED"} and bool(record.checkpoint_root and record.provenance_refs)

def promotion_ready(record: AnchorRecord) -> bool:
    return record.state=="VERIFIED" and bool(record.transaction_ref and record.inclusion_proof)
