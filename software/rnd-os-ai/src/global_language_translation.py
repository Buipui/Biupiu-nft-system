"""Biupiu Global Language Translation hard-code interface.

Provider-neutral translation contract. It deliberately does not embed API
credentials or select a commercial translation provider.

The module normalises language metadata, preserves the source text, records
translation provenance, and provides a deterministic fallback when no
translation backend is configured. It is an integration boundary, not a
claim of autonomous translation capability.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Optional


SUPPORTED_LANGUAGE_FAMILIES = {
    "af", "ar", "bn", "bg", "ca", "cs", "da", "de", "el", "en", "es",
    "et", "fa", "fi", "fil", "fr", "he", "hi", "hr", "hu", "id", "is",
    "it", "ja", "ka", "kk", "ko", "lt", "lv", "ms", "nl", "no", "pl",
    "pt", "ro", "ru", "sk", "sl", "sr", "sv", "sw", "ta", "te", "th",
    "tr", "uk", "ur", "vi", "xh", "yo", "zh", "zu", "st", "tn", "ts",
    "so", "am", "ha", "ig", "km", "my", "ne", "si", "pa", "mr", "gu",
    "kn", "ml", "or", "as",
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
    """Return the base language tag used by the Biupiu language registry."""
    value = language.strip().lower().replace("_", "-")
    return value.split("-", 1)[0]


def validate_language(language: str) -> str:
    code = normalise_language(language)
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
    """Create a provenance-preserving translation record.

    A real translation backend is intentionally injected rather than hard-coded.
    If no backend result is supplied, status is 'pending' and source text is
    preserved unchanged. This prevents the OS from treating untranslated text
    or an unverified machine translation as authoritative.
    """
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
