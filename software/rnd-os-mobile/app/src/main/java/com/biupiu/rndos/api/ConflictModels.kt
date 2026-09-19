package com.biupiu.rndos.api

import kotlinx.serialization.Serializable

@Serializable
data class RecordRevision(
    val entityId:String,
    val version:Int,
    val contentHash:String,
    val updatedAt:String
)

@Serializable
data class ConflictResolution(
    val operationId:String,
    val strategy:String,
    val reason:String
)