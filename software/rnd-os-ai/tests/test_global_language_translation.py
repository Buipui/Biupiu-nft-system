from biupiu_ai.global_language_translation import (
    SUPPORTED_LANGUAGE_FAMILIES,
    normalise_language,
    fallback_chain,
    language_family,
    translate,
    validate_language,
)


def test_language_normalisation():
    assert normalise_language("pt-BR") == "pt"
    assert normalise_language("ZH_cn") == "zh"


def test_global_language_registry_contains_key_world_languages():
    for code in (
        "en", "af", "xh", "zu", "ar", "ru", "zh", "ja", "ko",
        "hi", "ur", "fr", "de", "es", "pt",
    ):
        assert code in SUPPORTED_LANGUAGE_FAMILIES


def test_translation_is_provenance_preserving():
    record = translate(
        "Hallo Welt",
        "de",
        "en",
        provider="test-provider",
        translated_text="Hello world",
    )
    assert record.source_text == "Hallo Welt"
    assert record.translated_text == "Hello world"
    assert record.status == "translated-unverified"
    assert "verification=required" in record.provenance


def test_missing_backend_does_not_fake_translation():
    record = translate("Sawubona", "zu", "en")
    assert record.translated_text is None
    assert record.status == "pending"


def test_unknown_language_is_rejected():
    try:
        validate_language("xx")
    except ValueError:
        return
    raise AssertionError("unknown language must be rejected")


def test_bcp47_script_and_region_are_preserved():
    assert normalise_language("zh_Hant_TW") == "zh-Hant-TW"
    assert language_family("pt-BR") == "pt"


def test_locale_fallback_is_deterministic():
    assert fallback_chain("pt-BR") == ("pt-BR", "pt", "en")
    assert fallback_chain("en-US") == ("en-US", "en")
