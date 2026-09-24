# Biupiu R&D OS Mobile Architecture v0.8

**Date:** 18 September 2026

## v0.8 objective
Connect the existing Android foundation to the future authenticated R&D OS API and AI Gateway while preserving the v0.7 separation between mobile client and core datastore.

## Screens
- Dashboard
- Research Objects
- Experimental Control Centre
- AI Research Assistant
- Experiment Capture
- Evidence/Results
- Sync status

## Data flow
Android → HTTPS API → Auth boundary → R&D OS Core / AI Gateway → repository, experiment store and simulation services.

## Offline-first direction
The mobile client should queue drafts, experiment observations and evidence attachments locally, then synchronise through explicit API operations. Conflict handling must preserve audit history.

## AI interaction
AI requests are structured around research-object IDs, evidence context and user intent. The app displays whether returned content is fact, hypothesis, simulation output or interpretation.

## Security
No database credentials in the APK. Tokens are stored using Android secure storage. Production authentication, certificate strategy and threat modelling remain future gates.
