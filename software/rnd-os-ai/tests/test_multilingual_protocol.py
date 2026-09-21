from biupiu_ai.multilingual_protocol import *

def test_script_detection():
    assert detect_language("日本語の研究") == "ja"
    assert detect_language("机器学习") == "zh"
    assert detect_language("한국어 연구") == "ko"
    assert detect_language("Русский") == "ru"
    assert detect_language("English") == "und"

def test_query_expansion():
    p=QueryProfile("CFD","computational fluid dynamics",("Strömungsmechanik",),("CFD",),("fluid simulation",),("numerical fluid mechanics",),("CFD",))
    assert expand_query(p)==("computational fluid dynamics","Strömungsmechanik","CFD","fluid simulation","numerical fluid mechanics")

def test_routing():
    r=route_departments("photonic materials for aerospace simulation")
    assert {"PHOTONICS","MATERIALS","AERO","COMPUTE","DIGITAL-TWIN"}.issubset(r)

def test_translation_is_not_validation():
    assert translation_is_validation() is False

def test_fail_closed_provenance():
    r=MultilingualRecord("id","Original","de","https://example.invalid",translated_title="English")
    assert "translation_method" in validate_record(r)
