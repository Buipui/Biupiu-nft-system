from biupiu_ai.global_module_harvester import harvest_plan, eligible_for_first_party_implementation

def test_harvest_plan_has_core_families():
    families={x.family for x in harvest_plan()}
    assert {"open-data-api","OCR","geospatial","signal-processing","patent-prior-art","OEM-public-SDK"} <= families

def test_candidates_require_acceptance():
    assert all(eligible_for_first_party_implementation(x) for x in harvest_plan())
