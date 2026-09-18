# AI-02 — Repository RAG Foundation

## Status
Implemented as a deterministic development foundation.

## Pipeline
USER TASK → REPOSITORY RETRIEVAL → EVIDENCE CONTEXT → AI PROVIDER → STRUCTURED RESULT

The retrieval interface currently performs deterministic local Markdown retrieval. This creates a testable boundary before introducing embeddings/vector storage.

## Evidence rule
Retrieved text is context, not automatically verified truth. Each result retains a source identifier and evidence-state field.

## Next implementation
Replace or augment the deterministic retriever with embeddings/vector search, chunk metadata, source provenance, incremental indexing and API authentication. Connect the Android AI Gateway after the server boundary is established.
