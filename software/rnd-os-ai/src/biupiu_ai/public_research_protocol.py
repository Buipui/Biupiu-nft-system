"""Fail-closed discovery manifest for public declassified/patent research.

This is a metadata protocol: it records authoritative public sources and maps them
to candidate Biupiu modules. It does not download or execute restricted material.
"""
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class ResearchFeed:
    feed_id: str
    institution: str
    url: str
    module_families: Tuple[str, ...]
    public_only: bool = True
    executable: bool = False

PUBLIC_RESEARCH_FEEDS = (
    ResearchFeed("cia-foia-reading-room","CIA","https://www.cia.gov/readingroom/",
                  ("ocr","document-analysis","geospatial","historical-systems")),
    ResearchFeed("nsa-declassification","NSA","https://www.nsa.gov/Helpful-Links/NSA-FOIA/Declassification-Transparency-Initiatives/",
                  ("cryptography","signal-processing","information-assurance","historical-systems")),
    ResearchFeed("uspto-patent-public-search","USPTO","https://www.uspto.gov/patents/search/patent-public-search",
                  ("prior-art","technology-landscape","provenance")),
)

def discoverable_module_families() -> Tuple[str, ...]:
    return tuple(sorted({m for f in PUBLIC_RESEARCH_FEEDS for m in f.module_families}))

def executable_feeds() -> Tuple[ResearchFeed, ...]:
    return tuple(f for f in PUBLIC_RESEARCH_FEEDS if f.executable)

def validate_feed(feed: ResearchFeed) -> bool:
    return bool(feed.public_only and not feed.executable and feed.url.startswith("https://"))
