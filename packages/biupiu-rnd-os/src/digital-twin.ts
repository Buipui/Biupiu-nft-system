export type TwinEvidenceState = "T0"|"T1"|"T2"|"T3"|"T4"|"T5"|"T6"|"T7"|"T8"|"T9";
export type TwinSource = "SIMULATION"|"DEVICE"|"TEST"|"HUMAN"|"AI";
export type ActuatorKind = "HUMAN"|"AGENT"|"ROBOT"|"CONNECTED_SYSTEM";

export interface DigitalTwinRef {
 twinId:string;
 schemaVersion:string;
 modelVersion:string;
 evidenceState:TwinEvidenceState;
 sourceRefs:string[];
 dmsSiteId?:string;
 dmsAssetId?:string;
 contextType?:string;
 ontologyRefs?:string[];
}

export interface TwinEvent {
 eventId:string;
 twinId:string;
 eventType:"STATE_UPDATE"|"TELEMETRY"|"SIMULATION"|"TEST_RESULT"|"CALIBRATION";
 occurredAt:string;
 source:TwinSource;
 payloadRef:string;
 modelVersion:string;
 provenanceRefs:string[];
}

export interface TwinContextEntity {
 id:string;
 type:string;
 attributes:Record<string, unknown>;
 relationships:Record<string,string[]>;
 observedAt?:string;
}

export interface TwinActionRequest {
 actionId:string;
 twinId:string;
 actuator:ActuatorKind;
 actionType:string;
 requestedAt:string;
 confidence:number;
 evidenceState:TwinEvidenceState;
 simulationRef?:string;
 policyRefs:string[];
 humanApprovalRequired:boolean;
}

const STATES:TwinEvidenceState[]=["T0","T1","T2","T3","T4","T5","T6","T7","T8","T9"];

export function createTwinEvent(input:Omit<TwinEvent,"eventId"> & {eventId?:string}):TwinEvent {
 if(!input.twinId.trim()) throw new Error("twinId is required");
 if(!input.modelVersion.trim()) throw new Error("modelVersion is required");
 if(!input.payloadRef.trim()) throw new Error("payloadRef is required");
 if(input.provenanceRefs.length===0) throw new Error("at least one provenance reference is required");
 if(Number.isNaN(Date.parse(input.occurredAt))) throw new Error("occurredAt must be an ISO-compatible timestamp");
 return {...input,eventId:input.eventId ?? `twin_evt_${input.twinId}_${Date.parse(input.occurredAt)}`};
}

export function canPromoteEvidence(current:TwinEvidenceState,next:TwinEvidenceState):boolean {
 const currentIndex=STATES.indexOf(current), nextIndex=STATES.indexOf(next);
 return currentIndex>=0 && nextIndex===currentIndex+1;
}

/** Normalize a governed context entity for NGSI-LD-style linked-data exchange. */
export function toLinkedContextEntity(entity:TwinContextEntity):Record<string,unknown>{
 if(!entity.id.trim() || !entity.type.trim()) throw new Error("context entity id and type are required");
 return {
  id:entity.id,
  type:entity.type,
  ...entity.attributes,
  ...(Object.keys(entity.relationships).length ? {relationships:entity.relationships} : {}),
  ...(entity.observedAt ? {observedAt:entity.observedAt} : {})
 };
}

/** Map an asset to an AAS-style shell reference without importing an external runtime. */
export function toAssetAdministrationShellRef(twin:DigitalTwinRef){
 return {
  id:twin.twinId,
  modelVersion:twin.modelVersion,
  semanticIds:twin.ontologyRefs ?? [],
  assetRef:twin.dmsAssetId,
  siteRef:twin.dmsSiteId
 };
}

/** Candidate actions are blocked unless policy, evidence and simulation conditions are met. */
export function canActuate(action:TwinActionRequest):boolean{
 if(!action.actionId.trim() || !action.twinId.trim() || !action.actionType.trim()) return false;
 if(action.confidence<0 || action.confidence>1) return false;
 if(action.policyRefs.length===0) return false;
 if(action.evidenceState==="T0" || action.evidenceState==="T1") return false;
 if(!action.simulationRef) return false;
 return !action.humanApprovalRequired;
}

export function requiresHumanApproval(action:TwinActionRequest):boolean{
 return action.humanApprovalRequired || action.confidence<0.90 || action.evidenceState==="T2" || action.evidenceState==="T3";
}

export function dmsDigitalTwinFeatureId():string{return "digital-twin.advanced";}

export function canLearnFromTwinEvent(event:TwinEvent):boolean {
 return event.provenanceRefs.length>0 && !!event.modelVersion.trim() && (event.eventType==="SIMULATION" || event.eventType==="TEST_RESULT" || event.eventType==="CALIBRATION" || event.eventType==="STATE_UPDATE" || event.eventType==="TELEMETRY");\n}\n\nexport function bindLearningReference(twin:DigitalTwinRef, learningId:string):DigitalTwinRef {
 if(!learningId.trim()) throw new Error("learningId is required");
 return {...twin, sourceRefs:[...twin.sourceRefs, learningId]};\n}
