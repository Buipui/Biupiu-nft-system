# Biupiu Main Intelligence Control (MIC) v1.0

## Role

MIC is the central policy and orchestration layer through which Biupiu DMS modules obtain identity context, authorization decisions, entitlement state, site scope and audit correlation.

MIC is an architecture name, not a claim of autonomous intelligence. AI services remain bounded by explicit permissions, policies and human administrative authority.

## Core services

- Identity and authentication
- Role/profile resolution
- Organization/site/device scope
- Policy decision point
- Subscription entitlement resolution
- Feature-gate state
- Session/token lifecycle
- Audit correlation
- Cross-module event routing
- Administrative approvals
- Security alerts
- Configuration/version control

## Control path

Login -> Authentication -> Profile -> Scope -> MIC policy evaluation -> Entitlement evaluation -> Module authorization -> Audit event -> Session.

For sensitive operations:

Request -> MIC -> policy + role + entitlement + scope -> allow/deny -> module -> audit.

## Centralization rule

Department applications may cache short-lived authorization/entitlement state for resilience, but the central DMS/MIC remains authoritative. Cached state must have an explicit expiry and revocation strategy.

## Future intelligence layer

Analytics and AI can recommend actions, detect anomalies and summarize operations, but policy-sensitive changes require appropriate human authorization. AI services do not receive ROOT privileges by default.
