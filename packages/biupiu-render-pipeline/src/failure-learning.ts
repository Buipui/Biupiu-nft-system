export type FailureClass="AUTHORIZATION"|"VALIDATION"|"PROVIDER_TRANSIENT"|"PROVIDER_PERMANENT"|"ASSET"|"TIMEOUT"|"UNKNOWN";
export type RemediationAction="RETRY"|"REFRESH_ASSET"|"CHANGE_PROVIDER"|"REVIEW_CONFIGURATION"|"REQUIRE_HUMAN_REVIEW"|"STOP";
export interface FailureRecord { jobId:string; class:FailureClass; code:string; message:string; provider?:string; retryable:boolean; timestamp:string; context:Record<string,unknown>; }
export interface RecoveryPlan { action:RemediationAction; reason:string; confidence:"LOW"|"MEDIUM"|"HIGH"; requiresApproval:boolean; }
export function classifyFailure(code:string):FailureClass {
 if(code.startsWith("AUTH_"))return "AUTHORIZATION"; if(code.startsWith("ASSET_"))return "ASSET"; if(code.startsWith("TIMEOUT_"))return "TIMEOUT"; if(code.startsWith("PROVIDER_TRANSIENT_"))return "PROVIDER_TRANSIENT"; if(code.startsWith("PROVIDER_PERMANENT_"))return "PROVIDER_PERMANENT"; if(code.startsWith("VALIDATION_"))return "VALIDATION"; return "UNKNOWN";
}
export function recoveryForFailure(f:FailureRecord):RecoveryPlan {
 switch(f.class){case "PROVIDER_TRANSIENT":case "TIMEOUT":return {action:"RETRY",reason:"transient execution failure",confidence:"HIGH",requiresApproval:false};case "ASSET":return {action:"REFRESH_ASSET",reason:"source asset requires validation or refresh",confidence:"MEDIUM",requiresApproval:true};case "PROVIDER_PERMANENT":return {action:"CHANGE_PROVIDER",reason:"provider reported a terminal failure",confidence:"MEDIUM",requiresApproval:true};case "AUTHORIZATION":return {action:"STOP",reason:"authorization must be resolved before execution",confidence:"HIGH",requiresApproval:true};default:return {action:"REQUIRE_HUMAN_REVIEW",reason:"insufficient evidence for safe automated recovery",confidence:"LOW",requiresApproval:true};}
}