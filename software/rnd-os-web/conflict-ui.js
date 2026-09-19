export const CONFLICT_ACTIONS=["USE_SERVER","SAVE_LOCAL_REVISION","MANUAL_MERGE"];
export function describeConflict(conflict){
 return {title:"Sync conflict requires review",message:"The server version changed after your local version. Select an explicit resolution.",serverVersion:conflict?.server_version,localVersion:conflict?.base_version,contentHash:conflict?.content_hash,actions:CONFLICT_ACTIONS};
}
export async function resolveConflict(apiBase,recordId,operationId,strategy){
 if(!CONFLICT_ACTIONS.includes(strategy)) throw new Error("Invalid conflict strategy");
 const r=await fetch(apiBase+"/records/"+encodeURIComponent(recordId)+"/conflicts/resolve",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({operation_id:operationId,strategy})});
 const data=await r.json().catch(()=>({})); if(!r.ok) throw new Error(data.error||"Conflict resolution failed"); return data;
}