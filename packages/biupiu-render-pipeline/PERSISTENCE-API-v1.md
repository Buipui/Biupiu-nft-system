# Render Persistence and Service API v1

Render jobs are created and tracked through a server-authoritative service boundary.

The repository interface can later be backed by PostgreSQL, SQLite or another approved persistence layer without changing client contracts.

Every job keeps source asset IDs, source model version, provider, workflow, state, output references and provenance. Terminal failures remain queryable.

jobId is the idempotency key; clients cannot directly mutate persistent job state.