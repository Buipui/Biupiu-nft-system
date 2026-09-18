# Biupiu Unreal MCP Layer

This package defines the Biupiu R&D OS integration boundary for Unreal MCP tooling.

## Architecture
Biupiu R&D OS -> Unreal MCP adapter -> Unreal-MCP-Ultra -> Unreal Engine 5 editor -> Digital Twin / simulation / visualization

The adapter is intentionally source-independent. Upstream Unreal-MCP-Ultra remains a separate GitHub project.

## Why this matters
This allows Biupiu to track compatible UE versions without creating an embedded Unreal fork, while preserving a clean IP/licensing boundary.

## Upstream reference
PR #5 provides the current dual-engine compatibility groundwork for UE 5.6.1 and UE 5.8.1. See UNREAL-MCP-ULTRA-INTEGRATION.md and compatibility/UE56-UE58-MATRIX.md.

## Next validation gate
Run the same representative MCP workflow against both installed engines:
- start editor
- load plugin
- start MCP server
- enumerate/register tools
- create/read/mutate a test Blueprint
- create/read a DataAsset/UserDefinedStruct
- validate a material
- run PIE
- capture output

Record actual results in the matrix before promoting an engine to verified.
