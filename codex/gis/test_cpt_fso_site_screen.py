from codex.gis.cpt_fso_site_screen import (
    SiteObservation,
    candidate_links,
    site_screen_score,
    straight_line_distance_m,
)


def test_distance_is_deterministic():
    a = SiteObservation("A", -33.95, 18.48, 20, True, True, "approved", True)
    b = SiteObservation("B", -33.951, 18.481, 20, True, True, "approved", True)
    assert straight_line_distance_m(a, b) == straight_line_distance_m(a, b)
    assert straight_line_distance_m(a, b) > 0


def test_permission_is_gate():
    site = SiteObservation("A", -33.95, 18.48, 40, True, True, "pending", True)
    assert site_screen_score(site) == 0.0


def test_safety_constraint_is_gate():
    site = SiteObservation("A", -33.95, 18.48, 40, True, True, "approved", True, aviation_constraint=True)
    assert site_screen_score(site) == 0.0


def test_candidate_link_generation():
    a = SiteObservation("A", -33.9500, 18.4800, 20, True, True, "approved", True)
    b = SiteObservation("B", -33.9505, 18.4805, 20, True, True, "approved", True)
    c = SiteObservation("C", -34.10, 18.60, 20, True, True, "approved", True)
    links = candidate_links([a, b, c], max_distance_m=200.0)
    assert len(links) == 1
    assert {links[0].source_id, links[0].target_id} == {"A", "B"}
