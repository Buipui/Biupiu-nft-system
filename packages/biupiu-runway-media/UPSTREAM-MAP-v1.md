# Runway Upstream Map v1

| Upstream | Biupiu use | Treatment |
|---|---|---|
| runwayml/skills | agent-facing generation/integration skills | reference/integrate, do not vendor |
| runwayml/runway-studio-skills | standalone Python image/video/audio scripts | reference or selectively adapt |
| runwayml/sdk-python | server-side Python adapter | dependency |
| runwayml/sdk-node | Node/TypeScript service adapter | dependency option |
| runwayml/openapi | API contract/model validation | upstream reference |
| runwayml/runway-api-mcp-server | MCP bridge | optional deployment adapter |
| runwayml/runway-mcp-plugin | hosted MCP + workflow UX | optional external integration |

## Biupiu cross-discipline uses
- product-development showreels
- digital-twin cinematic previews
- marine / eVTOL / helicopter / microturbine concept visualization
- character/environment presentation
- research visualization and controlled concept iteration

## Gate decision
Integrate a **thin provider module and contracts**, not the full upstream repositories. This keeps the Biupiu repository maintainable and avoids coupling the core R&D OS to Runway implementation details.
