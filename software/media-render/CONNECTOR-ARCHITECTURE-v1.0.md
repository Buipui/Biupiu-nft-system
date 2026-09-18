# Media Connector Architecture v1.0

The R&D OS uses a provider-neutral adapter boundary.

```
R&D Object / Asset
       |
       v
Media Job API
       |
       +--> Blender
       +--> KeyShot
       +--> Twinmotion
       +--> Unreal Engine
       +--> Runway
       +--> Adobe Firefly
       +--> Premiere Pro
       +--> After Effects
```

## Connector responsibilities

Each connector should:

- accept a versioned render/media job
- resolve source assets
- record software/version metadata
- submit or prepare the job
- capture output references
- preserve provenance
- return status/errors
- never silently modify the authoritative research object

## Future implementation

Create provider adapters only after the corresponding application/API access is available. The current repository records the architecture and contracts first.
