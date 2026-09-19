package com.biupiu.rndos.api

import kotlinx.serialization.Serializable

@Serializable
data class Session(val actorId:String,val role:String,val expiresAt:String)

@Serializable
data class SyncOperation(
    val operationId:String,
    val entityType:String,
    val payload:String,
    val baseVersion:Int=0,
    val createdAt:String
)

@Serializable
data class SyncConflict(
    val operationId:String,
    val entityId:String,
    val reason:String="VERSION_CONFLICT"
)