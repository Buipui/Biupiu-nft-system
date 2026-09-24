export interface AssetMaterialRef { materialId:string; provenanceStatus:"verified"|"pending-review"|"reference-only"|"restricted"; }
export interface VisualAssetManifest {
  assetId:string; name:string; domain:string;
  source:{uri:string;format:string;sha256?:string|null};
  geometry:{status:"validated"|"pending"|"failed";units?:string|null;scale?:number|null};
  materials:AssetMaterialRef[]; environment:string;
  validation:{status:"passed"|"pending"|"failed";checkedAt:string;errors?:string[]};
}
export function validateAssetManifest(a:VisualAssetManifest):string[] {
  const e:string[]=[];
  if(!/^asset-[a-z0-9-]+$/.test(a.assetId)) e.push("invalid assetId");
  if(!a.source?.uri || !a.source?.format) e.push("source uri and format required");
  if(a.geometry?.status!=="validated") e.push("geometry must be validated");
  if(!a.materials?.length) e.push("at least one material reference required");
  for(const m of a.materials||[]) if(m.provenanceStatus==="restricted") e.push("restricted material cannot enter render manifest");
  if(!a.environment) e.push("environment required");
  return e;
}
