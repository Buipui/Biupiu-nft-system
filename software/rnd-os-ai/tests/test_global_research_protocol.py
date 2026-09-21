from biupiu_ai.global_research_protocol import (
    GLOBAL_PUBLIC_SOURCES, OEM_PUBLIC_SOURCES, discoverable_classes,
    executable_sources, validate_source
)

def test_multilingual_sources_exist():
    ids={s.source_id for s in GLOBAL_PUBLIC_SOURCES}
    assert {"govdata-de","recherche-data-gouv","data-gov-in","data-go-jp","data-go-kr","dados-gov-br","open-canada"} <= ids

def test_oem_layer_exists():
    assert any(s.source_id=="eu-digital-vehicle-ecosystem" for s in OEM_PUBLIC_SOURCES)

def test_global_module_classes():
    c=discoverable_classes()
    assert {"open-data","research-data","open-source","repositories","automotive"} <= set(c)

def test_every_source_is_fail_closed():
    assert executable_sources()==()
    assert all(validate_source(s) for s in GLOBAL_PUBLIC_SOURCES+OEM_PUBLIC_SOURCES)
