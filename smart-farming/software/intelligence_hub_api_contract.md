# Biupiu Intelligence Hub ↔ Farming OS API Contract v0.1

## POST /v1/observations
Receives validated sensor observations.

## POST /v1/cycles
Starts or updates a plant growth cycle.

## POST /v1/experiments
Creates a testable experiment and hypothesis.

## GET /v1/plants
Returns available plant profiles.

## GET /v1/plants/{plant_id}
Returns profile, stages, required metrics and compatible Biupiu products.

## GET /v1/plants/{plant_id}/protocols
Returns optimisation protocols whose evidence level and conditions match the request.

## POST /v1/advisories
Requests an advisory from the Intelligence Hub using the supplied observations and plant-cycle context.

## POST /v1/results
Records measured outcomes, interventions and experiment conclusions.

## Safety contract
The API may return recommendations and proposed actions. The Farming OS must enforce local limits, permissions, hardware interlocks and manual approval requirements before an actuator is allowed to operate.
