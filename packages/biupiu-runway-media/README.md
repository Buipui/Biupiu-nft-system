# Biupiu Runway Media Engine

Runway integration layer for the Biupiu R&D OS. This module treats Runway as an external media-generation provider rather than vendoring the Runway source repositories.

## Architecture
- **Provider adapter:** Runway API/SDK boundary.
- **Agent skills:** generation and workflow recipes are referenced from official Runway repositories.
- **Task queue:** async generation/polling/download lifecycle belongs behind the adapter.
- **Asset registry:** generated media should be recorded with provenance, model, prompt, source references and expiry/download status.
- **Clients:** Android and Windows invoke the shared runtime contract; secrets remain server-side.

## Official upstreams
- runwayml/skills — agent skills and generation workflows
- runwayml/runway-studio-skills — standalone Python media-generation skills
- runwayml/sdk-python — Python SDK
- runwayml/sdk-node — Node/TypeScript SDK
- runwayml/openapi — API specification
- runwayml/runway-api-mcp-server — MCP/API bridge
- runwayml/runway-mcp-plugin — hosted MCP integration

Do not copy credentials or generated media URLs into source control.
