# Biupiu Department Service Registry v1

Gate 23 introduces a runtime registry for department services.

Each registration identifies the department, service ID, provider, adapter version, and executable adapter.

Flow:

Department request → registry resolution → subscriber entitlement gateway → service adapter.

A missing registration returns NOT_CONFIGURED. Registration does not grant access; subscriber entitlement remains authoritative.
