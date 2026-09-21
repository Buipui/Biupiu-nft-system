export interface DmsAuthContext {
  accessTokenRef: string;
  subjectRef: string;
  scopes: string[];
}
export interface TwinEnvelope {
  twinId: string;
  siteId: string;
  assetId: string;
  modelVersion: string;
  provenanceRefs: string[];
  payloadRef: string;
  idempotencyKey: string;
}
export function validateDmsAuthContext(value: DmsAuthContext): void {
  if (!value.accessTokenRef?.trim()) throw new Error("DMS access token reference is required");
  if (!value.subjectRef?.trim()) throw new Error("DMS subject reference is required");
  if (!Array.isArray(value.scopes) || value.scopes.length === 0) throw new Error("DMS scopes are required");
  if (value.accessTokenRef.startsWith("secret://")) throw new Error("Embedded secret references are not permitted");
}
export function validateTwinEnvelope(value: TwinEnvelope): void {
  if (!value.twinId?.trim()) throw new Error("twinId is required");
  if (!value.siteId?.trim()) throw new Error("siteId is required");
  if (!value.assetId?.trim()) throw new Error("assetId is required");
  if (!value.modelVersion?.trim()) throw new Error("modelVersion is required");
  if (!Array.isArray(value.provenanceRefs) || value.provenanceRefs.length === 0) throw new Error("provenanceRefs are required");
  if (!value.payloadRef?.trim()) throw new Error("payloadRef is required");
  if (!value.idempotencyKey?.trim()) throw new Error("idempotencyKey is required");
}
