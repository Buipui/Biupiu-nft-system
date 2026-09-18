# EXP-002 — Olla Irrigation Sensitivity Analysis

**Date:** 2026-09-18  
**Status:** Scenario analysis completed; field validation not performed  
**Classification:** Inconclusive for real-world performance

## Question
Under a simplified water-balance model, when could olla delivery offset estimated evaporative loss in a 1 m² plot over 30 days?

## Model
- Area: 1 m²
- Duration: 30 days
- Conversion: 1 mm of water over 1 m² = 1 litre
- Open-soil loss: `evaporation_mm_per_day × 30`
- Reduced loss: `open-soil loss × (1 − reduction factor)`
- Olla delivery: `olla_litres_per_day × 30`
- Balance: `olla delivery − reduced loss`
- Tested evaporation: 3, 5, and 7 mm/day
- Tested reduction factors: 0.40, 0.65, and 0.85
- Tested olla delivery: 1, 2, and 3 L/day

## Results
The model is highly sensitive to assumptions. At 5 mm/day evaporation and a 0.65 reduction factor, estimated reduced loss is 52.5 L over 30 days. Olla delivery of 1, 2, and 3 L/day produces 30, 60, and 90 L respectively, giving model balances of −22.5 L, +7.5 L, and +37.5 L.

Across the tested ranges:
- Higher evaporation increases the required water supply.
- Greater assumed reduction decreases the estimated requirement.
- Olla delivery of 1 L/day is insufficient in several scenarios.
- Olla delivery of 3 L/day exceeds modeled reduced loss in the tested scenarios except where evaporation is high and the assumed reduction is low.

## Interpretation
This analysis **does not prove olla irrigation effectiveness**. It shows that conclusions depend strongly on local evaporation, soil texture, vessel porosity, plant demand, weather, and actual delivery rate. The model can support planning of controlled trials, but cannot establish water savings or crop outcomes.

## Required validation
1. Measure soil moisture and olla delivery rate over time.
2. Compare olla plots with matched open-irrigated and control plots.
3. Record weather, soil type, crop stage, and irrigation volume.
4. Use repeated plots and report uncertainty.
5. Compare water use, plant health, biomass/yield, and root-zone moisture.

## Reproducibility
Run:

```bash
python experiments/digital-lab/EXP-002-olla-sensitivity-analysis.py
```

**Gate decision:** Proceed to a controlled bench/field protocol; do not treat this scenario model as empirical evidence.
