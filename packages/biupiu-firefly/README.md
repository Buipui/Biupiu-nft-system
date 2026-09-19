# @biupiu/firefly — Biupiu Adobe Firefly Integration

## Purpose

Provide a controlled Adobe Firefly Services integration boundary for the Biupiu R&D OS.

The package does **not** store Adobe credentials, call Firefly directly from mobile clients, or make the client an authority. It defines the shared contract that a secure server-side adapter can implement.

## Current Adobe API source

The repository is aligned to Adobe's current Firefly OpenAPI specification:

- OpenAPI: 3.1.0
- Firefly API version: 3.0.0
- Production base URL: `https://firefly-api.adobe.io`
- Current image generation includes Image3, Image4 variants and Image5.
- Current access failures expose `x-access-error` values including entitlement, profile, quota and IMS-scope failures.

The Adobe-supplied OpenAPI specification is treated as the API contract. Account entitlement and credentials remain a separate runtime concern.

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
          +--> Adobe IMS authentication (server side)
          |
          +--> Adobe Firefly API
          |
          v
Asset / Job Result
          |
          +--> R&D provenance
          +--> Digital Twin / Showcase
          +--> NFT Studio (release-gated)
          +--> Research Library
```

## Security boundary

Adobe Client ID and Client Secret must remain server-side. Never put them in Android, browser bundles, public GitHub files or NFT metadata.

The adapter uses environment/secret-manager configuration and returns opaque job/output identifiers to clients.

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

## Recommended first workflows

1. Product concept generation for Biupiu Showcase.
2. Environment/character concept generation for Biupiu World.
3. Product-shot compositing for prototype renders.
4. Controlled image expansion/fill for presentation assets.
5. Upscaling of approved render assets.
6. Research-art generation through a provenance-aware NFT Studio workflow.
7. Video concept generation for controlled showreel previsualization.

## Explicit non-goals

- No credential storage in this package.
- No automatic publication to public galleries.
- No automatic NFT minting.
- No claim that generated images constitute scientific evidence.
- No replacement of Blender, Unreal, Twinmotion or KeyShot.
- No silent overwrite of source/research assets.

## Dependency policy

Use the official Adobe Firefly Services SDK and Adobe OpenAPI specification as the primary implementation references. Third-party Firefly clients/MCP servers may be evaluated separately but are not trusted dependencies by default.

## Server-side API configuration

The repository includes `src/auth.ts` and `firefly.env.example` for Adobe IMS OAuth Server-to-Server authentication.

Configure these values in the **server/hosting environment**, never in Android/Windows client bundles or committed files:

- `FIREFLY_SERVICES_CLIENT_ID`
- `FIREFLY_SERVICES_CLIENT_SECRET`
- `FIREFLY_SERVICES_TOKEN_URL` (defaults to Adobe IMS)
- `FIREFLY_SERVICES_SCOPE` (defaults to the Firefly Services scope set)

The auth module caches the access token until shortly before expiry and never logs the client secret or access token.

**Live API status:** repository-side integration is prepared, but a live call still requires valid Adobe credentials and the account's applicable Firefly API access/entitlement. The Adobe OpenAPI specification does not itself grant access.
