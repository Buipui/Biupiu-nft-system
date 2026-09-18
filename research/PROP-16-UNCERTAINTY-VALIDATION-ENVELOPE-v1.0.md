# PROP-16 — Uncertainty, Mission Priority & Validation Envelope v1.0

## Executed
Added the first uncertainty-propagation and validation-envelope utilities.

### Functions
- root-sum-square uncertainty propagation
- relative nominal/low/high bands
- validated-envelope flags
- mission test-priority scoring

### Interpretation
Priority is an engineering test-planning metric based on power/energy gap and uncertainty. It is not a product ranking.

### Digital-twin rule
A point cannot be flagged as within a validated envelope unless validated boundary data exists. In the absence of that evidence, the appropriate state remains `NO_VALIDATED_ENVELOPE`.

### Cross-discipline application
The utilities are designed for AUTO, MARINE, EVTOL, HELI and UAV mission records.

## PROP-17
Next gate:
- connect uncertainty to PROP-15 records;
- create explicit NO_VALIDATED_ENVELOPE handling;
- add planned-versus-measured comparison;
- generate anomaly records;
- update digital-twin state only when evidence thresholds are met;
- produce an experiment report dataset.
