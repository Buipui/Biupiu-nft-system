# Biupiu World — Web Hosting & Online Capability Test Plan v1.1

## Scope

This gate verifies repository-level readiness for a future Biupiu World web entry point. It does not claim that a public production host, domain, multiplayer runtime, WebXR session, WebRTC relay, or UE5 runtime is currently online.

## Test layers

1. **Repository integrity** — required web manifest, health contract, and CI workflow exist.
2. **Build/package integrity** — the repository web surface is packaged and required files are present.
3. **Hosting reachability** — when BIUPIU_WORLD_BASE_URL is configured, CI checks HTTPS reachability, redirect safety, the configured health path, and HSTS.
4. **Application health** — the health endpoint must return HTTP 200 and JSON containing status=ok.
5. **Realtime readiness** — WebSocket/WebRTC/WebXR remain architecture gates until a deployed runtime endpoint and browser/device test are supplied.

## Required environment values

- BIUPIU_WORLD_BASE_URL — optional deployed HTTPS origin, without a trailing slash.
- BIUPIU_WORLD_HEALTH_PATH — optional health path; defaults to /healthz.json.

## Pass criteria

- No secrets committed to the repository.
- Repository integrity/package checks complete successfully.
- If a base URL is supplied: HTTPS responds, redirects remain HTTPS, the health endpoint returns 200 with status=ok, and HSTS is present.
- Failure output identifies the exact layer; no failed or skipped test is promoted to VERIFIED.

## Current status

- Repository/CI readiness contract: IMPLEMENTED.
- CI execution for this gate: PENDING / NOT YET OBSERVED after the current changes.
- Public hosting reachability: NOT VERIFIED until BIUPIU_WORLD_BASE_URL is configured and the live probe passes.
- Live WebSocket/WebRTC/WebXR: NOT VERIFIED.
- UE5 runtime/editor launch: NOT VERIFIED by this repository workflow.

## Promotion states

IMPLEMENTED → TESTED → DEPLOYED → VERIFIED

A repository contract may be IMPLEMENTED without being TESTED in CI, and a deployed endpoint may be DEPLOYED without being VERIFIED until the live probe and relevant acceptance tests pass.

## Remaining modules

- Browser acceptance tests for desktop/mobile and later WebXR-capable devices.
- Authenticated gateway implementation.
- Live WebSocket adapter and server runtime.
- WebRTC relay where required.
- Observability backend and trace/audit ingestion.
- UE5 runtime/editor integration verification.
