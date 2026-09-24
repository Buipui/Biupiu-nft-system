package com.biupiu.rndos

import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertTrue

class LanguageSelectorTest {
    @Test fun preservesRegionAndScript() {
        assertEquals("pt-BR", BiupiuLanguageRegistry.normalise("pt_BR"))
        assertEquals("zh-Hant", BiupiuLanguageRegistry.normalise("zh-Hant"))
    }

    @Test fun rejectsUnknownLanguage() {
        assertTrue(!BiupiuLanguageRegistry.isSupported("xx"))
    }

    @Test fun fallbackIsDeterministic() {
        assertEquals(listOf("pt-BR", "pt", "en"), BiupiuLanguageRegistry.fallbackChain("pt-BR"))
    }
}
