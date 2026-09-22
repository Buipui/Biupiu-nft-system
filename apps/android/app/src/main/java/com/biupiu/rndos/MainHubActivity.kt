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
 private val session=RuntimeSession("android-preview","local-preview","PUBLIC","active",emptyList())

 override fun onCreate(savedInstanceState:Bundle?){
  super.onCreate(savedInstanceState)
  val root=LinearLayout(this).apply{
   orientation=LinearLayout.VERTICAL
   gravity=Gravity.CENTER
   setPadding(48,48,48,48)
  }
  root.addView(TextView(this).apply{
   text="BIUPIU R&D OS"
   textSize=28f
   gravity=Gravity.CENTER
   setTextColor(Color.BLACK)
  })
  val status=root.addViewAndReturn(TextView(this).apply{
   text="READY — select a workspace"
   gravity=Gravity.CENTER
   setPadding(0,16,0,20)
  })

  listOf("SMART_FARMING","SMART_METAL_WORKSHOP","RND_OS","RENDER_PIPELINE").forEach{route->
   val state=BiupiuRuntime.resolveRoute(session,route)
   root.addView(Button(this).apply{
    text=when {
     route=="RENDER_PIPELINE" -> "RENDER PIPELINE — NOT REGISTERED"
     state.enterable -> "ENTER  $route"
     else -> "LOCKED  $route"
    }
    setOnClickListener{
     if(route=="RENDER_PIPELINE"){
      status.text="RENDER_PIPELINE — UNKNOWN_CAPABILITY"
      return@setOnClickListener
     }
     if(!state.enterable){
      status.text="$route — ${state.reason}"
      return@setOnClickListener
     }
     openDepartment(route)
    }
   })
  }
  setContentView(root)
 }

 private fun openDepartment(route:String){
  val module=DepartmentModuleRegistry.resolve(route)
  if(module==null){
   return
  }
  val activityClass=when(module.screenId){
   "FARMING_WORLD"->SmartFarmingActivity::class.java
   "METAL_MAKING_WORLD"->SmartMetallurgyActivity::class.java
   "RND_OS_HOME"->RndOsActivity::class.java
   else->return
  }
  startActivity(Intent(this,activityClass))
 }
}

private fun <T : android.view.View> LinearLayout.addViewAndReturn(view:T):T {
 addView(view)
 return view
}
