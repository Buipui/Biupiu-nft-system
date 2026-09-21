"""Harvest planner for globally discoverable public modules.

It records candidate implementation families and safe integration actions without
copying third-party code. Code may be imported only after explicit license/provenance
validation and compatibility/regression testing.
"""
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class ModuleCandidate:
    family: str
    action: str
    acceptance: Tuple[str,...]

CANDIDATES=(
ModuleCandidate("open-data-api","build native catalogue/API adapters",("public","license","schema","tests")),
ModuleCandidate("SPARQL/DCAT","build metadata query adapter",("public","license","query-test")),
ModuleCandidate("OCR","use permissively licensed OCR backend behind adapter",("license","accuracy-test","sandbox")),
ModuleCandidate("geospatial","use open geospatial libraries behind adapter",("license","projection-test","regression")),
ModuleCandidate("signal-processing","build first-party numerical wrappers",("math-test","dependency-review","regression")),
ModuleCandidate("patent-prior-art","build evidence/provenance indexer",("source-uri","citation","rights")),
ModuleCandidate("repository-discovery","index public repositories/dependencies",("license","provenance","security")),
ModuleCandidate("OEM-public-SDK","adapter for public SDK/API/docs only",("OEM-license","API-version","integration-test")),
)

def harvest_plan():
    return CANDIDATES

def eligible_for_first_party_implementation(candidate):
    return all(candidate.acceptance)
