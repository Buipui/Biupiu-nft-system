package com.biupiu.rndos.sync

interface OfflineQueue {
    fun enqueue(item: SyncItem)
    fun pending(): List<SyncItem>
    fun markSynced(itemId: String)
    fun markFailed(itemId: String)
}

class InMemoryOfflineQueue : OfflineQueue {
    private val items = linkedMapOf<String, SyncItem>()
    override fun enqueue(item: SyncItem) { items[item.id] = item.copy(state = "queued") }
    override fun pending(): List<SyncItem> = items.values.filter { it.state == "queued" || it.state == "failed" }
    override fun markSynced(itemId: String) { items[itemId]?.let { items[itemId] = it.copy(state = "synced") } }
    override fun markFailed(itemId: String) { items[itemId]?.let { items[itemId] = it.copy(state = "failed") } }
}
