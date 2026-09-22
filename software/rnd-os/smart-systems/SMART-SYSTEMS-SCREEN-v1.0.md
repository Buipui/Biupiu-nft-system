# Smart Systems Screen v1.0

## User-facing layout
The Smart Systems screen is the common control surface for connected Biupiu systems.

### Primary cards
- **System Status:** Online / Simulation / Physical / Fault / Maintenance
- **Current Gate:** G0–G8 with evidence state
- **Digital Twin:** model identity, last sync, provenance
- **Sensors:** live/sample state, freshness, quality
- **Rules & Intelligence:** active rules, AI recommendations, human approval state
- **Actuation:** requested vs confirmed state
- **Experiments:** active test, acceptance criteria and result
- **Audit:** latest changes, operator, timestamp and version
- **Next Gate:** explicit prerequisite checklist

### User flow
Select system → inspect status → inspect twin → review evidence → approve/execute allowed action → record result → advance or return to prior gate.

### Safety boundary
The UI must distinguish:
- simulated commands from physical commands
- recommendations from approved actions
- measured values from estimated values
- validated components from experimental components

No physical actuator should be controlled solely by an unverified recommendation.

## Reference architecture
Smart Farming is the baseline implementation pattern. Other domains plug into the same contracts through adapters rather than creating independent control architectures.
