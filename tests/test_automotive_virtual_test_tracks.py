from simulators.automotive_virtual_test_tracks_v0_1 import create_default_tracks,curvature_speed_kph,run_screen,Track,Segment

def test_tracks_validate():
    for t in create_default_tracks():
        t.validate(); assert t.length_m > 0

def test_mu_effect():
    assert curvature_speed_kph(80,.6) < curvature_speed_kph(80,1.0)

def test_screen():
    assert run_screen(create_default_tracks()[0])["validation"] == "screened"

def test_invalid_segment():
    try: Track("BAD","test",(Segment("x","straight",0),)).validate()
    except ValueError: return
    assert False
