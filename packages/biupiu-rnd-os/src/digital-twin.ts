export type TwinEvidenceState = "T0"|"T1"|"T2"|"T3"|"T4"|"T5"|"T6"|"T7"|"T8"|"T9";
export interface DigitalTwinRef { twinId:string; schemaVersion:string; modelVersion:string; evidenceState:TwinEvidenceState; sourceRefs:string[]; dmsSiteId?:string; dmsAssetId?:string; }
export interface TwinEvent { eventId:string; twinId:string; eventType:"STATE_UPDATE"|"TELEMETRY"|"SIMULATION"|"TEST_RESULT"|"CALIBRATION"; occurredAt:string; source:"SIMULATION"|"DEVICE"|"TEST"|"HUMAN"|"AI"; payloadRef:string; modelVersion:string; provenanceRefs:string[]; }
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
export function dmsDigitalTwinFeatureId():string{return "digital-twin.advanced";}
