import { validateMaterial } from "../src/material-registry";

const base = {
  materialId:"mat-hemp-panel-v1", family:"hemp-fibre-composite", displayName:"Biupiu Hemp Panel",
  sourceType:"biupiu-generated", license:"Biupiu internal", redistributionAllowed:true,
  modificationAllowed:true, provenanceStatus:"verified" as const
};

if(validateMaterial(base).length) throw new Error("valid material rejected");
if(!validateMaterial({...base, license:""}).includes("license required")) throw new Error("missing license not rejected");
if(!validateMaterial({...base, provenanceStatus:"pending-review"}).includes("redistributable material must be verified")) throw new Error("unverified redistribution not rejected");
if(!validateMaterial({...base, sourceType:"reference-only"}).includes("reference-only material cannot be redistributed")) throw new Error("reference-only redistribution not rejected");
