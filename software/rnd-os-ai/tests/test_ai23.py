from biupiu_ai.open_resource_registry import OPEN_RESOURCES, get_resource

def test_ai23_resource_registry_has_nasa_and_mit():
    ids = {r.resource_id for r in OPEN_RESOURCES}
    assert "NASA-FPRIME" in ids
    assert "NASA-CFS" in ids
    assert "MIT-MULTICOPTER" in ids

def test_ai23_resource_lookup():
    resource = get_resource("WISP-SCIENCE")
    assert resource is not None
    assert resource.license == "AGPL-3.0-only"
