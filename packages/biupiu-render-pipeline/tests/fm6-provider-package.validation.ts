import {createFM6ProviderPackagePlan} from "../src/fm6-provider-package";
describe("FM6 provider package planning",()=>{
 const base={digitalTwinId:"DT-AUTO-001",sourceAssetId:"BIU-VEH-001",sourceModelVersion:"1.0.0",presetId:"BIU-AUTO-FM6REF-STUDIO-001",renderer:"unreal-engine-5" as const,licenceState:"CLEARED" as const,referenceState:"FM6-REFERENCE-ONLY" as const};
 it("creates a provenance-gated plan",()=>{const p=createFM6ProviderPackagePlan(base);expect(p.validation.provenance).toBe("PASS");expect(p.validation.rendererEnvironment).toBe("NOT_EXECUTED");});
 it("blocks uncleared assets",()=>{expect(()=>createFM6ProviderPackagePlan({...base,licenceState:"PENDING"})).toThrow();});
 it("blocks non-reference state",()=>{expect(()=>createFM6ProviderPackagePlan({...base,referenceState:"OTHER" as any})).toThrow();});
});