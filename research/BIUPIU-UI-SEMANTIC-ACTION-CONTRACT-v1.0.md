# Biupiu UI Semantic Action Contract v1.0

Status: IMPLEMENTED ON AUDIT BRANCH — runtime/device verification pending

## Purpose

A visual control is not considered functional merely because it renders. Every interactive control must have a deterministic semantic route, an authority check, an execution/simulation boundary and visible feedback.

## Canonical action pipeline

INTENT -> ROUTE -> AUTHORISE -> VALIDATE -> EXECUTE_OR_SIMULATE -> OBSERVE -> FEEDBACK -> AUDIT

## Required button contract

Every button/action must declare:

- action ID;
- owning domain;
- target route/capability;
- authority requirement;
- enabled/disabled condition;
- handler;
- result code;
- visible success/error/blocked feedback;
- audit event where applicable.

## Fail-closed behaviour

Unknown or unbound actions must never silently do nothing.

They must return one of:

- UNKNOWN_CAPABILITY
- ACTION_NOT_IMPLEMENTED
- ACTION_BLOCKED
- REGISTERED_NOT_ENTITLED

and expose that state to the user.

## Simulation boundary

A simulator control must distinguish:

SIMULATED -> model/state change only
PHYSICAL -> authorised hardware actuation
BLOCKED -> no state mutation

The UI must never imply PHYSICAL execution when the backend is only a simulator or source-level adapter.

## Design-language enforcement

The contract inherits the unified Biupiu rule:

NEUTRAL BASE -> MATERIAL FINISH -> RESTRAINED NATURE ACCENT -> CLEAR INFORMATION

Decorative styling cannot change semantic meaning.

## Verification

Static source audit can establish route/handler presence and fail-closed behaviour. It cannot establish device rendering, UE5 runtime, external simulator execution or hardware actuation without those environments.
