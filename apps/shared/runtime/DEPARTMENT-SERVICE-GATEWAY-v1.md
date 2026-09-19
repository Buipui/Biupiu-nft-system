# Biupiu Department Service Gateway v1

Gate 21 places an authorization boundary between department UI capabilities and service execution.

Main Hub → entitlement resolution → department authorization → service gateway → service adapter.

The gateway denies requests for departments not present in the authorized department set. The adapter remains responsible for reporting whether the underlying service is configured.

This is an application-layer boundary; production authorization must still be enforced server-side.
