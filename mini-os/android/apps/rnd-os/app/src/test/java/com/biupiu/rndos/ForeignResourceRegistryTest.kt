package com.biupiu.rndos

import org.junit.Assert.assertTrue
import org.junit.Test

class ForeignResourceRegistryTest {
    @Test
    fun everyResourceHasAuthorityAndBoundary() {
        assertTrue(ForeignResourceRegistry.modules.isNotEmpty())
        assertTrue(ForeignResourceRegistry.modules.all { it.authority.isNotBlank() && it.integrationBoundary.isNotBlank() })
    }

    @Test
    fun vendorResourcesRemainNonExecutableReferences() {
        assertTrue(ForeignResourceRegistry.modules.none { it.id.contains("blob") && it.runtimeVerified })
    }

    @Test
    fun multilingualHarvestHasMultipleLanguageLanes() {
        val languages = ForeignResourceRegistry.modules.flatMap { it.languages }.toSet()
        assertTrue(languages.size >= 6)
    }
}
