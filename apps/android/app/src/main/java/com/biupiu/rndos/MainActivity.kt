package com.biupiu.rndos

import android.app.Activity
import android.os.Bundle
import androidx.activity.compose.setContent

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { BiupiuApp() }
    }
}
