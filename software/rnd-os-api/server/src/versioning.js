import crypto from "node:crypto";
export function contentHash(payload){
 return crypto.createHash("sha256").update(JSON.stringify(payload)).digest("hex");
}
export function nextRecordVersion(previousVersion=0){return previousVersion+1}
export function conflict(serverVersion,baseVersion){return serverVersion!==baseVersion}