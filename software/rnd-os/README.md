# Biupiu R&D OS — MVP 0.1

A dependency-free local prototype of the Biupiu Research & Development Operating System.

## What is implemented

- Dashboard and Research Control Centre UI
- Project, research-object, hypothesis, experiment, failure and IP registries
- Evidence-state and R0–R9 maturity fields
- JSON persistence for the development prototype
- Audit-event generation for new records
- Search API
- Relationship graph API
- Research-object JSON Schema
- Seeded Biupiu pilot project
- Node.js built-in test suite

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

## API

`GET /api/health`
`GET /api/dashboard`
`GET /api/search?q=...`
`GET|POST /api/projects`
`GET|POST /api/research`
`GET|POST /api/hypotheses`
`GET|POST /api/experiments`
`GET|POST /api/failures`
`GET|POST /api/ip`
`GET /api/graph`

## Architecture status

This is an MVP development foundation, not a production SaaS system. The next engineering stages should replace JSON persistence with PostgreSQL, add authentication/tenant isolation, stronger validation, permissions, encrypted secrets, background jobs, immutable audit storage, production observability, and connectors for simulation, AI, digital twins and manufacturing systems.

The software is based on the repository's R&D OS architecture and uses the lifecycle:

`SOURCE → CLAIM → HYPOTHESIS → MODEL → SIMULATION → EXPERIMENT → MEASUREMENT → VALIDATION → REPLICATION → IP → PROTOTYPE → PRODUCT`
