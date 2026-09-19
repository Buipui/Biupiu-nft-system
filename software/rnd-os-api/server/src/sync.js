// Conflict-safe synchronization primitives for the client queue.
// Server timestamps and record versions are authoritative in production.
export function makeOperation({id,type,payload,baseVersion=0}){
  return {operation_id:id,entity_type:type,payload,base_version:baseVersion,created_at:new Date().toISOString()};
}
export function applyPolicy(serverVersion,baseVersion){
  if(baseVersion===serverVersion)return "APPLY";
  return "CONFLICT";
}