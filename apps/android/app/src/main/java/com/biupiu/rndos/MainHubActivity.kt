package com.biupiu.rndos

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.graphics.Color
import android.view.Gravity
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView

class MainHubActivity : Activity() {
    private val session = RuntimeSession("local-preview", "PUBLIC", "active", emptyList())

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            gravity = Gravity.CENTER
            setPadding(48, 48, 48, 48)
        }
        root.addView(TextView(this).apply {
            text = "BIUPIU R&D OS"
            textSize = 28f
            gravity = Gravity.CENTER
            setTextColor(Color.BLACK)
        })
        listOf(
            "SMART_FARMING",
            "SMART_METAL_WORKSHOP",
            "RND_OS",
            "RENDER_PIPELINE",
            "CREATIVE_AI"
        ).forEach { route ->
            val state = CapabilityRouter.route(session, route)
            root.addView(Button(this).apply {
                text = when (state.reason) {
                    "AUTHORIZED" -> "ENTER  $route"
                    "REGISTERED_NOT_ENTITLED" -> "LOCKED  $route"
                    else -> "UNAVAILABLE  $route"
                }
                isEnabled = state.enterable
                setOnClickListener { openDepartment(route) }
            })
        }
        setContentView(root)
    }

    private fun openDepartment(route: String) {
        val state = CapabilityRouter.route(session, route)
        if (!state.enterable) return
        val module = DepartmentModuleRegistry.resolve(route) ?: return
        val activityClass = when (module.screenId) {
            "FARMING_WORLD" -> SmartFarmingActivity::class.java
            "METAL_MAKING_WORLD" -> SmartMetallurgyActivity::class.java
            "RND_OS_HOME" -> RndOsActivity::class.java
            "RENDER_PIPELINE" -> RenderPipelineActivity::class.java
            else -> return
        }
        startActivity(Intent(this, activityClass))
    }
}
