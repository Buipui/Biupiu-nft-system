import importlib.util
from dataclasses import replace
from pathlib import Path

SPEC=importlib.util.spec_from_file_location("anchor",Path(__file__).with_name("BIUPIU-BLOCKCHAIN-ANCHOR-BOUNDARY.py"))
anchor=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(anchor)

def test_merkle_deterministic():
    assert anchor.merkle_root(["a","b"])==anchor.merkle_root(["a","b"])
    assert anchor.merkle_root(["a","b"])!=anchor.merkle_root(["b","a"])

def test_candidate_is_not_live_proof():
    r=anchor.make_anchor_candidate("a1",anchor.merkle_root(["event1"]),chain_id="candidate-chain",provenance_refs=["event1"])
    assert anchor.verify_anchor(r)
    assert not anchor.promotion_ready(r)

def test_verified_requires_transaction_and_inclusion():
    r=anchor.make_anchor_candidate("a1","root",chain_id="chain",provenance_refs=["e"])
    assert not anchor.promotion_ready(replace(r,state="VERIFIED"))
    assert anchor.promotion_ready(replace(r,state="VERIFIED",transaction_ref="tx:1",inclusion_proof="proof:1"))
