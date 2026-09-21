from biupiu_ai.public_research_protocol import (
    PUBLIC_RESEARCH_FEEDS, discoverable_module_families, executable_feeds, validate_feed
)

def test_public_feeds_are_registered():
    ids = {f.feed_id for f in PUBLIC_RESEARCH_FEEDS}
    assert {"cia-foia-reading-room","nsa-declassification","uspto-patent-public-search"} <= ids

def test_candidate_modules_are_discoverable():
    modules = discoverable_module_families()
    assert "ocr" in modules
    assert "cryptography" in modules
    assert "prior-art" in modules

def test_executable_promotion_is_fail_closed():
    assert executable_feeds() == ()
    assert all(validate_feed(f) for f in PUBLIC_RESEARCH_FEEDS)
