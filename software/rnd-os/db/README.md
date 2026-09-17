# Database Layer

The MVP currently uses `data/db.json` for zero-dependency local development.

`schema.sql` defines the planned PostgreSQL v0.2 persistence model, including:
- organisations and users
- projects
- research objects
- research-object relationships / knowledge graph edges
- experiments
- evidence records
- audit events

This schema is a migration target and is not yet connected to a live PostgreSQL server. Production use requires authentication, tenant isolation, migrations, backups, secret management and security review.
