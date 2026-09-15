# BIUPIU Core Evidence-Layer Architecture

**Version:** 1.0  
**Date:** 15 September 2026  
**Status:** Active — master source and evidence-control architecture

## Purpose

This file defines the permanent Biupiu evidence architecture for Ancient Applied Technology (AAT), anthropology, archaeology, ancient civilizations, historical engineering, materials, water systems, agriculture, human origins and computational reconstruction.

The architecture separates **hypothesis generation**, **scholarly evidence**, **primary evidence**, **scientific validation**, **engineering reconstruction**, **computation** and **Biupiu experimentation**. No source category automatically proves a claim.

## Core evidence layers

### L01 — Primary archaeological and historical evidence
**Role:** Excavated sites, artefacts, stratigraphy, inscriptions, dated materials, museum records, primary historical documents and original datasets.

**Rule:** Highest-priority evidence for claims about what physically existed, where and when. Provenance and dating must be recorded.

### L02 — JSTOR
**Role:** Scholarly discovery and full-text research layer covering archaeology, anthropology, history, material culture, technology, environment and related humanities/social-science literature.

**Control:** JSTOR is a scholarly evidence layer, not an automatic truth filter. Record article/book title, author, publication, year, DOI/stable identifier where available, relevant pages and the exact proposition supported. Prefer the original primary study or publisher version where available.

### L03 — AnthroSource / American Anthropological Association
**Role:** Anthropology, archaeology, human-material relationships, craft production, technology transmission, cultural ecology and social organisation.

**Control:** Use alongside JSTOR rather than as a duplicate. AnthroSource can contain current AAA journal runs and reference-linking capabilities not identical to JSTOR.

### L04 — ResearchGate / scientific literature discovery
**Role:** Experimental science, archaeometry, metallurgy, materials science, genetics, engineering, computational research and author-uploaded papers.

**Control:** ResearchGate is a discovery/access layer. Prefer DOI/publisher/institutional versions when available. Do not treat author-upload status as peer-review verification.

### L05 — Emerald Insight / Emerald Publishing
**Role:** Engineering management, sustainability, water systems, agriculture, infrastructure, optimisation, implementation and socioeconomic/system-level analysis.

**Control:** Index at publication/DOI level and distinguish peer-reviewed research from proceedings, reviews and other content types.

### L06 — Robert Sepehr / YouTube / Atlantean Gardens
**Role:** Alternative-history and speculative hypothesis generation, comparative mythology, ancient-civilisation narratives, human-origins claims, ancient geography and technology claims.

**Control:** **Hypothesis-generation layer only.** A Sepehr video is never counted as independent corroboration of itself or of another channel repeating the same source. Extract exact claim + timestamp, trace it to the earliest identifiable evidence/source and test independently.

### L07 — Ancient texts and historical literature
**Role:** Primary or near-primary textual testimony, translations, chronicles, technical descriptions and mythological/cultural traditions.

**Control:** Distinguish historical testimony from mythology, later commentary and modern interpretation. Preserve original language/translation provenance where possible.

### L08 — Scientific databases and primary research
**Role:** Archaeogenomics, radiocarbon/dating, isotopes, palaeoclimate, geology, geophysics, chemistry, physics and environmental science.

**Control:** Use quantitative data and uncertainty ranges. Do not convert correlation into causation without testing.

### L09 — Patents / prior art / IP
**Role:** Existing modern implementations, claims, drawings, materials, algorithms and freedom-to-operate context.

**Control:** Patent existence does not prove efficacy or commercial success. Record jurisdiction, priority, legal status and relevant claims. Ancient/public-domain knowledge is not patentable merely because Biupiu rediscovers it; protect only novel modern implementations where legally appropriate.

### L10 — Public and declassified technical archives
**Role:** Historical engineering, propulsion, turbine, materials and systems documentation that is lawfully public/declassified.

**Control:** Historical documentation is evidence of what was documented, not automatic evidence that every claim or performance statement was correct. No classified/restricted material is to be incorporated.

### L11 — GitHub / BIUPIU CODEX
**Role:** Reproducible code, algorithms, simulation methods, datasets, notebooks, computational archaeology, geometry reconstruction and engineering models.

**Control:** Record repository, commit/version, author, licence, dependencies, method and provenance. Public GitHub code is not automatically public-domain or commercially reusable.

### L12 — Biupiu computational validation
**Role:** GIS, CAD, CFD, FEA/FEM, multiphysics, thermal, EM, acoustic, network, statistical, optimisation and digital-twin tests.

**Control:** Every model requires assumptions, inputs, parameters, versioned code, baseline/null model, uncertainty/limitations and validation target.

### L13 — Biupiu physical/experimental validation
**Role:** Laboratory reconstruction, materials testing, hydraulic experiments, prototypes, sensor measurements and repeatability studies.

**Control:** Experimental results must preserve raw data, method, calibration, sample provenance and reproducibility information.

## Evidence workflow

`Sepehr/other hypothesis → exact claim → source genealogy → primary evidence → JSTOR → AnthroSource → ResearchGate/scientific literature → Emerald/system literature → texts → patents/declassified records → GIS/CODEX model → physical experiment → evidence status`

## Evidence status

- **A — Directly demonstrated:** direct physical/experimental evidence with adequate provenance.
- **B — Strongly supported:** multiple independent, high-quality lines of evidence converge.
- **C — Plausible/incomplete:** credible mechanism/evidence but material gaps remain.
- **D — Testable hypothesis:** sufficiently defined to design a falsifiable test.
- **E — Unsupported/contradicted:** evidence is absent, inadequate or materially inconsistent.
- **M — Mythological/cultural:** valuable as cultural evidence but not a factual technological claim by itself.
- **S — Speculative/inspirational:** useful for research or artwork generation but not evidentiary.

## Independence rule

Three videos repeating the same book, website, photograph or archaeological claim count as **one source lineage**, not three independent confirmations. Independent corroboration requires a genuinely separate evidentiary chain.

## Sepehr-specific control

Sepehr material is retained because it can surface unusual research questions. However, claims involving race, ancestry, lost civilisations, Atlantis, ancient technology, transoceanic contact, catastrophism or human origins must be decomposed into specific testable propositions and checked against primary archaeology, genetics, geology, chronology and scholarship. Cultural or speculative narratives must not be converted into NFT metadata as factual claims without validation.

## JSTOR-specific control

JSTOR is a core scholarly layer. Searches should use targeted terms such as `ancient technology`, `technological change`, `technology transfer`, `experimental archaeology`, `ancient metallurgy`, `ancient hydraulic engineering`, `civilization collapse`, `population movement`, `material culture`, `southern African archaeology`, `Mapungubwe`, `Bokoni`, `Great Zimbabwe`, `Nubia`, `Kush`, `Mesoamerica`, `Andean engineering` and equivalent site/technology-specific terms.

## Cross-disciplinary research matrix

| Question | Primary | JSTOR | AnthroSource | ResearchGate | Emerald | Sepehr | CODEX | Experiment |
|---|---|---|---|---|---|---|---|---|
| Did it exist? | ✓ | ✓ | ✓ | ✓ |  | hypothesis only |  | ✓ |
| When did it exist? | ✓ | ✓ | ✓ | ✓ |  | hypothesis only | dating models |  |
| How did it work? | artefact | ✓ | ✓ | ✓ | ✓ | hypothesis | CFD/FEA/EM/etc. | ✓ |
| Did technology diffuse? | artefact/trade | ✓ | ✓ | ✓ | ✓ | hypothesis | GIS/network models |  |
| Did climate/environment matter? | proxies | ✓ | ✓ | ✓ | ✓ | hypothesis | climate/GIS models |  |
| Can it be reproduced? | ✓ | experimental archaeology | ✓ | ✓ | ✓ | hypothesis | simulation | ✓ |
| Is it commercially useful today? |  | ✓ | ✓ | ✓ | ✓ | idea source | optimisation | prototype |

## Biupiu source genealogy record

Each indexed claim should carry:

`Source ID → source type → exact title/video → creator/author → date → URL/stable ID → timestamp/page → claim text/paraphrase → cited source lineage → independent sources → evidence status → Biupiu division → CODEX model → experimental path → IP status → NFT relevance`

## Core source relationships

`AAT ↔ JSTOR ↔ AnthroSource ↔ ResearchGate ↔ Emerald`

`AAT ↔ Primary Archaeology ↔ Ancient Texts ↔ GEOARCH/LAND-GIS`

`AAT ↔ Sepehr hypotheses ↔ SPEC-CLAIM-REGISTRY ↔ evidence testing`

`AAT ↔ CODEX ↔ GEOMETRY ↔ GIS ↔ CFD/FEA/multiphysics ↔ experimental reconstruction`

`All validated modern implementations ↔ IP/Patent/FTO`

`Validated research ↔ NFT-PROV only after licence/evidence review`

## Status

This architecture is the master source-control layer for future Biupiu ancient-civilization and ancient-technology research. It is deliberately designed to allow unconventional hypotheses to be investigated without lowering evidence standards.
