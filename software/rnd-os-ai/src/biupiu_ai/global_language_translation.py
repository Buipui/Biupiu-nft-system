"""Biupiu Global Language Translation contract.

Provider-neutral and fail-closed: records language metadata and provenance
without embedding credentials or silently inventing translation results.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Optional

SUPPORTED_LANGUAGE_FAMILIES = {
    "af","ar","bn","bg","ca","cs","da","de","el","en","es","et","fa","fi",
    "fil","fr","he","hi","hr","hu","id","is","it","ja","ka","kk","ko","lt",
    "lv","ms","nl","no","pl","pt","ro","ru","sk","sl","sr","sv","sw","ta",
    "te","th","tr","uk","ur","vi","xh","yo","zh","zu","st","tn","ts","so",
    "am","ha","ig","km","my","ne","si","pa","mr","gu","kn","ml","or","as",
}


@dataclass(frozen=True)
class TranslationRecord:
    source_text: str
    source_language: str
    target_language: str
    translated_text: Optional[str]
    provider: Optional[str]
    status: str
    provenance: str

    def to_dict(self) -> dict:
        return asdict(self)


def normalise_language(language: str) -> str:
    """Return a canonical BCP-47-compatible language tag.

    Script and region subtags are retained; the previous implementation
    discarded them, which made locale selection lossy.
    """
    value = language.strip().replace("_", "-")
    if not value:
        raise ValueError("language code must not be empty")
    parts = [part for part in value.split("-") if part]
    if not parts:
        raise ValueError("language code must not be empty")
    parts[0] = parts[0].lower()
    for i in range(1, len(parts)):
        part = parts[i]
        if len(part) == 4 and part.isalpha():
            parts[i] = part.title()
        elif len(part) in (2, 3) and part.isalnum():
            parts[i] = part.upper() if len(part) == 2 else part
        else:
            parts[i] = part
    return "-".join(parts)


def language_family(language: str) -> str:
    return normalise_language(language).split("-", 1)[0]


def fallback_chain(language: str, default: str = "en") -> tuple[str, ...]:
    """Build a deterministic locale fallback chain without losing identity."""
    canonical = normalise_language(language)
    family = canonical.split("-", 1)[0]
    default_tag = normalise_language(default)
    result = [canonical]
    if family != canonical:
        result.append(family)
    if default_tag not in result:
        result.append(default_tag)
    return tuple(result)


def validate_language(language: str) -> str:
    code = language_family(language)
    if code not in SUPPORTED_LANGUAGE_FAMILIES:
        raise ValueError(f"Unsupported language code: {language}")
    return code


def translate(
    source_text: str,
    source_language: str,
    target_language: str = "en",
    *,
    provider: Optional[str] = None,
    translated_text: Optional[str] = None,
) -> TranslationRecord:
    source = validate_language(source_language)
    target = validate_language(target_language)
    if not source_text:
        raise ValueError("source_text must not be empty")
    if translated_text is not None and not provider:
        raise ValueError("provider is required when translated_text is supplied")
    status = "translated-unverified" if translated_text is not None else "pending"
    provenance = (
        f"biupiu.translation:{source}->{target};"
        f"provider={provider or 'none'};verification=required"
    )
    return TranslationRecord(
        source_text=source_text,
        source_language=source,
        target_language=target,
        translated_text=translated_text,
        provider=provider,
        status=status,
        provenance=provenance,
    )
