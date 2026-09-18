# @biupiu/firefly — Biupiu Adobe Firefly Integration

## Purpose

Provide a controlled Adobe Firefly Services integration boundary for the Biupiu R&D OS.

The package does **not** store Adobe credentials, call Firefly directly from mobile clients, or make the client an authority. It defines the shared contract that a secure server-side adapter can implement.

## Reusable Adobe components selected

### Required
- `@adobe/firefly-services-common-apis` — authentication/common utilities.
- `@adobe/firefly-apis` — Firefly product API client.

Adobe's current JavaScript SDK is TypeScript/Node.js based and separates Common, Firefly, Photoshop and Lightroom packages. Biupiu initially selects Common + Firefly; Photoshop and Lightroom remain optional downstream adapters.

### Useful Firefly capabilities

- Text-to-image generation
- Image expansion
- Generative fill
- Object/product compositing
- Similar-image generation
- Asset upload
- Image upscaling
- Asynchronous job handling

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
          +--> Adobe Firefly Services
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

The adapter should use environment/secret-manager configuration and return opaque job/output identifiers to clients.

## Provenance boundary

A generated asset should be associated with:
- Biupiu Project ID
- Research ID where applicable
- Firefly operation
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

Long-running generation should use a job model:
`QUEUED -> RUNNING -> SUCCEEDED/FAILED`.

The R&D OS can poll or later consume provider callbacks while retaining the provider job ID and audit event.

## Recommended first workflows

1. Product concept generation for Biupiu Showcase.
2. Environment/character concept generation for Biupiu World.
3. Product-shot compositing for prototype renders.
4. Controlled image expansion/fill for presentation assets.
5. Upscaling of approved render assets.
6. Research-art generation through a provenance-aware NFT Studio workflow.

## Explicit non-goals

- No credential storage in this package.
- No automatic publication to public galleries.
- No automatic NFT minting.
- No claim that generated images constitute scientific evidence.
- No replacement of Blender, Unreal, Twinmotion or KeyShot.
- No silent overwrite of source/research assets.

## Dependency policy

Use the official Adobe Firefly Services SDK as the primary implementation reference. Third-party Firefly clients/MCP servers may be evaluated separately but are not trusted dependencies by default.
