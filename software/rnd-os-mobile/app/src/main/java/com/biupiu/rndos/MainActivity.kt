package com.biupiu.rndos

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { BiupiuRndOsApp() }
    }
}

@Composable
fun BiupiuRndOsApp() {
    val navController = rememberNavController()
    MaterialTheme {
        Surface(Modifier.fillMaxSize()) {
            NavHost(navController, startDestination = "dashboard") {
                composable("dashboard") { DashboardScreen({ navController.navigate("research") }, { navController.navigate("experiments") }) }
                composable("research") { PlaceholderScreen("Research Objects", "API integration is the next mobile gate.") }
                composable("experiments") { PlaceholderScreen("Experimental Control Centre", "Experiment capture is planned for v0.9.") }
            }
        }
    }
}

@Composable
private fun DashboardScreen(onResearch: () -> Unit, onExperiments: () -> Unit) {
    Column(Modifier.fillMaxSize().padding(24.dp), verticalArrangement = Arrangement.spacedBy(16.dp)) {
        Text("Biupiu R&D OS", style = MaterialTheme.typography.headlineMedium)
        Text("Mobile foundation v0.7")
        Text("Research → Hypothesis → Experiment → Evidence → Validation")
        Button(onClick = onResearch, modifier = Modifier.fillMaxWidth()) { Text("Research Objects") }
        Button(onClick = onExperiments, modifier = Modifier.fillMaxWidth()) { Text("Experimental Control Centre") }
    }
}

@Composable
private fun PlaceholderScreen(title: String, message: String) {
    Column(Modifier.fillMaxSize().padding(24.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
        Text(title, style = MaterialTheme.typography.headlineSmall)
        Text(message)
    }
}
