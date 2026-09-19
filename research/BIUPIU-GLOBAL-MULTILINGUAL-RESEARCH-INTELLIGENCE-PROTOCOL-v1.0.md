# BIUPIU GLOBAL MULTILINGUAL RESEARCH & INTELLIGENCE PROTOCOL v1.0

Date: 19 September 2026
Status: Active
Purpose: Extend Biupiu World research discovery beyond English-language search so useful scientific, engineering, agricultural, medical, computational, historical, cultural and technical information can be discovered in the language in which it was originally published.

## 1. Core rule
Biupiu World is treated as a multilingual knowledge system. English is the coordination language, not the exclusive evidence language.
1. Discover sources in their native language.
2. Preserve original title, authors, identifiers and source URL.
3. Create an English working summary only as a derived representation.
4. Retain original-language evidence.
5. Translate terminology both directions for future retrieval.
6. Route useful records to relevant Biupiu departments.
7. Deduplicate by DOI, ISBN, repository ID, patent number, dataset ID, Git commit or another stable identifier.
8. Classify evidence independently of language.
9. Record licence and access conditions before reuse.
10. Never treat machine translation as scientific validation.

## 2. Global discovery architecture
Primary discovery layers: OpenAlex, Crossref/DataCite, DOAJ, national repositories, institutional repositories, specialist repositories, patents/standards, GitHub/code, datasets, and primary historical/archaeological archives.
OpenAlex is the global scholarly graph/index layer; it exposes works, authors, institutions, funders, topics, languages and repository locations. Its repository network covers thousands of repositories and links open-access copies where available.
DOAJ is the broad open-access journal discovery layer and currently reports coverage across 92 languages and 141 countries.

## 3. Native-language search matrix
### Russian / Cyrillic
Priority sources: Math-Net.Ru; V.A. Trapeznikov Institute of Control Sciences (IPU RAS); Russian Academy of Sciences repositories and journals; CyberLeninka; eLIBRARY/RSCI where access permits; institutional repositories.
Priority departments: COMPUTE, AI, CONTROL, DIGITAL-TWIN, MATHEMATICS, PHYSICS, ENGINEERING, MATERIALS, AERO, ENERGY, BIO.
Special rule: search both Cyrillic and transliterated terminology.

### Japanese
Priority sources: CiNii Research; J-STAGE; J-STAGE Data; NII institutional repositories/IRDB; Jxiv.
Priority departments: MATERIALS, MANUFACTURING, ROBOTICS, AI, COMPUTE, AGRI, BIO, ENERGY, PHOTONICS, AERO, AUTOMOTIVE.

### Chinese
Priority discovery: university repositories; Chinese Academy of Sciences resources; national science/data repositories; Chinese-language journal indexes and open repositories where legally accessible.
Search both simplified Chinese and English equivalents. Where possible, use DOI/ISBN/patent identifiers rather than relying on translated titles.

### Korean
Priority discovery: Korean university repositories; national research repositories; KCI-indexed literature; science and engineering institutional archives.
Search Hangul plus English terminology.

### Spanish / Portuguese
Priority sources: SciELO; Redalyc; institutional repositories; national university repositories; Latin American and Iberian open-science platforms.
Priority departments: AGRI, WATER, BIO, MEDICAL, MATERIALS, ENERGY, TEXTILES, FOOD, ECOLOGY, COMPUTE, SOCIAL SYSTEMS.

### French
Priority sources: HAL; institutional repositories; French national research infrastructure; open-access university repositories.
Priority departments: MATERIALS, AERO, ENERGY, AGRI, BIO, PHOTONICS, COMPUTE, ARCHITECTURE, HISTORY.

### German
Priority sources: German university repositories; institutional open-access archives; specialist engineering/science repositories.
Priority departments: ENGINEERING, AUTOMOTIVE, AERO, MATERIALS, ROBOTICS, ENERGY, COMPUTE, MANUFACTURING.

### Arabic / Persian / Turkish
Search native scripts and transliterated technical terminology. Route useful material through HISTORY, WATER, AGRI, ARCHITECTURE, MATERIALS, MEDICAL, ENERGY and COMPUTE as appropriate.

### African languages
Dedicated discovery track for isiXhosa, isiZulu, Sesotho, Setswana, Sepedi, Afrikaans and other relevant African languages, prioritising universities, government repositories, indigenous-knowledge archives, agricultural knowledge, biodiversity, ethnobotany, conservation, archaeology and language resources.

### South Asian languages
Search Hindi, Bengali, Urdu, Tamil, Telugu, Marathi, Gujarati, Kannada, Malayalam and other relevant languages through institutional repositories, national research platforms and open-access indexes.

### Southeast Asian languages
Search Indonesian, Malay, Vietnamese, Thai, Filipino and other relevant languages through national university repositories, government science portals and open-access journal networks.

### Nordic / Central / Eastern European languages
Search Danish, Swedish, Norwegian, Finnish, Icelandic, Dutch, Polish, Czech, Slovak, Hungarian, Romanian, Bulgarian, Serbian, Croatian, Ukrainian, Greek and related languages through institutional and national repositories.

## 4. Translation-aware retrieval
Every important query should have: Concept ID; English term; native-language term; transliteration; synonyms; historical terminology; engineering terminology; abbreviation.
Example: computational fluid dynamics → CFD → native-language equivalent → local abbreviation → fluid simulation → numerical fluid mechanics.
Search engines must not assume literal translation is sufficient.

## 5. Evidence and provenance
Each multilingual record should store: Source ID; original title; original language; English working title; author(s); institution; publication year; DOI/ISBN/ISSN/patent/repository ID; original URL; open-access status; licence; abstract or structured summary; translation method; unresolved terminology; department routing; evidence class; research question; code/dataset linkage; Digital Twin linkage; IP status; reproducibility status.

## 6. Intelligence-layer integration
Multilingual sources become candidate knowledge, not automatically trusted knowledge.
Pipeline: Native discovery → identifier resolution → source verification → translation/terminology extraction → evidence classification → claim extraction → department routing → cross-source comparison → computational model/code queue → Digital Twin → validation → approved knowledge record.
The Intelligence layer preserves original evidence, translated representation, provenance, contradictions, uncertainty and superseded versions. It must not silently overwrite an earlier translation or source interpretation.

## 7. OS integration
Biupiu OS should expose multilingual research services as modular interfaces:
LANG-DETECT; TERM-MAP; NATIVE-SEARCH; SOURCE-VERIFY; TRANSLATE; CLAIM-EXTRACT; EVIDENCE-CLASSIFY; DEPARTMENT-ROUTE; DEDUP; PROVENANCE; LICENCE-CHECK; DIGITAL-TWIN-QUEUE.
Biupiu AI remains separate from the authoritative OS layer. AI may discover, translate, classify and propose links; OS validation and provenance controls determine authoritative state.

## 8. Department routing
All departments can receive multilingual records. Automatic routing should use subject/entity matching rather than language.
Core routes include AGRI, BIO, BIO-GEN, FOOD, WATER, MATERIALS, BIOCARBON, ENERGY, PHOTONICS, AERO, MARINE, AUTOMOTIVE, TEXTILES, ADV-MFG, ROBOTICS, AI, COMPUTE, GEOMETRY, DIGITAL-TWIN, MEDICAL, CONSERVATION, ARCHAEOLOGY/HISTORY, ARCHITECTURE, IP/PATENTS and WORLD SYSTEMS.

## 9. Safety, rights and quality gates
- Do not scrape or redistribute copyrighted material merely because it is discoverable.
- Prefer metadata, abstracts, open-access copies and legally reusable datasets.
- Record licence terms.
- Treat third-party code as external until licence/security review passes.
- Treat machine translation as a retrieval aid and working representation.
- Important technical, medical, legal or safety-critical conclusions require verification against the original source and, where possible, an independent source.
- Conflicting translations remain visible for human review.
- Restricted, classified or unlawfully obtained material is not incorporated.

## 10. Initial validated source additions
### Math-Net.Ru
Native-language and English interfaces expose mathematics, physics, information technology and related scientific resources. The portal reports hundreds of thousands of publications and provides journal archives and free-access material subject to individual journal conditions.
### IPU RAS
The V.A. Trapeznikov Institute of Control Sciences provides research directions, laboratories, periodicals and scientific publications in control science and related systems research. Its material is particularly relevant to Biupiu AI, robotics, autonomous systems, Digital Twins, optimisation and control.
### ISAND concept
IPU material describing ISAND is relevant to Biupiu Intelligence because it describes an ontology and system for collecting, storing and analysing scientific-publication metadata, thematic profiles and network relationships. This is indexed as external research architecture to study, not as Biupiu-owned software.
### CiNii Research / J-STAGE / NII
CiNii Research integrates articles, books, dissertations, research data and projects, including material from J-STAGE, institutional repositories and KAKEN. J-STAGE Data provides a research-data repository layer.
### DOAJ
Global open-access discovery layer covering many languages and countries; use as a multilingual journal discovery index, not as a guarantee that every individual record is high quality.
### SciELO
Multilingual regional discovery layer with substantial Spanish, Portuguese and English coverage and collections spanning Latin America, Portugal, Spain and South Africa.
### Open Books
Use legitimate open-book platforms and institutional open-access book collections. Do not treat similarly named abandoned or unlicensed book-sharing repositories as authoritative.

## 11. Search cadence
For each major Biupiu department: run English discovery; run native-language discovery; run transliteration/synonym discovery; search regional repositories; compare results; deduplicate; route records; update the research index; create code/model tasks where justified; preserve source and licence provenance.

## 12. Version
BIUPIU GLOBAL MULTILINGUAL RESEARCH & INTELLIGENCE PROTOCOL v1.0
Activated: 19 September 2026
This protocol is an indexing/search architecture. It does not claim that Biupiu has exhaustively searched every language or every publication in the world. Coverage expands iteratively through the language matrix and source registry.