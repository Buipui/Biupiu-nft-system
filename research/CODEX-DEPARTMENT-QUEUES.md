# BIUPIU CODEX DEPARTMENT SIMULATION QUEUES

**Version:** 1.2  
**Date:** 15 September 2026  
**Status:** Active — source-integrated computational backlog

## P0 execution activation

Activated P0 queues: `Q-CODEX-001`, `Q-IP-001`, `Q-AGRI-001`, `Q-HEMP-001`, and `Q-PHO-001`. Activation means the test definition, inputs and validation gate are ready; it does not mean a simulation result exists.

## New source-routing rule

All new CODEX queues inherit `research/SOURCE-TO-DEPARTMENT-CROSSWALK.md` and `research/BIUPIU-RESEARCH-OPERATING-PROTOCOL-v2.0.md`. Ancient-technology queues should use AnthroSource alongside primary archaeology/JSTOR; systems/implementation questions should use Emerald where relevant; scientific mechanisms should use ResearchGate/publisher sources; implementation/IP questions should use patents/declassified records; code and computational methods must be versioned and licensed.

## Queue

| Queue ID | Department | Model / method | First executable test | Dataset required | Validation | IP gate | Priority | Status |
|---|---|---|---|---|---|---|---|---|
| Q-BIO-001 | BIO | statistics / biological modelling | plant-trait baseline | trait observations + metadata | independent replication | IP review | P1 | DATA-GATHERING |
| Q-GEN-001 | BIO-GEN | statistics / genetics | cultivar-trait association baseline | approved datasets | statistical controls + oversight | IP/FTO | P2 | DATA-GATHERING |
| Q-AGRI-001 | AGRI | soil/water time series | regenerative pilot baseline vs control | soil, water, biomass | field controls | IP | P0 | READY |
| Q-HEMP-001 | HEMP | process mass balance | bast/hurd/loss balance | representative feedstock | measured yield + repeat trials | IP | P0 | READY |
| Q-BC-001 | BIOCARBON | thermal/process model | pyrolysis/activation parameter map | feedstock + process data | material/yield tests | IP | P1 | DATA-GATHERING |
| Q-BCH-001 | BIOCHEM | process simulation | biomass fractionation balance | composition + process parameters | laboratory balance closure | IP | P2 | DATA-GATHERING |
| Q-TEX-001 | TEXTILES | process optimisation | fibre opening vs properties | fibre/property data | standard textile tests | IP | P1 | READY |
| Q-COAT-001 | COAT | DOE/materials testing | adhesion/durability screen | formulation matrix | adhesion/wear/weathering | IP | P2 | DATA-GATHERING |
| Q-COMP-001 | COMPOSITES | FEA | coupon stiffness/strength model | fibre/resin properties | physical coupon tests | IP | P1 | READY |
| Q-MAT-001 | MATERIALS | FEA/thermal | material property baseline | composition/property data | lab characterisation | IP | P2 | DATA-GATHERING |
| Q-WATER-001 | WATER | GIS/hydrology | watershed/spring baseline | DEM, geology, rainfall, discharge | field observations | IP | P1 | READY |
| Q-ENERGY-001 | ENERGY | CFD/FEA/system model | turbine/storage baseline | geometry + operating data | bench/published benchmark | IP | P1 | READY |
| Q-EM-001 | ELECTROMAG | EM simulation | dielectric/EMI baseline | permittivity, conductivity, geometry | VNA/EM test | IP | P2 | DATA-GATHERING |
| Q-PHO-001 | PHOTONICS | wave propagation | structured-light turbulence baseline | WITS-PHO resource IDs + optical parameters | lab/field link test | IP | P0 | READY |
| Q-PHQ-001 | PH-QPM | inverse optics | phase/wavefront reconstruction | camera/interferometry data | ground-truth phase | IP | P1 | DATA-GATHERING |
| Q-CRM-001 | CRM | optical/electronic materials | quantum-dot/crystal screen | material parameters | published/lab values | IP | P2 | DATA-GATHERING |
| Q-MM-001 | METAMATERIALS | full-wave EM | unit-cell resonance baseline | geometry + materials | independent solver/experiment | IP | P1 | READY |
| Q-AERO-001 | AERO | CFD/FEA | public geometry lift/drag baseline | public geometry + boundary conditions | wind-tunnel/published data | IP/FTO | P1 | DATA-GATHERING |
| Q-MAR-001 | MARINE | CFD/FSI | propeller/pumpjet baseline | geometry + fluid conditions | tow/bench/published benchmark | IP/FTO | P1 | DATA-GATHERING |
| Q-CODEX-001 | COMPUTE | reproducibility | source-to-result provenance test | source hashes + dataset | deterministic rerun | IP | P0 | READY |
| Q-AI-001 | AI | surrogate/optimisation | baseline surrogate after validated data | labelled data | held-out test set | IP | P2 | UNQUEUED |
| Q-GEO-001 | GEOMETRY | parametric/topology optimisation | public geometry reconstruction | mesh/CAD parameters | geometry/performance comparison | IP/FTO | P1 | READY |
| Q-DT-001 | DIGITAL-TWIN | state estimation | sensor-to-model calibration | time-series sensor data | physical measurement | IP | P2 | UNQUEUED |
| Q-ROB-001 | ROBOTICS | robot-cell simulation | material handling/inspection task | cycle times + robot specs | physical cell trial | IP/safety | P2 | UNQUEUED |
| Q-MFG-001 | ADV-MFG | manufacturability | process-constraint comparison | machine/process limits | produced sample | IP | P1 | DATA-GATHERING |
| Q-BMED-001 | BIOMED | imaging/statistics | non-clinical benchmark | approved/public dataset | benchmark metrics | IP/regulatory | P3 | UNQUEUED |
| Q-GA-001 | GEOARCH | GIS/geophysics | evidence-ladder site map | maps, DEM, geology, geophysics | independent field evidence | IP | P2 | DATA-GATHERING |
| Q-GIS-001 | LAND-GIS | georeferencing | historical map reproduction | scan + control points | independent coordinate check | IP | P1 | READY |
| Q-ALA-001 | ALA | temporal GIS | time-slice reconstruction | dated maps/environmental data | chronology/spatial controls | NFT/IP | P2 | DATA-GATHERING |
| Q-AAT-001 | AAT | reconstruction/experimental archaeology | documented ancient engineering model | archaeological measurements + AnthroSource/JSTOR/primary records | physical/historical evidence | IP | P2 | DATA-GATHERING |
| Q-ATH-001 | AAT-H | comparative analysis | material-culture dataset | archaeological/anthropological sources incl. AnthroSource | source provenance | IP/NFT | P3 | UNQUEUED |
| Q-COAST-001 | PALAEO-COAST | palaeogeographic GIS | ancient coastline scenario | sea-level/DEM/geology | dated proxies | IP/NFT | P2 | DATA-GATHERING |
| Q-CULT-001 | EMPIRE-CULTURE | network/GIS | documented exchange/political network map | dated historical/archaeological data | source triangulation | NFT | P3 | UNQUEUED |
| Q-NH-001 | NAGA-HIM | source genealogy/GIS | location claim evidence ladder | primary/historical/GIS sources | independent evidence | SPEC/IP | P3 | DATA-GATHERING |
| Q-AMR-001 | OLMEC-AMR | chronology/material comparison | contact hypothesis test | archaeological/material data | statistical/archaeological controls | SPEC/IP | P3 | UNQUEUED |
| Q-FAIL-001 | PRE-DISASTER | spatial failure analysis | before/after degradation sequence | imagery/field records | independent temporal evidence | IP | P2 | DATA-GATHERING |
| Q-GMAG-001 | GEO-MAG | statistics/field model | Monte Carlo alignment test | coordinates + geology/topography/magnetic field | control-site comparison | IP | P2 | READY |
| Q-SPEC-001 | SPEC | claim extraction + null/alternative | priority claim through CODEX-SPEC-EXECUTION | source capture + primary evidence | independent corroboration | IP/NFT | P1 | READY |
| Q-IP-001 | IP | prior-art graph | invention vs patents/public technical records | patent/public-source corpus | human/legal review | FTO/patentability | P0 | READY |
| Q-NFT-001 | NFT-ART | procedural generation | original art from validated research dataset | validated data + algorithm | deterministic regeneration | provenance/licence | P2 | DATA-GATHERING |
| Q-PROV-001 | NFT-PROV | provenance graph | hash source/data/algorithm/parameters | source + artefact hashes | reproducibility | licence/IP | P1 | READY |
| Q-RES-REG-001 | Governance | register normalisation | recover historical payment/resource register | original register file | source-file verification | provenance/IP | P1 | VERIFY SOURCE FILE |

## New AAT/AAT-H source integration

`Q-AAT-001` and `Q-ATH-001` now explicitly accept AnthroSource records as a scholarly anthropology/archaeology input. AnthroSource does not replace primary archaeological evidence and does not prove engineering performance. It supplies context on craft, technology transmission, materiality, cultural ecology and human practice.

## Emerald integration

Water, agriculture, infrastructure and systems-design queues should use relevant Emerald publications when an exact publication/DOI has been identified. Emerald evidence should inform implementation/system models; it does not replace primary experimental engineering data.

## IP / public-declassified control

`Q-IP-001` covers patent, prior-art and public/declassified technical-document research. It records document identifier, date, legal/publication status, technical disclosure, claim/feature mapping, novelty overlap, licence/public-domain status, evidence classification and independent validation. No classified or non-public military information is sought.

## Queue states

UNQUEUED → DATA-GATHERING → READY → SIMULATING → VALIDATING → PROTOTYPE → COMPLETE. HOLD is used for data, regulatory, safety, licence or IP blocks. VERIFY SOURCE FILE is used where an original historical register/source must first be recovered.

## Execution order

**P0:** Q-CODEX-001, Q-IP-001, Q-AGRI-001, Q-HEMP-001, Q-PHO-001.  
**P1:** Q-BC-001, Q-TEX-001, Q-COMP-001, Q-ENERGY-001, Q-MM-001, Q-AERO-001, Q-MAR-001, Q-GEO-001, Q-GIS-001, Q-SPEC-001, Q-PROV-001, Q-RES-REG-001.  
**P2:** remaining validated R&D queues.  
**P3:** exploratory/comparative queues.

All queues inherit the repository evidence doctrine and must not convert speculative material into factual claims merely because a simulation is visually suggestive.
