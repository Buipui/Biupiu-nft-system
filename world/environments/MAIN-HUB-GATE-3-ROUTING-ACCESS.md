# Gate 3 — Main Campus Hub Routing & Department Access

Status: IMPLEMENTED
Date: 2026-09-18

## Objective

Turn the Main Campus Hub into the canonical entry point for the Biupiu World while preserving department separation.

Flow:

Avatar Arrival -> Main Campus Hub -> Shared Services -> Destination Gate -> Department World -> Campus -> Restricted resources

## Canonical destinations

### Farming World
Department scope: SMART_FARMING

Includes:
- regenerative farming
- historical farming environments
- smart-farming simulations
- water/soil/crop systems
- farming research and learning resources

### Metal Making World
Department scope: SMART_METAL_WORKSHOP

Includes:
- metallurgy resources
- home/hobby workshop learning
- historical metalworking environments
- materials laboratory
- metallurgy simulations and research resources

## Access model

The hub is shared. Department resources are not.

A subscriber may:
1. enter the Main Hub;
2. view public/shared navigation and library metadata;
3. see which departments their account can enter;
4. enter only authorised department resources;
5. retain the same avatar/profile identity across worlds.

The client must never be treated as the final authorization authority. Production authorization belongs to the server/API layer defined by Gate 2.

## Required control checks

- destination scope check
- resource scope check
- subscriber entitlement check
- provenance/evidence visibility check
- audit event on protected-resource entry
- deny-by-default for unknown scopes

## Historical integrity

The Main Hub may link to historical environments, but historical reconstruction, scholarly interpretation and Biupiu experimental/R&D content remain explicitly labelled.

## Acceptance criteria

- Farming and Metal Making remain separate first-class destinations.
- A Farming-only subscriber cannot silently access Metal Making protected resources.
- A Metal Making-only subscriber cannot silently access Farming protected resources.
- Shared hub services remain available according to their own access policy.
- Cross-world learning is possible only where the entitlement policy explicitly permits it.
- Routing and access decisions are represented as versioned data, not hard-coded UI assumptions.
