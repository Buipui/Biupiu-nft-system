# Cape Town FSO / Light-Internet Pilot Test Plan v1.0

**Record:** BPU-NET-FSO-CPT-TEST-001  
**Status:** laboratory → controlled outdoor validation  
**Purpose:** convert the Cape Town network concept into measurable engineering experiments.

## Test gates

### Gate 1 — simulation
- atmospheric turbulence/channel model;
- structured-light mode comparison;
- optical power and BER budget;
- latency/throughput model;
- multi-hop topology simulation;
- AI link-quality prediction baseline.

### Gate 2 — laboratory
- transmitter/receiver alignment;
- structured-light encoding/decoding;
- turbulence emulator;
- controlled attenuation;
- conventional-link control;
- repeatability and deterministic logging.

### Gate 3 — controlled outdoor link
- approved site pair;
- documented line of sight;
- optical safety review;
- environmental sensors;
- fibre/RF fallback;
- continuous link telemetry.

### Gate 4 — multi-node pilot
- 3–5 nodes;
- dynamic route selection;
- weather-aware link prediction;
- structured-light adaptation;
- failover measurement;
- digital-twin comparison against observed data.

## Core measurements

- received optical power;
- BER / packet loss;
- throughput;
- latency and jitter;
- visibility;
- temperature/humidity/pressure;
- wind;
- alignment error;
- availability percentage;
- fallback activation frequency;
- AI prediction error;
- false failover / missed degradation events.

## Controls

Every structured-light or AI-enhanced experiment should have a conventional optical-control condition wherever practical. AI must be compared against a transparent non-AI baseline.

## Success criteria

No universal performance threshold is assumed in advance. Thresholds must be defined per experiment from the link budget, regulatory/safety requirements, application bandwidth and acceptable availability. Results must report uncertainty and environmental conditions.

## Cape Town data acquisition

Required datasets before physical site selection:

1. authoritative coordinates/elevation/building geometry;
2. line-of-sight obstruction model;
3. weather/visibility/fog observations;
4. wind statistics;
5. fibre/backhaul availability;
6. electrical power availability;
7. site ownership/permission status;
8. aviation and optical-safety constraints;
9. maintenance access;
10. environmental/heritage constraints.

## AI development sequence

`rules baseline → statistical predictor → supervised predictor → topology optimiser → digital twin → human-approved adaptive controller`

The AI layer must retain an audit trail of inputs, model version, confidence, action recommendation and observed outcome.

## Evidence boundary

A successful simulation is not an outdoor demonstration. An outdoor link is not a citywide network. A laboratory result is not proof of economic feasibility. Each stage must be independently documented.
