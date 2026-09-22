from software.digital_orchestra.orchestra import DigitalOrchestra, Evidence, WorkItem, Provenance, WorkState

def test_governed_harvest_lifecycle():
    o=DigitalOrchestra()
    item=WorkItem(
        title="foreign workflow pattern",
        capability="orchestration",
        evidence=Evidence.PRELIMINARY,
        provenance=Provenance(
            source_uri="https://example.org/source",
            source_kind="EXTERNAL_REPOSITORY",
            language="ja",
            licence="REFERENCE_ONLY",
        ),
    )
    cid=o.register(item)
    o.route(cid, ["classify","compare","verify"])
    o.observe(cid, {"result":"pattern extracted"})
    o.verify(cid, True, Evidence.SUPPORTED)
    o.digest_and_file(cid, "research/harvest/orchestration.md")
    assert o.items[cid].state == WorkState.FILED
    assert len(o.events) >= 4
