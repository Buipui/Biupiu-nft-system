package com.biupiu.rndos.ui

import com.biupiu.rndos.data.DashboardSnapshot

data class MobileDashboardState(
    val loading: Boolean = false,
    val dashboard: DashboardSnapshot? = null,
    val error: String? = null
)
