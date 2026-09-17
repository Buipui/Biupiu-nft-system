# Biupiu R&D OS — MVP 0.2

A dependency-free local prototype of the Biupiu Research & Development Operating System.

## Implemented in v0.2

- Dashboard and Research Control Centre UI
- Project, research-object, hypothesis, experiment, failure and IP registries
- Evidence-state and R0–R9 maturity fields
- JSON development datastore behind a storage abstraction
- PostgreSQL-ready relational schema in `db/schema.sql`
- Relationship registry and graph API
- Research lineage endpoint
- Lifecycle transition validation
- Research package export with SHA-256 integrity checksum
- Non-production authentication/role primitives
- Audit-event generation
- Search API
- Seeded Biupiu pilot project
- Automated Node.js test suite
- GitHub Actions CI workflow

## Run

Requires Node.js 20+.

```bash
npm start
```

Open `http://localhost:3000`.

Run tests:

```bash
npm test
```

Export the current development database as an integrity-checked research package:

```bash
npm run package:export
```

## API

`GET /api/health`
`GET /api/meta`
`GET /api/dashboard`
`GET /api/search?q=...`
`GET|POST /api/projects`
`GET|POST /api/research`
`GET|POST /api/hypotheses`
`GET|POST /api/experiments`
`GET|POST /api/failures`
`GET|POST /api/ip`
`GET /api/graph`
`GET /api/research/:id/lineage`
`POST /api/research/:id/transition`
`GET|POST /api/relationships`
`GET /api/package/export`
`POST /api/package/import` (validation-only in v0.2; it does not overwrite the datastore)

## Architecture status

v0.2 remains a development foundation, not a production SaaS, regulated laboratory information system, security-certified platform or validated scientific instrument. PostgreSQL is modelled but not yet connected at runtime. Authentication primitives are scaffolding, not production identity/security. Production deployment requires security review, database hardening, real identity management, tenant isolation, backups, privacy controls, observability, rate limiting and independent workflow validation.

The software uses the lifecycle:

`SOURCE → CLAIM → HYPOTHESIS → MODEL → SIMULATION → EXPERIMENT → MEASUREMENT → VALIDATION → REPLICATION → IP → PROTOTYPE → PRODUCT`
