# BIUPIU MULTI-PROVIDER AI EXPANSION REGISTER v1.0

Date: 20 September 2026
Status: REGISTERED / INTEGRATION ARCHITECTURE UPDATED

## Providers added

### Anthropic / Claude
Repositories:
- anthropics/claude-agent-sdk-python — MIT
- anthropics/claude-agent-sdk-typescript — public SDK
- anthropics/sandbox-runtime — Apache-2.0
- anthropics/claude-code — public agentic coding tool

Biupiu routes:
AGENT ORCHESTRATION, CODING, SANDBOX, TOOL USE, MCP, REPOSITORY, EVALUATION.

The sandbox-runtime is especially relevant to the existing Biupiu security/housekeeping architecture because it provides filesystem and network restriction mechanisms for processes without requiring a container.

### DeepSeek
Repositories:
- deepseek-ai/DeepSeek-V3 — MIT
Official API now supports current V4 family and OpenAI Responses-compatible access.

Current research route:
REASONING, CODE AGENTS, MATHEMATICS, MULTIMODAL, LOCAL/OPEN-MODEL RESEARCH, CROSS-MODEL EVALUATION.

DeepSeek V4.1-Flash currently exposes native multimodal capability through the API. DeepSeek V4-Pro and V4-Flash also support Responses-format integration, including Codex-compatible workflows.

### xAI / Grok
Repositories:
- xai-org/xai-sdk-python — Apache-2.0
- xai-org/xai-proto — Apache-2.0
- xai-org/grok-1 — Apache-2.0
- xai-org/grok-build — Apache-2.0
- xai-org/xai-cookbook — public examples

Biupiu routes:
MULTI-MODEL, AGENTIC CODING, TEXT, IMAGE, VIDEO, BATCH, gRPC, MODEL COMPARISON.

The xAI API exposes Chat, Image, Video, Batch Management, Models, Auth, Tokenize and Sampling services through its public API surface.

### Moonshot AI / Kimi
Repositories:
- MoonshotAI/kimi-agent-sdk — Apache-2.0
- MoonshotAI/Kimi-K3 — licence requires separate review
- Attention-Residuals and related Kimi research repositories
- Mooncake serving architecture

Biupiu routes:
LONG-CONTEXT, AGENTIC CODING, MULTIMODAL, REASONING, MODEL-SERVING, DISTRIBUTED INFERENCE, MCP.

Kimi Agent SDK supports external tools, MCP configuration, sessions, skills, model capability declarations and multiple provider types. It therefore maps particularly well onto the Biupiu provider-neutral gateway.

## Unified provider abstraction

BIUPIU INTELLIGENCE GATEWAY

OPENAI / CODEX
ANTHROPIC / CLAUDE
GOOGLE / GEMINI
DEEPSEEK
META / LLAMA
XAI / GROK
MOONSHOT / KIMI
LOCAL / OPEN-WEIGHT MODELS
SPECIALIST MODELS

All providers terminate at the same neutral interface:

TASK
-> EVIDENCE SET
-> PROVIDER ADAPTER
-> MODEL
-> TOOL/MCP PLAN
-> OUTPUT
-> FACT/CITATION EXTRACTION
-> CROSS-MODEL CHECK
-> SAFETY/LICENCE CHECK
-> VALIDATION
-> PROVENANCE
-> LEARNING RECORD

## Provider-selection rule

Biupiu Intelligence does not permanently assign one provider to all tasks.

A task may be routed according to:
- capability requirements
- latency
- context requirements
- modality
- local/offline requirement
- mathematical/reasoning requirement
- code-generation requirement
- tool-use requirement
- privacy/security classification
- cost
- licence/redistribution constraints
- validation history

Provider disagreement is preserved as an explicit contradiction/uncertainty record rather than silently averaged.

## Integration boundary

Implemented now:
- provider inventory
- repository references
- licence classification
- capability mapping
- adapter architecture
- security boundary
- cross-model evaluation route

Not claimed:
- API keys connected
- production provider calls
- autonomous provider switching
- automatic model-weight import
- redistribution of provider-restricted models
- production deployment

## Promotion gates

REFERENCE
-> LICENCE-CHECKED
-> SECURITY-CHECKED
-> SANDBOXED
-> BENCHMARKED
-> COMPATIBILITY-VERIFIED
-> HUMAN-APPROVED
-> ACTIVE MODULE

External proprietary services remain behind adapters. Public SDKs/examples can be incorporated only where their licences permit.

## Next gate

AI-30:
Create concrete provider adapter manifests for OpenAI, Anthropic, Gemini, DeepSeek, Meta/Llama, xAI and Moonshot/Kimi, including:
- API/interface
- model identifiers
- modality
- context
- tools/MCP
- licence
- dependency provenance
- security class
- evaluation suite
- fallback provider
- failure/contradiction handling
- activation state.
