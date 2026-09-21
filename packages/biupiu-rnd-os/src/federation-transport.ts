import type { TwinEnvelope } from "./dms-transport.js";

export type FederationPlatform = "ANDROID"|"LINUX"|"WINDOWS"|"RPI"|"ARDUINO"|"JVM"|"SERVER"|"DEVICE";
export type FederationNodeState = "CREATED"|"QUEUED"|"SENT"|"ACKED"|"RETRYABLE_FAILURE"|"CONFLICT"|"DEAD_LETTER";

export interface FederationNodeRef {
  nodeId:string;
  platform:FederationPlatform;
  protocolVersion:string;
  siteId:string;
  capabilities:string[];
}

export interface FederatedTwinEnvelope {
  federationId:string;
  node: FederationNodeRef;
  envelope:TwinEnvelope;
  eventId:string;
  sequence:number;
  createdAt:string;
  state:FederationNodeState;
}

export interface FederationAck {
  federationId:string;
  eventId:string;
  nodeId:string;
  acknowledgedAt:string;
  duplicate:boolean;
}

function canonical(value:unknown):string {
  return JSON.stringify(value, (_key, item) =>
    item && typeof item === "object" && !Array.isArray(item)
      ? Object.keys(item).sort().reduce((o,k)=>{ (o as Record<string,unknown>)[k]=(item as Record<string,unknown>)[k]; return o; }, {} as Record<string,unknown>)
      : item
  );
}

function fnv1a(value:string):string {
  let hash=0x811c9dc5;
  for(let i=0;i<value.length;i++){ hash ^= value.charCodeAt(i); hash = Math.imul(hash,0x01000193); }
  return (hash>>>0).toString(16).padStart(8,"0");
}

export function deterministicEventId(envelope:TwinEnvelope):string {
  if(!envelope.idempotencyKey.trim()) throw new Error("idempotencyKey is required");
  return `twin_evt_${fnv1a(canonical({
    twinId:envelope.twinId, siteId:envelope.siteId, assetId:envelope.assetId,
    modelVersion:envelope.modelVersion, payloadRef:envelope.payloadRef,
    provenanceRefs:[...envelope.provenanceRefs].sort(), idempotencyKey:envelope.idempotencyKey
  }))}`;
}

export function createFederatedEnvelope(node:FederationNodeRef,envelope:TwinEnvelope,sequence:number,createdAt:string):FederatedTwinEnvelope {
  if(!node.nodeId.trim()) throw new Error("nodeId is required");
  if(!node.protocolVersion.trim()) throw new Error("protocolVersion is required");
  if(!node.siteId.trim()) throw new Error("node siteId is required");
  if(!Number.isInteger(sequence) || sequence<1) throw new Error("sequence must be a positive integer");
  if(Number.isNaN(Date.parse(createdAt))) throw new Error("createdAt must be an ISO-compatible timestamp");
  if(node.siteId!==envelope.siteId) throw new Error("federation node site scope does not match envelope");
  return {federationId:`${node.nodeId}:${sequence}`,node,envelope,eventId:deterministicEventId(envelope),sequence,createdAt,state:"CREATED"};
}

export class FederationReplayStore {
  private readonly records = new Map<string,{fingerprint:string;state:FederationNodeState}>();

  accept(item:FederatedTwinEnvelope):FederationAck|undefined {
    const fingerprint=canonical(item.envelope);
    const existing=this.records.get(item.eventId);
    if(existing && existing.fingerprint!==fingerprint){
      this.records.set(item.eventId,{fingerprint,state:"CONFLICT"});
      item.state="CONFLICT";
      return undefined;
    }
    if(existing){
      item.state=existing.state==="ACKED" ? "ACKED" : "SENT";
      return {federationId:item.federationId,eventId:item.eventId,nodeId:item.node.nodeId,acknowledgedAt:new Date().toISOString(),duplicate:true};
    }
    this.records.set(item.eventId,{fingerprint,state:"QUEUED"});
    item.state="QUEUED";
    return undefined;
  }

  markSent(eventId:string):void { this.setState(eventId,"SENT"); }
  markAcked(eventId:string):void { this.setState(eventId,"ACKED"); }
  markRetryable(eventId:string):void { this.setState(eventId,"RETRYABLE_FAILURE"); }
  markDeadLetter(eventId:string):void { this.setState(eventId,"DEAD_LETTER"); }
  state(eventId:string):FederationNodeState|undefined { return this.records.get(eventId)?.state; }

  private setState(eventId:string,state:FederationNodeState):void {
    const current=this.records.get(eventId);
    if(!current) throw new Error("unknown federation event");
    if(current.state==="CONFLICT" || current.state==="DEAD_LETTER") throw new Error("terminal federation event cannot transition");
    this.records.set(eventId,{...current,state});
  }
}
