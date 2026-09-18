# Provider Adapter Guide

Adapters normalize provider-specific execution behind one RenderJob contract.

## Deterministic 3D
Blender, Unreal Engine 5, Twinmotion and KeyShot remain authoritative for scene/model rendering.

## Post/generative
Adobe handles editorial/post workflows; Firefly and Runway handle generative variations and motion/audio workflows.

## Security
Credentials and provider API calls stay server-side. Clients submit authorized jobs and receive status/output asset references.

## Provenance
Every derivative output must retain source asset IDs, source model version, provider and provider job ID when available.