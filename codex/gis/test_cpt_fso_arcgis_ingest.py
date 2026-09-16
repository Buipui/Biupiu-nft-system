from cpt_fso_arcgis_ingest import feature_to_node, ingest_features


def test_public_feature_becomes_candidate_node():
    feature = {
        "attributes": {"OBJECTID": 42, "BLDG_USG": "LIBRARY", "SBRB": "TEST", "NAME": "Example"},
        "geometry": {"x": 18.5, "y": -33.95},
    }
    node = feature_to_node(feature, "CCT_BUILDINGS")
    assert node is not None
    assert node["node_id"] == "CCT-CCT_BUILDINGS-42"
    assert node["permission_status"] == "unknown"
    assert node["los_status"] == "unresolved"


def test_private_or_unknown_usage_is_not_promoted():
    feature = {
        "attributes": {"OBJECTID": 7, "BLDG_USG": "RESIDENTIAL"},
        "geometry": {"x": 18.5, "y": -33.95},
    }
    assert feature_to_node(feature, "CCT_BUILDINGS") is None


def test_missing_geometry_is_rejected():
    feature = {"attributes": {"OBJECTID": 8, "BLDG_USG": "OFFICE"}, "geometry": {}}
    assert feature_to_node(feature, "CCT_BUILDINGS") is None
