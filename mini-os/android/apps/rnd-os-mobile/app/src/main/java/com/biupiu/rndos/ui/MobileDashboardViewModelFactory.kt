package com.biupiu.rndos.ui

import android.content.Context
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.biupiu.rndos.auth.DevSession
import com.biupiu.rndos.data.RndOsClientFactory

class MobileDashboardViewModelFactory(
    context: Context,
    private val session: DevSession?
) : ViewModelProvider.Factory {
    private val appContext = context.applicationContext

    @Suppress("UNCHECKED_CAST")
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if (modelClass.isAssignableFrom(MobileDashboardViewModel::class.java)) {
            return MobileDashboardViewModel(RndOsClientFactory.create(session)) as T
        }
        throw IllegalArgumentException("Unsupported ViewModel: " + modelClass.name)
    }
}