package com.biupiu.rndos.sync

interface SyncTransport { suspend fun upload(item: SyncItem): SyncResult }

class SyncEngine(private val queue: OfflineQueue, private val transport: SyncTransport) {
    suspend fun sync(): List<SyncResult> {
        val results = mutableListOf<SyncResult>()
        for (item in queue.pending()) {
            val result = transport.upload(item)
            if (result.accepted) queue.markSynced(item.id) else queue.markFailed(item.id)
            results += result
        }
        return results
    }
}
