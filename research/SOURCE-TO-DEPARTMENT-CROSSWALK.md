# BIUPIU SOURCE → DEPARTMENT CROSSWALK

**Version:** 1.0  
**Date:** 15 September 2026  
**Status:** Active

## Purpose

This crosswalk prevents source silos. A source is assigned to one or more Biupiu departments only where its subject materially informs that department. Assignment is an indexing relationship, not evidence that every claim in the source applies to the department.

| Source layer | Primary Biupiu use | Main departments |
|---|---|---|
| Primary archaeology/history | sites, artefacts, chronology, historical process | AAT, AAT-H, GEOARCH, ALA, PALAEO-COAST |
| JSTOR | archaeology, anthropology, history, material culture, technology, environment | AAT, AAT-H, AGRI, WATER, MATERIALS, GEOARCH |
| AnthroSource | anthropology, craft, technology transmission, human-material systems, cultural ecology | AAT, AAT-H, AGRI, HEMP, TEXTILES, MATERIALS, GEOARCH, ALA |
| ResearchGate | scientific/engineering discovery, archaeometry, metallurgy, materials, computation | MATERIALS, BIOCARBON, ENERGY, PHOTONICS, AERO, MARINE, COMPUTE, AI |
| Emerald Insight | sustainability, water, agriculture, infrastructure, engineering management, implementation | AGRI, WATER, ENERGY, ADV-MFG, COMPUTE, AI |
| Ancient texts | historical/cultural terminology and technical descriptions | AAT, AGRI, WATER, BIO, AAT-H |
| Scientific primary data | quantitative validation | BIO, BIO-GEN, AGRI, WATER, MATERIALS, ENERGY, GEOARCH, GEO-MAG |
| Patents/prior art | modern implementation, novelty/FTO | IP + relevant technical department |
| Public/declassified engineering | historical technical architecture | ENERGY, MATERIALS, AERO, MARINE, ELECTROMAG, GEOMETRY, COMPUTE |
| GitHub / BIUPIU CODEX | code, algorithms, simulation, datasets | COMPUTE, MATH, GEOMETRY, AI, DIGITAL-TWIN, ROBOTICS, all technical departments |
| Mathematics / scientific-computing layer | symbolic/numerical models, optimisation, dynamics, uncertainty and validation | MATH, COMPUTE, GEOMETRY, AI, ROBOTICS, DIGITAL-TWIN + target department |
| Computational validation | reproducible modelling | COMPUTE, GEOMETRY, AI, DIGITAL-TWIN + target department |
| Physical validation | prototype and measurement | target department + EXPERIMENT record |
| Controlled speculative sources | hypothesis generation only | SPEC + target department after claim decomposition |

## Ancient technology source bundle

For AAT investigations, the default research bundle is:

`PRIMARY → JSTOR → ANTHROSOURCE → RESEARCHGATE → EMERALD → TEXTS → PATENTS/DECLASS → CODEX → EXPERIMENT`

Not every investigation needs every layer. The investigator should record why a layer was skipped.

## Coding correlation rule

Whenever a source produces a computationally testable question, create or update a CODEX queue. Minimum linkage:

`Source ID → Claim ID → Department → Research Question → Model → Dataset → Code/Commit → Result → Evidence Status → IP Status`

## IP correlation rule

A modern engineering result must be compared with relevant prior art before being described as a Biupiu invention. Public-domain/ancient knowledge is background knowledge; novelty, inventive step, ownership and FTO require separate legal review.

## NFT correlation rule

Only original Biupiu artwork or properly licensed source material may enter the NFT pipeline. Research-inspired artwork can use speculative themes, but metadata must distinguish cultural narrative, hypothesis and established evidence.

## Current priority correlations

### Ancient agriculture
`AnthroSource + JSTOR + primary archaeology → AGRI/AAT/AAT-H → GEOARCH/LAND-GIS → CODEX hydrology/soil model → field validation`

### Ancient metallurgy
`AnthroSource craft/materiality + ResearchGate archaeometallurgy + primary artefacts → MATERIALS/BIOCARBON/AAT → thermal/material model → laboratory validation`

### Ancient hydraulic engineering
`AnthroSource cultural ecology + Emerald water/sustainability + primary archaeological engineering → WATER/AGRI/AAT → GIS/CFD → hydraulic prototype`

### Ancient geometry
`AnthroSource technology/materiality + archaeology → AAT/GEOMETRY → parametric reconstruction → CFD/FEA → experimental model`

### HempCarbon
`ResearchGate scientific literature + patents → HEMP/BIOCARBON/ENERGY/MATERIALS → CODEX electrochemical/material dataset → cell testing → IP review`

### Turbine engineering
`ResearchGate + Emerald optimisation + patents + declassified engineering → ENERGY/MARINE/AERO/GEOMETRY/COMPUTE → CFD/FEA/optimisation → bench testing → IP review`

## Status

This crosswalk is the permanent routing rule for future Biupiu research indexing.


## Multilingual routing extension — 19 September 2026

Language must not restrict department routing. A source discovered in any language is routed by subject, entities and research questions.

| Language/search layer | Default routing | Notes |
|---|---|---|
| Russian/Cyrillic | COMPUTE, AI, CONTROL, DIGITAL-TWIN, PHYSICS, ENGINEERING, MATERIALS, ENERGY | Search Cyrillic + transliteration |
| Japanese | MATERIALS, ROBOTICS, AI, MANUFACTURING, ENERGY, PHOTONICS, AERO, AUTOMOTIVE | Preserve original identifiers |
| Chinese | MATERIALS, MANUFACTURING, AGRI, ENERGY, PHOTONICS, AI, AERO | Search simplified Chinese + English |
| Korean | MATERIALS, ROBOTICS, COMPUTE, BIO, ENERGY, MANUFACTURING | Search Hangul + English |
| Spanish/Portuguese | AGRI, WATER, BIO, MEDICAL, MATERIALS, TEXTILES, FOOD, ECOLOGY | Regional open-science repositories |
| French/German | ENGINEERING, MATERIALS, AERO, ENERGY, AGRI, BIO, COMPUTE, MANUFACTURING | Institutional repository priority |
| Arabic/Persian/Turkish | HISTORY, WATER, AGRI, ARCHITECTURE, MATERIALS, MEDICAL, ENERGY | Native-script + transliteration |
| African languages | AGRI, BIO, CONSERVATION, ETHNOBOTANY, ARCHAEOLOGY, WATER, LANGUAGE | Prioritise universities, government and indigenous-knowledge archives |
| South/Southeast Asian languages | AGRI, WATER, BIO, MATERIALS, TEXTILES, FOOD, ENERGY, COMPUTE | National and university repositories |
| European regional languages | ENGINEERING, MATERIALS, ENERGY, AERO, ROBOTICS, COMPUTE, HISTORY | National/institutional repositories |

Minimum linkage remains: `Source ID → Claim ID → Department → Research Question → Model → Dataset → Code/Commit → Result → Evidence Status → IP Status`.


## Simulator / graphics repository code-routing extension — 19 September 2026

Usable-code candidates identified from the multilingual simulator/graphics pass are registered as external references for future Intelligence searches. Discovery is not incorporation.

| Repository | Primary routing | Validation gate |
|---|---|---|
| Gazebo gz-sim | ROBOTICS, DIGITAL-TWIN, SIMULATION | licence + ROS2 compatibility + security + tests |
| ros_gz | ROBOTICS, ROS2, DIGITAL-TWIN | ROS2 compatibility + integration tests |
| DISCOVERSE | ROBOTICS, MUJOCO, REAL2SIM2REAL, AI | licence + dependency + reproducibility tests |
| GaussianRenderer | GRAPHICS, 3DGS, COMPUTATIONAL-VISION | licence + GPU compatibility + benchmark |
| gs-real2sim | 3DGS, DIGITAL-TWIN, MUJOCO | licence + dataset provenance + physics validation |
| DLR OAISYS | SIMULATION, BLENDER, PLANETARY-ROBOTICS | licence + dependency audit + reproducibility |
| rbot | AMR, ROS2, GAZEBO, NAVIGATION | licence + ROS2/security + navigation tests |

Routing rule:
`Repository → Resource ID → Language/Source → Department → Simulator Adapter → Digital Twin → AI Training → Validation → Provenance → Commit`

Hard-link policy: these repository URLs are searchable anchors in the Biupiu Intelligence Network. They remain `discovered-reference` until explicit validation promotes them to `validated-incorporated`.


## Mathematics Division routing — 19 September 2026

The MATH department is the repository-wide quantitative support layer. Complex problems route through `PROBLEM → VARIABLES → ASSUMPTIONS → DIMENSIONAL CHECK → SYMBOLIC MODEL → NUMERICAL MODEL → SOLVER → SENSITIVITY/UNCERTAINTY → VALIDATION → RESULT → RESEARCH RECORD`.

MATH supports GEOMETRY, COMPUTE, AI, ROBOTICS, DIGITAL-TWIN and specialist scientific/engineering departments. A converged solver result is not automatically experimental evidence.

## Infrastructure routing — 19 September 2026

`MATH → COMPUTE → GEOMETRY → AI → ROBOTICS → DIGITAL-TWIN → EXPERIMENT → LEARNING`

Third-party code remains external until licence, provenance, security, dependency, compatibility and regression gates pass.
