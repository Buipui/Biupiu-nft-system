package com.biupiu.rndos.api

import kotlinx.serialization.Serializable
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path

@Serializable
data class ResearchObject(val id:String?=null,val title:String,val evidence_class:String,val notes:String?=null)

@Serializable
data class Experiment(val id:String?=null,val title:String,val hypothesis:String,val protocol:String?=null)

@Serializable
data class DigitalAsset(val id:String?=null,val name:String,val status:String="DRAFT")

@Serializable
data class GateRequest(val status:String)

interface RndApi {
    @GET("v1/research") suspend fun research():List<Map<String,String>>
    @POST("v1/research") suspend fun createResearch(@Body body:ResearchObject):ResearchObject
    @GET("v1/experiments") suspend fun experiments():List<Map<String,String>>
    @POST("v1/experiments") suspend fun createExperiment(@Body body:Experiment):Experiment
    @GET("v1/assets") suspend fun assets():List<Map<String,String>>
    @POST("v1/assets") suspend fun createAsset(@Body body:DigitalAsset):DigitalAsset
    @POST("v1/assets/{id}/gate") suspend fun advanceGate(@Path("id") id:String,@Body body:GateRequest):Map<String,String>
    @GET("v1/audit") suspend fun audit():List<Map<String,String>>
}
