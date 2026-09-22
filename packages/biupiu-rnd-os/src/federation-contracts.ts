/** Shared federation contracts harvested from interoperable industrial/open-source patterns.
 * This file defines boundaries only; protocol adapters remain replaceable.
 */
export type FederationHealth = "HEALTHY"|"DEGRADED"|"OFFLINE"|"QUARANTINED";
export type FederationDelivery = "AT_MOST_ONCE"|"AT_LEAST_ONCE"|"EXACTLY_ONCE_REQUESTED";
export type FederationAuthority = "OBSERVE"|"SIMULATE"|"PROPOSE"|"COMMIT";
export type FederationEvidence = "OBSERVED"|"COMPUTED"|"SIMULATED"|"INFERRED"|"UNRESOLVED";
export type FederationLicenceState = "VERIFIED"|"REVIEW"|"RESTRICTED"|"PROHIBITED"|"UNKNOWN";

export interface FederationCapability {
  schemaVersion:string;
  provenance:string;
  id:string;
  version:string;
  enabled:boolean;
  authority:FederationAuthority;
  supportedSchemas:string[];
  transports:string[];
}
export interface FederationHealthSnapshot {
  nodeId:string;
  state:FederationHealth;
  checkedAt:string;
  latencyMs?:number;
  queueDepth?:number;
  clockSkewMs?:number;
  detail?:string;
}
export interface FederationTraceContext {
  traceId:string;
  spanId:string;
  parentSpanId?:string;
  correlationId:string;
}
export interface FederationSchemaRef {
  name:string;
  version:string;
  contentType:string;
  schemaHash:string;
}
export interface FederationDeliveryPolicy {
  mode:FederationDelivery;
  maxAttempts:number;
  retryBackoffMs:number;
  ttlMs?:number;
}
export interface FederationObservation {
  simulationId:string;
  simulatorId:string;
  domain:string;
  modelVersion:string;
  sourceCommit:string;
  inputHash:string;
  outputHash:string;
  timestamp:string;
  seed?:string|number;
  units:string[];
  assumptions:string[];
  evidenceClass:FederationEvidence;
  licenceState:FederationLicenceState;
  schema:FederationSchemaRef;
  trace:FederationTraceContext;
}
export interface FederationAdapterContract {
  adapterId:string;
  version:string;
  discover():Promise<FederationCapability[]>;
  health():Promise<FederationHealthSnapshot>;
  publish(observation:FederationObservation,policy:FederationDeliveryPolicy):Promise<void>;
  close():Promise<void>;
}
