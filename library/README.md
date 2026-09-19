# Biupiu Research Library v1.0

Reference-only library for current journals, technical articles, Popular Mechanics discovery records, open-source projects, CAD/simulation references, and InvestSA material.

## Separation
- Research records are references, not automatic product assets.
- Commercial and personal R&D records are explicitly separated.
- Copyrighted articles are referenced by URL/DOI; full-text copies are stored only when the source explicitly permits downloading/reuse.
- Open-source code/assets require licence verification before integration.
- Popular Mechanics is a discovery/secondary-source layer; original scientific papers remain the technical authority.

## Intake states
DISCOVERED -> VERIFIED -> LICENCE-CHECKED -> ROUTED -> DOWNLOAD-ELIGIBLE -> DOWNLOADED -> VALIDATED -> IMPLEMENTATION-CANDIDATE

## Automation rule
A future CI harvester may refresh metadata and download only explicitly licence-eligible open-access documents. It must never bypass paywalls, access controls, or copyright restrictions.
