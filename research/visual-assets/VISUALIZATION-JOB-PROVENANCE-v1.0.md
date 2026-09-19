# Biupiu Visualization Job Provenance v1.0

A visualization job is a reproducible record connecting an approved asset/material manifest to a render or video output.

## Required fields
- `job_id`
- `project_id`
- `asset_manifest_ids`
- `source_model_version`
- `authoring_application`
- `target_renderer`
- `renderer_version`
- `scene_version`
- `output_files`
- `created_at`
- `operator`
- `notes`

## Pipeline
Asset manifests → validation gate → scene assembly → renderer → output hash → provenance record.

## Promotion gates
1. Manifest exists.
2. Licence is verified.
3. Source model/version is identified.
4. Renderer/application versions are recorded.
5. Output file hash is recorded.
6. Render is labelled as visualisation, not engineering validation.
7. Material-performance claims link to separate measured/research evidence.

## Renderer targets
- Lumion
- Unreal Engine 5
- V-Ray
- Blender

## Digital Twin rule
A render can represent a Digital Twin state, but the render itself is not the authoritative Digital Twin state.