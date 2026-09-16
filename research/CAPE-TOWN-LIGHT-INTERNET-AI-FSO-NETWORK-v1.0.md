# Biupiu Cape Town Light-Based Internet & AI-Assisted FSO Network v1.0

**Record:** BPU-NET-FSO-CPT-001  
**Status:** Feasibility / research architecture — NOT a deployed network  
**Date:** September 2026  
**Parent streams:** PHOTONICS, PH-QPM, AI, CODEX, MM, GEOMETRY, DIGITAL-TWIN, ROBOTICS

## Objective

Develop a research-grade architecture for a Cape Town metropolitan light-based internet network using terrestrial free-space optical (FSO) links as high-capacity point-to-point backhaul/access links, with indoor Visible Light Communication (VLC/LiFi) as a complementary local-access layer and RF/fibre fallback for resilience.

This is a proposed engineering study, not a claim that a Cape Town network has already been surveyed, approved, funded or deployed.

## Evidence foundation

Wits University Optical Communication Lab explicitly researches long-range FSO, VLC/LiFi, optical computing, machine intelligence and hybrid optical/RF/PLC communications. Its research page also describes a permanent 300 m campus FSO testbed and AI-assisted approaches to optical-channel adaptation. citehttps://www.wits.ac.za/oclab/research/

Wits researchers reported in 2026 a real-world experiment across the Wits West Campus showing that information encoded in the topology of structured light can remain intact under naturally occurring atmospheric turbulence. The experiment used skyrmion-structured light and is directly relevant to robust FSO system research. citehttps://www.wits.ac.za/news/latest-news/research-news/2026/--2026-08/wits-researchers-use-lights-topology-to-beat-atmospheric-distortion.html

Wits also reports earlier work on turbulence eigenmodes, vectorial structured-light encoding and light correcting light. citehttps://wiredspace.wits.ac.za/items/10e33a69-bf08-4abd-a3a7-a612ef788744 citehttps://www.wits.ac.za/news/latest-news/research-news/2023/2023-06/researchers-demonstrate-noise-free-communication-with-structured-light-.html

A South African FSO feasibility study explicitly included Cape Town and evaluated visibility, wind and atmospheric attenuation. A separate South African analysis reports that Cape Town's FSO availability can be strongly affected by fog, making weather-aware link management and fallback paths essential. citehttps://www.researchgate.net/publication/302922768_Feasibility_study_of_free-space_optical_communication_for_South_Africa citehttps://www.scielo.org.za/scielo.php?pid=S1991-16962022000100002&script=sci_arttext

## Cape Town candidate deployment zones

The following are **candidate zones for GIS/LOS/meteorological screening**, not confirmed installation sites. Exact rooftops, coordinates, private properties and municipal assets require a later site survey and permissions.

### Zone A — Cape Town CBD / Foreshore

Potential role: dense urban backbone/access aggregation between high-rise rooftops and major network/fibre nodes.

Screening variables:
- rooftop-to-rooftop line of sight;
- building height and obstruction clearance;
- fibre backhaul availability;
- electrical power and battery/UPS space;
- pedestrian/public-safety exclusion zones;
- atmospheric visibility and fog statistics;
- optical eye-safety classification;
- municipal/property permissions.

### Zone B — Observatory / Salt River / Woodstock corridor

Potential role: research/education and mixed commercial-residential test corridor with relatively short multi-hop links before metropolitan expansion.

Priority research question: whether a chain of shorter optical hops plus AI-controlled routing gives better availability than attempting very long direct links.

### Zone C — Rondebosch / Newlands / Claremont corridor

Potential role: university, research, residential and commercial interoperability testbed. This zone should be evaluated for connections to existing fibre and institutional networks rather than treated as an independent internet backbone.

### Zone D — Bellville / Tyger Valley / northern metropolitan corridor

Potential role: secondary aggregation corridor and candidate industrial/commercial test zone.

Research emphasis:
- rooftop density;
- LOS corridor continuity;
- fog/cloud/rain statistics;
- fibre interconnection;
- resilient multi-hop topology.

### Zone E — Century City / Paarden Eiland / Milnerton corridor

Potential role: high-density commercial/industrial and coastal test environment.

Special consideration: coastal aerosol, humidity, wind and fog can materially affect optical availability. These must be measured rather than assumed.

### Zone F — Airport / logistics / industrial corridor

Potential role: controlled industrial IoT, vehicle-to-infrastructure and warehouse VLC/LiFi experiments, subject to airport/aviation safety restrictions and property permissions.

### Zone G — Stellenbosch / Cape Winelands research extension

Potential role: longer rural/semi-rural FSO links and agricultural/remote-connectivity experiments outside the dense urban mesh.

This is an extension zone rather than part of the initial Cape Town metropolitan mesh.

## Proposed network architecture

```text
                     INTERNET / FIBRE CORE
                              |
                       AI ROUTING LAYER
                              |
             +----------------+----------------+
             |                                 |
        FSO BACKBONE                       RF/FIBRE FALLBACK
             |
       +-----+-----+
       |           |
   FSO NODE     FSO NODE
       |           |
       +-----+-----+
             |
       LOCAL OPTICAL EDGE
        /            \
    VLC/LiFi       FSO AP
      /               \
 indoor users       outdoor users
```

The network should not depend on optical links alone. Fibre, RF or another approved bearer should provide failover where fog, obstruction, maintenance or weather makes an optical path unavailable.

## AI-assisted control plane

The AI layer should initially be a **decision-support and optimisation system**, not an autonomous safety controller.

### Inputs

- received optical power;
- bit-error rate / packet loss;
- atmospheric visibility;
- temperature, humidity and pressure;
- wind speed/direction;
- beam alignment telemetry;
- transmitter/receiver status;
- link latency and throughput;
- weather forecasts;
- historical link-quality data;
- topology state;
- fibre/RF fallback availability.

### AI functions

1. Predict short-term link-quality degradation.
2. Select structured-light mode families appropriate to the channel.
3. Recommend adaptive coding/modulation settings.
4. Select an alternate FSO hop before link failure where possible.
5. Optimise network load across optical/RF/fibre paths.
6. Detect alignment drift and maintenance conditions.
7. Build a digital twin of the optical mesh.
8. Estimate uncertainty and abstain from automatic changes when confidence is insufficient.

## Wits-derived optical research integration

The Biupiu CODEX should explicitly model:

- turbulence as an optical channel/operator;
- turbulence eigenmodes;
- structured-light/OAM modes;
- topological/skyrmion encoding;
- vectorial-light invariants;
- adaptive signal processing;
- atmospheric channel simulation;
- hybrid optical/RF/PLC routing;
- AI prediction and inverse optimisation.

Wits describes AI and machine intelligence as an active part of its optical communications research, including real-time channel adaptation and computational treatment of turbulent channels. citehttps://www.wits.ac.za/oclab/research/

## Cape Town GIS/site-screening algorithm

### `CPT-FSO-SITE-01`

Candidate nodes should be scored by measurable engineering criteria rather than subjective location preference.

```text
candidate_site
  → building/structure permission
  → geographic coordinates
  → elevation/height
  → LOS obstruction analysis
  → candidate-neighbour discovery
  → link distance
  → visibility/fog statistics
  → wind statistics
  → fibre availability
  → power availability
  → optical safety constraints
  → maintenance access
  → environmental/heritage constraints
  → multi-hop resilience
  → AI-routing value
  → feasibility classification
```

No site receives a deployment recommendation until these fields are populated with authoritative GIS, meteorological, infrastructure and permission data.

## Initial experimental topology

Phase 1 should use a small closed testbed rather than a citywide deployment:

1. Two fixed optical nodes.
2. One weather/environmental sensor station.
3. Fibre or RF fallback.
4. Structured-light transmitter/receiver hardware.
5. AI telemetry collector.
6. Digital-twin simulation.
7. Controlled fog/turbulence testing where safe and lawful.
8. Outdoor line-of-sight test after laboratory validation.

Phase 2 can test a three-to-five-node mesh.

Phase 3 can evaluate selected Cape Town corridors using real GIS and meteorological datasets.

## CODEX modules

- `codex/photonics/fso_channel.py`
- `codex/photonics/structured_light.py`
- `codex/photonics/turbulence_eigenmodes.py`
- `codex/photonics/topological_encoding.py`
- `codex/network/fso_mesh.py`
- `codex/network/hybrid_optical_rf.py`
- `codex/ai/link_quality_predictor.py`
- `codex/ai/route_optimizer.py`
- `codex/digital_twin/cape_town_fso.py`
- `codex/gis/cpt_fso_site_screen.py`

These are planned module names until implemented and tested.

## Metamaterials cross-link

The existing MM research branch should be connected to the optical network through:

`MM → metasurface wavefront control → beam steering/phase control → structured light → FSO channel → AI optimisation`

Potential research questions include compact beam steering, optical coupling, adaptive wavefront control and receiver/transmitter packaging. These remain engineering hypotheses until supported by simulation and experiment.

## Research source network

Primary:
- Wits Optical Communication Lab
- Wits Structured Light research
- Wits WiredSpace repository

Secondary discovery:
- ResearchGate
- Emerald Insight

Technical/official cross-reference:
- NASA optical communications/metamaterials research where technically relevant
- public standards and South African regulatory material
- public/declassified historical technical archives where relevant

The repository must retain evidence classifications and must not treat discovery platforms such as ResearchGate as equivalent to peer-reviewed primary publications.

## Safety, regulation and deployment boundary

This architecture does not authorise deployment. Any physical optical network must undergo appropriate optical eye-safety assessment, aviation/airspace considerations where relevant, property/municipal permissions, telecommunications regulatory review, electrical safety review, cybersecurity review and environmental/heritage assessment where applicable.

No exact private rooftop or property is designated by this research record.

## Status

**Research architecture established.** Cape Town has been divided into candidate screening zones, Wits research has been integrated into the optical/AI network architecture, and a GIS/LOS/weather/AI site-selection workflow has been defined. Actual site selection remains pending authoritative geospatial, infrastructure, meteorological and permission data.
