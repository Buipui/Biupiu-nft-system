# Gate 4 — Biupiu Subscriber Tier Architecture

Status: IMPLEMENTED
Date: 2026-09-18

## Purpose
Define subscription tiers independently from department permissions. A tier controls platform capability; a department entitlement controls which specialised resources a subscriber may access.

## Tier model

### TIER-0 — PUBLIC
- Main Hub public orientation
- Public civilisation/library metadata
- Public showcase content
- No protected simulations
- No private research access
- No department write access

### TIER-1 — EXPLORER
- Everything in PUBLIC
- Subscriber avatar/profile
- Guided world exploration
- Educational video/library access
- Basic simulations
- Progress tracking
- Department access only where an explicit department entitlement exists

### TIER-2 — BUILDER
- Everything in EXPLORER
- Full department simulations within entitled departments
- Advanced learning modules
- Virtual workshop/farm tools
- Expanded virtual inventory/economy
- Personal project workspace
- Save/export of permitted project records

### TIER-3 — RESEARCHER
- Everything in BUILDER
- Approved research sandbox tools
- Evidence/provenance tooling
- Experiment authoring and result logging
- Advanced simulation controls
- Cross-world research where explicitly entitled
- Research workspace access

### TIER-4 — CREATOR / DEVELOPER
- Everything in RESEARCHER
- Approved content authoring
- Environment/mod sandbox tools
- Digital asset pipeline
- Test NFT/mint workflow subject to release gates
- Developer/test APIs when provisioned
- No automatic production wallet or production mint authority

## Department entitlements

Tier and department are separate dimensions.

Supported department scopes:
- SMART_FARMING
- SMART_METAL_WORKSHOP
- FUTURE_DEPARTMENT

Examples:
- Explorer + SMART_FARMING = Farming Explorer
- Builder + SMART_METAL_WORKSHOP = Metal Workshop Builder
- Researcher + SMART_FARMING + SMART_METAL_WORKSHOP = cross-department Researcher, subject to explicit cross-world entitlement
- Creator/Developer does not automatically unlock every department

## Security model

1. Default deny.
2. Tier grants capabilities.
3. Department entitlement grants resource scope.
4. Role grants privileged tools.
5. Server/API remains authoritative.
6. Client cannot self-upgrade tier or entitlement.
7. Every protected action is auditable.
8. NFT release remains DRAFT -> REVIEW -> TESTNET -> VERIFIED -> RELEASED.

## Commercial flexibility

The tier system is deliberately capability-based rather than hard-coded to prices. Pricing, billing provider, regional currency and promotional offers can be attached later without changing the authorization model.

## Acceptance criteria

- Tiers and departments are independently represented.
- A higher tier does not silently grant unrelated department access.
- Department access can be added/revoked without changing a user's tier.
- Protected research and creation tools remain role-controlled.
- Production authorization is server-side.
