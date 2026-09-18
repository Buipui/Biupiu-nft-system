package com.biupiu.rndos.ai

/** Stable client/server contract for the R&D OS AI gateway. */
data class AiRequest(
    val task: String,
    val researchObjectId: String? = null,
    val evidenceSourceIds: List<String> = emptyList(),
    val datasetVersionIds: List<String> = emptyList()
)

data class AiResponse(
    val answer: String,
    val evidenceState: String,
    val citations: List<String> = emptyList(),
    val requestId: String? = null
)

data class AiError(
    val code: String,
    val message: String
)
