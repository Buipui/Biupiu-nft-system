package com.biupiu.rndos.ui

import kotlin.test.Test
import kotlin.test.assertFalse
import kotlin.test.assertNull

class MobileDashboardStateTest {
    @Test
    fun defaultStateStartsEmpty() {
        val state = MobileDashboardState()
        assertFalse(state.loading)
        assertNull(state.dashboard)
        assertNull(state.error)
    }
}