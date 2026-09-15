# BIUPIU CODEX DEPARTMENT SIMULATION QUEUES

**Version:** 1.0  
**Date:** 15 September 2026  
**Status:** Active queue architecture

## Purpose

This file converts the department architecture into reproducible computational work queues. A queue entry is not a claim that the underlying hypothesis is true. It is an instruction to define data, model assumptions, controls, validation criteria and an evidence update.

**Universal workflow:** `source capture → claim/question → dataset → baseline → null/alternative → model → simulation → validation → result → evidence status → IP gate → prototype/commercial/NFT gate`.

## Queue

| Queue ID | Department | Model / method | First executable test | Dataset required | Validation | IP gate | Priority | Status |
|---|---|---|---|---|---|---|---|---|
| Q-BIO-001 | BIO | statistics / biological modelling | define plant-trait baseline and reproducibility protocol | trait observations + metadata | independent replication | IP review | P1 | DATA-GATHERING |
| Q-GEN-001 | BIO-GEN | statistics / genetics | cultivar-trait association baseline | approved datasets | statistical controls + institutional oversight | IP/FTO | P2 | DATA-GATHERING |
| Q-AGRI-001 | AGRI | soil/water time series | regenerative pilot baseline vs control | soil, water, biomass | field controls | IP | P0 | READY |
| Q-HEMP-001 | HEMP | process mass balance | bast/hurd/loss mass balance from representative stalk | feedstock samples | measured yield + repeat trials | IP | P0 | READY |
| Q-BC-001 | BIOCARBON | thermal/process model | map pyrolysis/activation parameter space | feedstock + process data | yield/surface-area/material tests | IP | P1 | DATA-GATHERING |
| Q-BCH-001 | BIOCHEM | process simulation | mass/energy balance for biomass fractionation | composition + process parameters | laboratory balance closure | IP | P2 | DATA-GATHERING |
| Q-TEX-001 | TEXTILES | process optimisation | fibre opening/cleanliness vs mechanical properties | fibre length, fineness, moisture, tensile | standard textile tests | IP | P1 | READY |
| Q-COAT-001 | COAT | DOE / materials testing | formulation screening for adhesion and durability | formulation matrix | adhesion/wear/weathering tests | IP | P2 | DATA-GATHERING |
| Q-COMP-001 | COMPOSITES | FEA | coupon-level stiffness/strength model | fibre/resin properties | physical coupon tests | IP | P1 | READY |
| Q-MAT-001 | MATERIALS | FEA / thermal | property baseline for candidate materials | composition/property data | lab characterisation | IP | P2 | DATA-GATHERING |
| Q-WATER-001 | WATER | GIS/hydrology | watershed/spring inventory baseline | DEM, geology, rainfall, discharge | field observations | IP | P1 | READY |
| Q-ENERGY-001 | ENERGY | CFD/FEA/system model | turbine/storage baseline under defined boundary conditions | geometry + operating data | bench test / published benchmark | IP | P1 | READY |
| Q-EM-001 | ELECTROMAG | EM simulation | dielectric/EMI baseline for candidate hemp composites | permittivity, conductivity, geometry | VNA/EM test where available | IP | P2 | DATA-GATHERING |
| Q-PHO-001 | PHOTONICS | wave propagation | structured-light propagation through turbulence | wavelength, turbulence model, beam mode | laboratory/field link test | IP | P0 | READY |
| Q-PHQ-001 | PH-QPM | inverse optics | reconstruct wavefront/phase from synthetic and measured data | camera/interferometry data | ground-truth phase | IP | P1 | DATA-GATHERING |
| Q-CRM-001 | CRM | electronic/optical materials modelling | quantum-dot/crystal candidate property screen | material parameters | published/lab values | IP | P2 | DATA-GATHERING |
| Q-MM-001 | METAMATERIALS | full-wave EM | unit-cell resonance / transmission baseline | geometry + material properties | independent solver or experiment | IP | P1 | READY |
| Q-AERO-001 | AERO | CFD/FEA | public geometry baseline for lift/drag | public geometry + boundary conditions | wind-tunnel/published data | IP/FTO | P1 | DATA-GATHERING |
| Q-MAR-001 | MARINE | CFD/FSI | propeller/pumpjet baseline | geometry + fluid conditions | tow/bench data or published benchmark | IP/FTO | P1 | DATA-GATHERING |
| Q-CODEX-001 | COMPUTE | reproducibility | execute source-to-result provenance test | source hashes + dataset | deterministic rerun | IP | P0 | READY |
| Q-AI-001 | AI | surrogate/optimisation | train a baseline surrogate only after validated dataset exists | labelled simulation/experiment data | held-out test set | IP | P2 | UNQUEUED |
| Q-GEO-001 | GEOMETRY | parametric/topology optimisation | reconstruct and optimise a non-sensitive public geometry | mesh/CAD parameters | geometry and performance comparison | IP/FTO | P1 | READY |
| Q-DT-001 | DIGITAL-TWIN | state estimation | sensor-to-model calibration loop | time-series sensor data | physical measurement | IP | P2 | UNQUEUED |
| Q-ROB-001 | ROBOTICS | robot-cell simulation | simulate material handling/inspection task | cycle times + robot specs | physical cell trial | IP/safety | P2 | UNQUEUED |
| Q-MFG-001 | ADV-MFG | manufacturability | compare design against process constraints | machine/process limits | produced sample | IP | P1 | DATA-GATHERING |
| Q-BMED-001 | BIOMED | imaging/statistics | define non-clinical benchmark dataset and validation plan | approved/public dataset | benchmark metrics | IP/regulatory | P3 | UNQUEUED |
| Q-GA-001 | GEOARCH | GIS/geophysics | evidence-ladder mapping of a selected site | maps, DEM, geology, geophysics | independent field evidence | IP | P2 | DATA-GATHERING |
| Q-GIS-001 | LAND-GIS | georeferencing | reproduce one historical map georeference | scan + control points | independent coordinate check | IP | P1 | READY |
| Q-ALA-001 | ALA | temporal GIS | build one time-slice reconstruction | dated maps/environmental data | chronology and spatial controls | NFT/IP | P2 | DATA-GATHERING |
| Q-AAT-001 | AAT | reconstruction/experimental archaeology | model one documented ancient engineering system | archaeological measurements | physical/historical evidence | IP | P2 | DATA-GATHERING |
| Q-ATH-001 | AAT-H | comparative analysis | build material-culture transmission dataset | archaeological/anthropological sources | source provenance | IP/NFT | P3 | UNQUEUED |
| Q-COAST-001 | PALAEO-COAST | palaeogeographic GIS | reconstruct one ancient coastline scenario | sea-level/DEM/geology | dated proxies | IP/NFT | P2 | DATA-GATHERING |
| Q-CULT-001 | EMPIRE-CULTURE | network/GIS | map documented exchange/political networks | dated historical/archaeological data | source triangulation | NFT | P3 | UNQUEUED |
| Q-NH-001 | NAGA-HIM | source genealogy/GIS | test a specific location claim against evidence ladder | primary/historical/GIS sources | independent evidence | SPEC/IP | P3 | DATA-GATHERING |
| Q-AMR-001 | OLMEC-AMR | chronology/material comparison | test a defined contact hypothesis against independent datasets | archaeological chronology/material data | statistical + archaeological controls | SPEC/IP | P3 | UNQUEUED |
| Q-FAIL-001 | PRE-DISASTER | spatial failure analysis | quantify one before/after degradation sequence | imagery/field records | independent temporal evidence | IP | P2 | DATA-GATHERING |
| Q-GMAG-001 | GEO-MAG | statistics/field model | Monte Carlo test for claimed site alignments | coordinates + geology/topography/magnetic field | control-site comparison | IP | P2 | READY |
| Q-SPEC-001 | SPEC | claim extraction + null/alternative | execute one high-priority claim through CODEX-SPEC-EXECUTION | source capture + primary evidence | independent corroboration | IP/NFT | P1 | READY |
| Q-IP-001 | IP | prior-art graph | map one invention against patents/public technical records | patent/public-source corpus | human/legal review | FTO/patentability | P0 | READY |
| Q-NFT-001 | NFT-ART | procedural generation | generate original artwork from a validated research dataset | validated data + algorithm | deterministic regeneration | provenance/licence | P2 | DATA-GATHERING |
| Q-PROV-001 | NFT-PROV | provenance graph | hash source/data/algorithm/parameters | source + artefact hashes | reproducibility check | licence/IP | P1 | READY |

## Wits / ResearchGate / Emerald photonics queue

The Wits structured-light work is promoted to a **P0/P1 validation queue**, not because the claims are automatically accepted, but because the work supplies a concrete experimental domain with measurable optical propagation variables. The first computational target is atmospheric-turbulence propagation of structured light, followed by link-budget and error-rate comparisons against conventional baselines.

Required controls:

1. Conventional Gaussian/orthogonal baseline.
2. Same wavelength, power, aperture and receiver assumptions.
3. Explicit turbulence model and parameter range.
4. Pre-registered performance metric such as BER, mode fidelity or received power.
5. Independent implementation or laboratory measurement before an engineering claim is promoted.

ResearchGate is used for discovery/cross-reference; original Wits/publisher records remain preferred primary sources. Emerald records must identify the exact publication/DOI before being used as independent evidence.

## IP / declassified queue

`Q-IP-001` is the gate for all prior patent and public/declassified technical-document work. It must produce:

- document identifier and date;
- legal/publication status;
- exact technical disclosure relevant to the Biupiu concept;
- claim/feature mapping;
- novelty overlap and possible design-around;
- licence/public-domain status where applicable;
- evidence classification;
- recommendation for independent simulation or prototype testing.

No classified, restricted or non-public military material is required or sought.

## Payment/resource-register queue

`Q-RES-REG-001` is a governance task rather than a technical simulation. It remains **VERIFY SOURCE FILE** because a standalone historical payment/resource register was not located in the current archive verification pass.

Once the actual register is found, each entry should be normalised to:

`Register ID → date → project/department → resource/payment category → source document → amount/quantity if applicable → status → evidence/licence → IP relationship → related Research ID → related CODEX Queue ID`.

## Queue state definitions

- **UNQUEUED** — defined but not yet prepared.
- **DATA-GATHERING** — source/data acquisition in progress.
- **READY** — enough structure exists for the first reproducible test.
- **SIMULATING** — computational execution underway.
- **VALIDATING** — comparing model against independent data.
- **PROTOTYPE** — physical or manufacturing test.
- **COMPLETE** — result archived with evidence and provenance.
- **HOLD** — blocked by data, regulatory, safety, licence or IP gate.

## Execution order

**P0:** Q-CODEX-001, Q-IP-001, Q-AGRI-001, Q-HEMP-001, Q-PHO-001.  
**P1:** Q-BIOCARBON/BC-001, Q-TEX-001, Q-COMP-001, Q-ENERGY-001, Q-MM-001, Q-AERO-001, Q-MAR-001, Q-GEO-001, Q-GIS-001, Q-SPEC-001, Q-PROV-001.  
**P2:** remaining validated R&D queues requiring additional datasets.  
**P3:** exploratory or low-priority speculative/comparative queues.

All queues inherit the repository evidence doctrine and must not convert speculative source material into factual claims merely because a simulation is visually suggestive.
