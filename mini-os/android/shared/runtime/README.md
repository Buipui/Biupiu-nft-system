# Biupiu Shared Runtime v1

Gate 10 connects the Android and Windows application shells to one runtime contract.

## Flow

Subscriber context → entitlement resolution → Main Hub → department route.

The runtime deliberately treats client state as presentation/local state. Production authorization and persistent subscriber state remain server-side responsibilities.

## Cross-client rule

Android and Windows must produce the same route decision for the same subscriber context.

## Current routes

- MAIN_HUB
- SMART_FARMING
- SMART_METAL_WORKSHOP
- RND_OS

This is the runtime foundation; native UI and live API integration are subsequent gates.
