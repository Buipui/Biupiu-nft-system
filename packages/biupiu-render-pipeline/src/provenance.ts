export interface ConversionLineage {
  sourceFormat:string;
  targetFormat:string;
  provider:string;
  status:"READY"|"BLOCKED"|"LOSSY"|"FAILED";
  unsupportedFeatures:string[];
  warnings:string[];
}

export interface RenderProvenance {
  jobId:string;
  sourceAssetIds:string[];
  sourceModelVersion:string;
  provider:string;
  providerJobId?:string;
  createdAt:string;
  parentJobId?:string;
  conversions?:ConversionLineage[];
}

export const createProvenance=(p:Omit<RenderProvenance,"createdAt">):RenderProvenance=>({...p,createdAt:new Date().toISOString()});

export function appendConversionLineage(provenance:RenderProvenance, conversion:ConversionLineage):RenderProvenance {
  return { ...provenance, conversions:[...(provenance.conversions||[]), conversion] };
}


export interface ReleaseProvenanceRequirements {
  outputHash: string;
  sourceAssetIds: string[];
  sourceModelVersion: string;
  provider: string;
  providerJobId?: string;
  conversions: ConversionLineage[];
  humanApproved: boolean;
}

export function validateReleaseProvenance(
  provenance: RenderProvenance,
  requirements: ReleaseProvenanceRequirements
): void {
  if (!requirements.humanApproved) throw new Error("Release requires human approval.");
  if (!requirements.outputHash) throw new Error("Release requires an output hash.");
  if (!requirements.sourceAssetIds.length || !requirements.sourceModelVersion) {
    throw new Error("Release requires complete source identity.");
  }
  if (provenance.provider !== requirements.provider) throw new Error("Release provider does not match provenance.");
  if (provenance.sourceModelVersion !== requirements.sourceModelVersion) throw new Error("Release model version does not match provenance.");
  if (provenance.sourceAssetIds.join("|") !== requirements.sourceAssetIds.join("|")) {
    throw new Error("Release source assets do not match provenance.");
  }
  if (requirements.providerJobId && provenance.providerJobId !== requirements.providerJobId) {
    throw new Error("Release provider job does not match provenance.");
  }
  if (requirements.conversions.some(c => c.status === "FAILED" || c.status === "BLOCKED")) {
    throw new Error("Release blocked by failed or blocked conversion.");
  }
  if (requirements.conversions.length !== (provenance.conversions || []).length) {
    throw new Error("Release conversion lineage is incomplete.");
  }
}
