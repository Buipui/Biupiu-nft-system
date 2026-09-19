package com.biupiu.rndos.api
import kotlinx.serialization.Serializable
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path
@Serializable data class SyncRequest(val base_version:Int,val operation_id:String,val payload:String)
@Serializable data class ConflictResponse(val error:String,val server_version:Int?=null,val base_version:Int?=null,val content_hash:String?=null)
@Serializable data class ResolutionRequest(val operation_id:String,val strategy:String)
interface SyncApi {
 @GET("v1/records/{id}/revisions") suspend fun revisions(@Path("id") id:String):List<RecordRevision>
 @POST("v1/records/{id}/sync") suspend fun sync(@Path("id") id:String,@Body body:SyncRequest):Map<String,String>
 @POST("v1/records/{id}/conflicts/resolve") suspend fun resolve(@Path("id") id:String,@Body body:ResolutionRequest):Map<String,String>
}