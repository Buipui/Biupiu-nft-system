# Gate 11 — Main Hub Runtime UI Contract

The Main Hub is the canonical navigation surface for the Biupiu OS.

## Startup

1. Load subscriber session.
2. Resolve entitlement state.
3. Build hub destinations.
4. Render ENTERABLE or LOCKED cards.
5. Navigate only when the runtime returns ENTERABLE.

## Initial destinations

- Farming World → SMART_FARMING
- Metal Making World → SMART_METAL_WORKSHOP
- R&D OS → RND_OS

The UI is a client presentation layer. It must not be treated as the final authorization boundary.
