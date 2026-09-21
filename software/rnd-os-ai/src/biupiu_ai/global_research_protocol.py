"""Global public/open research discovery registry.

Languages/regions are discovery hints; every source remains subject to provenance,
licence, security, compatibility and regression gates. OEM sources are restricted
to public developer portals, standards, SDKs and openly licensed material.
"""
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class GlobalSource:
    source_id:str
    organisation:str
    region:str
    language:str
    url:str
    classes:Tuple[str,...]
    public_api_or_repo:bool=True
    executable:bool=False

GLOBAL_PUBLIC_SOURCES=(
GlobalSource("govdata-de","GovData / Germany","Germany","German","https://data.gov.de/",("open-data","environment","transport","science")),
GlobalSource("recherche-data-gouv","Recherche Data Gouv / France","France","French","https://recherche.data.gouv.fr/en",("research-data","agriculture","science")),
GlobalSource("data-gov-in","OGD Platform India","India","English/Indian languages","https://data.gov.in/",("open-data","agriculture","environment","apis")),
GlobalSource("data-go-jp","Japanese Government Open Data","Japan","Japanese","https://www.data.go.jp/",("open-data","government-data")),
GlobalSource("data-go-kr","Korean Government Open Data","South Korea","Korean","https://www.data.go.kr/en/index.do",("open-data","apis","science")),
GlobalSource("dados-gov-br","Brazil Open Data","Brazil","Portuguese","https://dados.gov.br/",("open-data","science","environment")),
GlobalSource("open-canada","Open Government Canada","Canada","English/French","https://open.canada.ca/en/open-data",("open-data","research")),
GlobalSource("data-gouv-fr","data.gouv.fr","France","French","https://www.data.gouv.fr/fr/",("open-data","apis")),
GlobalSource("eu-osor","EU Open Source Observatory","EU","English/multilingual","https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/oss-repositories",("open-source","public-software")),
GlobalSource("ecosyste-ms","ecosyste.ms","Global","English/multilingual","https://ecosyste.ms/",("repositories","dependencies","provenance")),
GlobalSource("eclipse-research","Eclipse Foundation Research","Global","English/multilingual","https://www.eclipse.org/research/",("open-source","research","embedded","iot","vehicles")),
)

OEM_PUBLIC_SOURCES=(
GlobalSource("eu-digital-vehicle-ecosystem","EU Digital Vehicle Ecosystem","EU","multilingual","https://digital-strategy.ec.europa.eu/en/policies/digital-vehicle-ecosystem",("automotive","software-defined-vehicle","open-source")),
)

def source_ids(): return tuple(s.source_id for s in GLOBAL_PUBLIC_SOURCES+OEM_PUBLIC_SOURCES)
def discoverable_classes(): return tuple(sorted({c for s in GLOBAL_PUBLIC_SOURCES+OEM_PUBLIC_SOURCES for c in s.classes}))
def executable_sources(): return tuple(s for s in GLOBAL_PUBLIC_SOURCES+OEM_PUBLIC_SOURCES if s.executable)
def validate_source(s): return s.url.startswith("https://") and s.public_api_or_repo and not s.executable
