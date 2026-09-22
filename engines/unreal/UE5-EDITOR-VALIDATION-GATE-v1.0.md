# UE5 Editor Validation Gate v1.0

## Objective
Move Biupiu from repository bootstrap into a repeatable local Unreal Editor validation workflow.

## Repository scope
- Project configuration for a deterministic bootstrap map.
- Content manifest for the first Digital Twin scene.
- Local validation checklist and evidence requirements.

## User environment
The user has an Epic Games account. Unreal Engine installation and licensing remain local to that account.

## Exit criteria
- Project opens in UE5.6.
- Both Biupiu plugins are discovered and load.
- Bootstrap map is available after content creation.
- BL-01 fixture can be replayed once the native runtime implementation is compiled locally.
- Development packaging is attempted and evidence recorded.

## Important boundary
GitHub integration can prepare source/configuration, but it cannot truthfully mark Unreal Editor compilation or runtime validation as passed without local UE execution.
