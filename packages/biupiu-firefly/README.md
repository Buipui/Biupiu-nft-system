# @biupiu/firefly — Biupiu Adobe Firefly Integration

## Purpose

Provide a controlled Adobe Firefly Services integration boundary for the Biupiu R&D OS.

The package does **not** store Adobe credentials, call Firefly directly from mobile clients, or make the client an authority. It defines the shared contract that a secure server-side adapter can implement.

## Current Adobe API release lock

The repository is locked to Adobe's current Firefly OpenAPI release supplied through the official AdobeDocs repository:

- OpenAPI: 3.1.0
- Firefly API version: 3.0.0
- Production base URL: `https://firefly-api.adobe.io`
- Source: `AdobeDocs/ffs-firefly-api/static/firefly-api.json`
- Source URL: `https://raw.githubusercontent.com/AdobeDocs/ffs-firefly-api/main/static/firefly-api.json`

The credential-free gate validates this API contract and repository integration without attempting authentication or making a live generation request. Credentials are therefore **not required to inspect, validate, or smoke-test these updated API files**.

A live authenticated provider call is a separate runtime stage. The adapter retains a server-side authentication boundary for that stage because the current Adobe OpenAPI security declaration includes both `X-Api-Key` and `AccessToken`.

## Reusable Adobe components selected

### Required
- `@adobe/firefly-services-common-apis` — authentication/common utilities.
- `@adobe/firefly-apis` — Firefly product API client.

Adobe's JavaScript SDK is TypeScript/Node.js based and separates Common, Firefly, Photoshop and Lightroom packages. Biupiu initially selects Common + Firefly; Photoshop and Lightroom remain optional downstream adapters.

### Firefly capabilities routed by this package

- Image generation
- Image5 generation
- Image expansion
- Generative fill
- Object/product compositing
- Precise/adaptive compositing
- Similar-image generation
- Image upscaling
- Video generation
- Asset upload
- Asynchronous job/status handling
- Job cancellation

## Credential-free static gate

Run:

`node packages/biupiu-firefly/smoke-test.mjs`

This test performs source/contract checks only. It does **not** contact Adobe, request a token, require an API secret, or generate an asset.

## Biupiu integration path

```text
Biupiu Android / Windows / Web
          |
          v
Biupiu API Gateway
          |
          v
@biupiu/firefly
          |
          +--> Adobe Firefly API contract
          |
          +--> Optional live server authentication
          |
          v
Asset / Job Result
          |
          +--> R&D provenance
          +--> Digital Twin / Showcase
          +--> NFT Studio (release-gated)
          +--> Research Library
```

## Provenance boundary

A generated asset should be associated with:
- Biupiu Project ID
- Research ID where applicable
- Firefly operation
- model version where applicable
- prompt
- reference/source asset IDs
- provider
- job ID
- output asset ID
- generation timestamp
- output hash
- software/provider version information
- applicable licence/IP classification

Generated assets must be new records; they must not overwrite research source files.

## Async execution

Long-running generation uses a job model:
`QUEUED -> RUNNING -> SUCCEEDED/FAILED`.

The R&D OS can poll provider job status while retaining the provider job ID and audit event.

## Access-error handling

The current Adobe API contract exposes these access-related signals:

- `quota_exhausted`
- `user_non_entitled`
- `user_profile_denied`
- `invalid_ims_scope`

These are surfaced by the adapter rather than converted into a misleading generic failure.

## Explicit non-goals

- No credential storage in this package.
- No automatic publication to public galleries.
- No automatic NFT minting.
- No claim that generated images constitute scientific evidence.
- No replacement of Blender, Unreal, Twinmotion or KeyShot.
- No silent overwrite of source/research assets.

## Dependency policy

Use the official Adobe Firefly Services SDK and Adobe OpenAPI specification as the primary implementation references. Third-party Firefly clients/MCP servers may be evaluated separately but are not trusted dependencies by default.

## Server-side live API configuration

The repository includes `src/auth.ts` for the optional live authenticated runtime.

Configure these values only in the server/hosting environment when the live provider stage is enabled:

- `FIREFLY_SERVICES_CLIENT_ID`
- `FIREFLY_SERVICES_CLIENT_SECRET`
- `FIREFLY_SERVICES_TOKEN_URL`
- `FIREFLY_SERVICES_SCOPE`

Never put secrets in Android/browser bundles, committed files, NFT metadata, or the credential-free smoke test.
