# Biupiu World — Web Hosting & Online Capability Test Plan v1.0

## Scope

This gate verifies repository-level readiness for a future Biupiu World web entry point. It does not claim that a public production host, domain, multiplayer runtime, WebXR session, WebRTC relay, or UE5 runtime is currently online.

## Test layers

1. **Repository integrity** — required web manifest, health endpoint contract, and CI workflow exist.
2. **Build integrity** — JavaScript/TypeScript packages and Hardhat contracts compile and tests run where dependencies are available.
3. **Hosting reachability** — optional `BIUPIU_WORLD_BASE_URL` is checked for DNS/TLS/HTTP response and security headers.
4. **Application health** — optional `/healthz` endpoint must return HTTP 200 and JSON containing `status=ok`.
5. **Realtime readiness** — WebSocket/WebRTC/WebXR are architecture gates only until a deployed runtime endpoint and browser/device test are supplied.

## Required environment values

- `BIUPIU_WORLD_BASE_URL` — deployed HTTPS origin, without a trailing slash.
- `BIUPIU_WORLD_HEALTH_PATH` — optional path; defaults to `/healthz`.

## Pass criteria

- No secrets committed to the repository.
- Build/test jobs complete successfully.
- If a base URL is supplied: HTTPS responds, health endpoint returns 200, and no redirect downgrades to HTTP.
- Failure output identifies the exact layer; no failed or skipped test is promoted to VERIFIED.

## Current status

- Repository/CI inspection: **OBSERVED**.
- Public hosting reachability: **NOT VERIFIED** until `BIUPIU_WORLD_BASE_URL` is configured.
- Live WebSocket/WebRTC/WebXR: **NOT VERIFIED**.
- UE5 runtime/editor launch: **NOT VERIFIED by this repository workflow**.

## Missing modules identified

- Hosting health probe and security-header probe.
- Environment-safe deployment manifest.
- Web client shell / landing entry point.
- Authenticated gateway contract with server-side authority.
- Realtime transport adapter contract (WebSocket first; WebRTC optional).
- Observability: uptime, latency, error rate, trace/correlation ID and audit events.
- CI promotion rules separating `IMPLEMENTED`, `TESTED`, `DEPLOYED`, and `VERIFIED`.
- Browser acceptance tests for desktop/mobile and later WebXR-capable devices.
