from BIUPIU_BLOCKCHAIN_ANCHOR_BOUNDARY import merkle_root,make_anchor_candidate,verify_anchor,promotion_ready

def test_merkle_deterministic():
    assert merkle_root(["a","b"])==merkle_root(["a","b"])
    assert merkle_root(["a","b"])!=merkle_root(["b","a"])

def test_candidate_is_not_live_proof():
    r=make_anchor_candidate("a1",merkle_root(["event1"]),chain_id="candidate-chain",provenance_refs=["event1"])
    assert verify_anchor(r)
    assert not promotion_ready(r)

def test_verified_requires_transaction_and_inclusion():
    r=make_anchor_candidate("a1","root",chain_id="chain",provenance_refs=["e"])
    from dataclasses import replace
    assert not promotion_ready(replace(r,state="VERIFIED"))
    assert promotion_ready(replace(r,state="VERIFIED",transaction_ref="tx:1",inclusion_proof="proof:1"))
