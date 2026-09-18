package com.biupiu.rndos.ui

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp
import com.biupiu.rndos.auth.AuthViewModel

@Composable
fun AuthScreen(viewModel: AuthViewModel) {
    var token by remember { mutableStateOf("") }
    var userId by remember { mutableStateOf("dev-user") }
    var organisationId by remember { mutableStateOf("biupiu-dev") }
    var expiresAt by remember { mutableStateOf("2099-12-31T23:59:59Z") }

    Column(Modifier.fillMaxSize().padding(24.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
        Text("Biupiu R&D OS", style = MaterialTheme.typography.headlineMedium)
        Text("Development authentication gate")
        Text("Enter a development bearer token. Never ship a real credential in source code.")
        OutlinedTextField(token, { token = it }, label = { Text("Bearer token") }, visualTransformation = PasswordVisualTransformation(), modifier = Modifier.fillMaxWidth())
        OutlinedTextField(userId, { userId = it }, label = { Text("User ID") }, modifier = Modifier.fillMaxWidth())
        OutlinedTextField(organisationId, { organisationId = it }, label = { Text("Organisation ID") }, modifier = Modifier.fillMaxWidth())
        OutlinedTextField(expiresAt, { expiresAt = it }, label = { Text("Expiry (ISO-8601)") }, modifier = Modifier.fillMaxWidth())
        viewModel.state.error?.let { Text(it, color = MaterialTheme.colorScheme.error) }
        Button(onClick = { viewModel.setDevelopmentSession(token, userId, organisationId, expiresAt) }, modifier = Modifier.fillMaxWidth()) {
            Text("Save Secure Session")
        }
    }
}