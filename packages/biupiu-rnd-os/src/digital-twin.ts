export type TwinEvidenceState = "T0"|"T1"|"T2"|"T3"|"T4"|"T5"|"T6"|"T7"|"T8"|"T9";

export interface DigitalTwinRef {
  twinId: string;
  schemaVersion: string;
  modelVersion: string;
  evidenceState: TwinEvidenceState;
  sourceRefs: string[];
  dmsSiteId?: string;
  dmsAssetId?: string;
}

export interface TwinEvent {
  eventId: string;
  twinId: string;
  eventType: "STATE_UPDATE"|"TELEMETRY"|"SIMULATION"|"TEST_RESULT"|"CALIBRATION";
  occurredAt: string;
  source: "SIMULATION"|"DEVICE"|"TEST"|"HUMAN"|"AI";
  payloadRef: string;
  modelVersion: string;
  provenanceRefs: string[];
}

export function createTwinEvent(input: Omit<TwinEvent, "eventId"> & { eventId?: string }): TwinEvent {
  return {
    ...input,
    eventId: input.eventId ?? `twin_evt_${input.twinId}_${Date.parse(input.occurredAt)}`,
  };
}

export function canPromoteEvidence(current: TwinEvidenceState, next: TwinEvidenceState): boolean {
  const order = Number(next.slice(1)) - Number(current.slice(1));
  return order === 1;
}

export function dmsDigitalTwinFeatureId(): string {
  return "digital-twin.advanced";
}
