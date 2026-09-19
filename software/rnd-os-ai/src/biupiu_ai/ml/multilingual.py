"""Multilingual ML/research query profiles.

This module connects ML discovery to the existing Global Multilingual Research
Protocol. It expands terminology without claiming translation correctness.
Actual translation remains a replaceable provider with provenance.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from biupiu_ai.global_language_translation import validate_language


@dataclass(frozen=True)
class SearchProfile:
    concept_id: str
    english_term: str
    source_language: str
    native_terms: Tuple[str, ...]
    transliterations: Tuple[str, ...]
    synonyms: Tuple[str, ...]
    historical_terms: Tuple[str, ...]
    engineering_terms: Tuple[str, ...]
    abbreviations: Tuple[str, ...]


def build_search_profile(
    concept_id: str,
    english_term: str,
    source_language: str = "en",
    *,
    native_terms: Tuple[str, ...] = (),
    transliterations: Tuple[str, ...] = (),
    synonyms: Tuple[str, ...] = (),
    historical_terms: Tuple[str, ...] = (),
    engineering_terms: Tuple[str, ...] = (),
    abbreviations: Tuple[str, ...] = (),
) -> SearchProfile:
    if not concept_id or not english_term:
        raise ValueError("concept_id and english_term are required")
    language = validate_language(source_language)
    if language == "en" and native_terms == ():
        native_terms = (english_term,)
    return SearchProfile(
        concept_id, english_term, language, native_terms, transliterations,
        synonyms, historical_terms, engineering_terms, abbreviations,
    )


def query_terms(profile: SearchProfile) -> Tuple[str, ...]:
    values = (
        profile.english_term,
        *profile.native_terms,
        *profile.transliterations,
        *profile.synonyms,
        *profile.historical_terms,
        *profile.engineering_terms,
        *profile.abbreviations,
    )
    return tuple(dict.fromkeys(v.strip() for v in values if v and v.strip()))
