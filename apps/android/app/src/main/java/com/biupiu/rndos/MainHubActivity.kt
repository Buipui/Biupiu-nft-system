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

        listOf("SMART_FARMING", "SMART_METAL_WORKSHOP", "RND_OS").forEach { route ->
            val state = BiupiuRuntime.resolveRoute(session, route)
            val button = Button(this).apply {
                text = if (state.enterable) "ENTER  $route" else "LOCKED  $route"
                isEnabled = state.enterable
                setOnClickListener { openDepartment(route) }
            }
            root.addView(button)
        }
        setContentView(root)
    }

    private fun openDepartment(route: String) {
        val module = DepartmentModuleRegistry.resolve(route) ?: return
        val activityClass = when (module.screenId) {
            "FARMING_WORLD" -> SmartFarmingActivity::class.java
            "METAL_MAKING_WORLD" -> SmartMetallurgyActivity::class.java
            "RND_OS_HOME" -> RndOsActivity::class.java
            else -> return
        }
        startActivity(Intent(this, activityClass))
    }
}
