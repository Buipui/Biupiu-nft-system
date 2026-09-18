package com.biupiu.rndos.sync

data class SyncItem(val id: String, val type: String, val payload: String, val createdAtEpochMs: Long, val state: String = "queued")
data class SyncResult(val itemId: String, val accepted: Boolean, val message: String)
