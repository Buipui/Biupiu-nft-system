package com.biupiu.rndos.ui

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.biupiu.rndos.data.RndOsApi
import kotlinx.coroutines.launch

class MobileDashboardViewModel(private val api: RndOsApi) : ViewModel() {
    var state = MobileDashboardState()
        private set
    fun loadDashboard() {
        state = state.copy(loading = true, error = null)
        viewModelScope.launch {
            try { state = state.copy(loading = false, dashboard = api.dashboard()) }
            catch (error: Exception) { state = state.copy(loading = false, error = error.message ?: "API request failed") }
        }
    }
}
