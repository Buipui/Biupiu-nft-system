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
