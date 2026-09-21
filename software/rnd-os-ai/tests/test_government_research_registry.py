from biupiu_ai.government_research_registry import (
    PUBLIC_RESEARCH_SOURCES,
    executable_sources,
    source_ids,
    sources_by_institution,
)


def test_public_sources_are_registered():
    ids = source_ids()
    assert "nasa-fprime" in ids
    assert "nasa-gmat" in ids
    assert "nasa-osal" in ids
    assert "darpa-tractor" in ids
    assert "darpa-expmath" in ids
    assert "darpa-dial" in ids
    assert "mit-drake" in ids
    assert "dhs-public-ai-research" in ids


def test_sources_are_fail_closed():
    assert PUBLIC_RESEARCH_SOURCES
    assert executable_sources() == ()


def test_institution_filter_is_deterministic():
    assert len(sources_by_institution("NASA")) >= 4
    assert len(sources_by_institution("DARPA")) >= 3
    assert len(sources_by_institution("MIT")) == 1
    assert len(sources_by_institution("U.S. Department of Homeland Security")) == 1
