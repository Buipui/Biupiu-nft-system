package com.biupiu.rndos

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.biupiu.rndos.auth.AuthViewModel
import com.biupiu.rndos.auth.AuthViewModelFactory
import com.biupiu.rndos.ui.AuthScreen
import com.biupiu.rndos.ui.MobileDashboardViewModel
import com.biupiu.rndos.ui.MobileDashboardViewModelFactory

class MainActivity : ComponentActivity() {
    private val authViewModel: AuthViewModel by viewModels { AuthViewModelFactory(applicationContext) }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { BiupiuRndOsApp(authViewModel) }
    }
}

@Composable
fun BiupiuRndOsApp(authViewModel: AuthViewModel) {
    MaterialTheme {
        Surface(Modifier.fillMaxSize()) {
            val auth = authViewModel.state
            if (!auth.authenticated || auth.session == null) {
                AuthScreen(authViewModel)
            } else {
                val dashboardViewModel: MobileDashboardViewModel = viewModel(
                    key = "dashboard-${auth.session.userId}-${auth.session.organisationId}",
                    factory = MobileDashboardViewModelFactory(LocalContext.current, auth.session)
                )
                DashboardRoute(dashboardViewModel, authViewModel)
            }
        }
    }
}

@Composable
private fun DashboardRoute(viewModel: MobileDashboardViewModel, authViewModel: AuthViewModel) {
    LaunchedEffect(Unit) { viewModel.loadDashboard() }
    val state = viewModel.state
    Column(Modifier.fillMaxSize().padding(24.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
        Text("Biupiu R&D OS", style = MaterialTheme.typography.headlineMedium)
        Text("Authenticated dashboard")
        when {
            state.loading -> CircularProgressIndicator()
            state.error != null -> {
                Text("Dashboard error: " + state.error, color = MaterialTheme.colorScheme.error)
                Button(onClick = viewModel::loadDashboard) { Text("Retry") }
            }
            state.dashboard == null -> Text("No dashboard data returned.")
            else -> {
                val d = state.dashboard
                Text("Projects: " + d.projects)
                Text("Research: " + d.research)
                Text("Hypotheses: " + d.hypotheses)
                Text("Experiments: " + d.experiments)
                Text("Failures: " + d.failures)
                Text("IP records: " + d.ip)
                Text("Relationships: " + d.relationships)
                Button(onClick = viewModel::loadDashboard) { Text("Refresh") }
            }
        }
        OutlinedButton(onClick = authViewModel::signOut) { Text("Sign Out") }
    }
}