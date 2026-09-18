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
                composable("dashboard") {
                    DashboardScreen(
                        { navController.navigate("research") },
                        { navController.navigate("experiments") },
                        { navController.navigate("assets") },
                        { navController.navigate("controls") }
                    )
                }
                composable("research") { FormScreen("Research Objects", "Create evidence-classified research records.") }
                composable("experiments") { FormScreen("Digital Laboratory", "Log hypotheses, protocols and observations.") }
                composable("assets") { FormScreen("Assets & NFTs", "Create provenance records and mint payloads. Blockchain signing remains gated.") }
                composable("controls") { FormScreen("Control Centre", "Audit trail, release gates and security boundaries.") }
            }
        }
    }
}

@Composable
private fun DashboardScreen(onResearch: () -> Unit, onExperiments: () -> Unit, onAssets: () -> Unit, onControls: () -> Unit) {
    Column(Modifier.fillMaxSize().padding(24.dp), verticalArrangement = Arrangement.spacedBy(14.dp)) {
        Text("Biupiu R&D OS", style = MaterialTheme.typography.headlineMedium)
        Text("Cross-platform prototype v1.0")
        Text("Research → Hypothesis → Experiment → Evidence → Validation → Provenance → Release")
        Button(onClick = onResearch, modifier = Modifier.fillMaxWidth()) { Text("Research Objects") }
        Button(onClick = onExperiments, modifier = Modifier.fillMaxWidth()) { Text("Digital Laboratory") }
        Button(onClick = onAssets, modifier = Modifier.fillMaxWidth()) { Text("Assets & NFT Console") }
        Button(onClick = onControls, modifier = Modifier.fillMaxWidth()) { Text("Control Centre") }
    }
}

@Composable
private fun FormScreen(title: String, message: String) {
    Column(Modifier.fillMaxSize().padding(24.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
        Text(title, style = MaterialTheme.typography.headlineSmall)
        Text(message)
        Text("Production API, persistent audit storage, authentication and blockchain execution are explicit next gates.")
    }
}
