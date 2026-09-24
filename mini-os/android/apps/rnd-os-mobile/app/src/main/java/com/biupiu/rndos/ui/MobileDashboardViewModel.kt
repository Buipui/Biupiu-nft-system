package com.biupiu.rndos.ui

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.biupiu.rndos.data.RndOsApi
import kotlinx.coroutines.launch

class MobileDashboardViewModel(private val api: RndOsApi) : ViewModel() {
    var state: MobileDashboardState by mutableStateOf(MobileDashboardState())
        private set

    fun loadDashboard() {
        if (state.loading) return
        state = state.copy(loading = true, error = null)
        viewModelScope.launch {
            try {
                state = state.copy(loading = false, dashboard = api.dashboard(), error = null)
            } catch (error: Exception) {
                state = state.copy(loading = false, error = error.message ?: "API request failed")
            }
        }
    }

    fun clearError() {
        state = state.copy(error = null)
    }
}