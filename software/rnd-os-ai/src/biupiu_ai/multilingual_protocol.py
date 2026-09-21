"""Dependency-free Biupiu multilingual research protocol core."""
from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class QueryProfile:
    concept_id: str
    english_term: str
    native_terms: tuple[str, ...] = ()
    transliterations: tuple[str, ...] = ()
    synonyms: tuple[str, ...] = ()
    engineering_terms: tuple[str, ...] = ()
    abbreviations: tuple[str, ...] = ()

@dataclass(frozen=True)
class MultilingualRecord:
    source_id: str
    original_title: str
    original_language: str
    source_url: str
    licence: str | None = None
    translated_title: str | None = None
    translation_method: str | None = None
    evidence_state: str = "UNRESOLVED"
    department_routes: tuple[str, ...] = ()
    provenance_preserved: bool = True

DEPARTMENT_KEYWORDS = {
    "AGRI": ("agriculture","farming","soil","crop","water"),
    "BIO": ("biotechnology","biology","plant","genetics"),
    "MATERIALS": ("material","composite","metallurgy","resin"),
    "PHOTONICS": ("photonics","optics","laser","light"),
    "AI": ("artificial intelligence","machine learning","neural","ai"),
    "COMPUTE": ("algorithm","computing","software","simulation"),
    "DIGITAL-TWIN": ("digital twin","simulation","virtual model"),
    "ROBOTICS": ("robot","robotics","automation","control"),
    "AERO": ("aerospace","aircraft","flight","aerodynamics"),
    "AUTOMOTIVE": ("automotive","vehicle","mobility","chassis"),
    "MARINE": ("marine","ship","vessel","ocean"),
    "TEXTILES": ("textile","fiber","fibre","fabric"),
    "MEDICAL": ("medical","medicine","clinical","health"),
    "CONSERVATION": ("biodiversity","conservation","endemic","ecology"),
}

def detect_language(text: str) -> str:
    if not text or not text.strip(): return "und"
    checks = (
        ("zh", any("一" <= c <= "鿿" for c in text)),
        ("ja", any("぀" <= c <= "ヿ" for c in text)),
        ("ko", any("가" <= c <= "힯" for c in text)),
        ("ar", any("؀" <= c <= "ۿ" for c in text)),
        ("ru", any("Ѐ" <= c <= "ӿ" for c in text)),
        ("hi", any("ऀ" <= c <= "ॿ" for c in text)),
        ("bn", any("ঀ" <= c <= "৿" for c in text)),
        ("ta", any("஀" <= c <= "௿" for c in text)),
        ("te", any("ఀ" <= c <= "౿" for c in text)),
    )
    for code, found in checks:
        if found: return code
    return "und"

def expand_query(profile: QueryProfile, languages: Iterable[str] | None = None) -> tuple[str, ...]:
    terms = (profile.english_term, *profile.native_terms, *profile.transliterations, *profile.synonyms, *profile.engineering_terms, *profile.abbreviations)
    return tuple(dict.fromkeys(t.strip() for t in terms if t and t.strip()))

def route_departments(text: str) -> tuple[str, ...]:
    lowered = text.casefold()
    return tuple(d for d, words in DEPARTMENT_KEYWORDS.items() if any(w in lowered for w in words))

def validate_record(record: MultilingualRecord) -> tuple[str, ...]:
    errors = []
    for field in ("source_id","original_title","original_language","source_url"):
        if not getattr(record, field): errors.append(field)
    if record.translated_title and not record.translation_method: errors.append("translation_method")
    if record.evidence_state not in {"UNRESOLVED","CANDIDATE","VERIFIED","CONTRADICTED"}: errors.append("evidence_state")
    if not record.provenance_preserved: errors.append("provenance_preserved")
    return tuple(errors)

def translation_is_validation() -> bool: return False
