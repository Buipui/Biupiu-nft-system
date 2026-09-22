# BIUPIU SYSTEM HIERARCHY + FEDERATION PROTOCOL v1.0
Status: IMPLEMENTED AT ARCHITECTURE LEVEL / RUNTIME VERIFICATION PENDING

## Core principle
Biupiu consists of distinct systems that are linked through contracts, identifiers and federation events. Linking does not collapse systems into one authority domain.

## Hierarchy
MAIN SYSTEM
  -> SUBSYSTEM
     -> COMPONENT
        -> MODULE
           -> INSTANCE

A subsystem may be mounted/represented inside another subsystem through the Digital Twin. Its canonical owner and parent hierarchy remain unchanged.

## Digital Twin
The Twin may compose:
- system A with subsystem B
- subsystem B with component C
- multiple contextual views of the same canonical subsystem

But every representation carries:
canonical_owner_id, canonical_parent_id, contextual_parent_id, subsystem_path.

The contextual parent does not become the canonical owner.

## Federation
Federation discovers, checks, links and reconciles independent systems. It must preserve identity, authority and hierarchy.

Federated fault finding:
1. detect event
2. correlate affected subsystem path
3. identify canonical owner
4. inspect dependency/contract/evidence state
5. isolate fault domain
6. generate healing proposal
7. validate against owning system
8. execute only under owning authority
9. observe result
10. record outcome and learning

Healing is therefore federated in diagnosis and knowledge, but authority remains local to the owning system.
