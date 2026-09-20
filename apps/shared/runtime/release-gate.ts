import type { RenderProvenance, ReleaseProvenanceRequirements } from "@biupiu/render-pipeline";
import { validateReleaseProvenance } from "@biupiu/render-pipeline";

export interface ReleaseRequest {
  assetId:string;
  destination:"SHOWCASE"|"NFT_STUDIO";
  provenance:RenderProvenance;
  requirements:ReleaseProvenanceRequirements;
}

export function authorizeRelease(request:ReleaseRequest):void {
  if (!request.assetId) throw new Error("Release requires assetId.");
  if (request.destination !== "SHOWCASE" && request.destination !== "NFT_STUDIO") {
    throw new Error("Unsupported release destination.");
  }
  validateReleaseProvenance(request.provenance, request.requirements);
}
