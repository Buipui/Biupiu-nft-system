# Biupiu Farming System OS — Plant & Crop Catalogue Architecture

The OS is designed to grow into a selectable plant/crop catalogue.

## User flow
Select Plant/Crop -> Select Cultivar/Profile -> Select Growing Environment -> Connect Sensors -> Confirm Calibration -> Start Growth Cycle -> Monitor -> Optimise -> Record Outcome.

## Plant profile fields
- Plant ID
- Common name
- Scientific name
- Cultivar/variety (optional)
- Growth-stage definitions
- Environmental target ranges
- Sensor requirements
- Compatible Biupiu products
- Recommended experiment templates
- Water-management parameters
- Soil/substrate parameters
- Light parameters
- Known limitations
- Evidence level
- Profile version

## Product association
Each profile can expose a compatibility matrix:

Plant -> Stage -> Sensor -> Product -> Metric -> Recommendation -> Experiment -> Outcome.

This permits customers to start with a plant profile and then see which Biupiu devices can monitor the relevant variables.

## Governance
Profiles must be reviewed and versioned. Regional conditions, cultivar differences and measurement uncertainty must remain visible to the user.
