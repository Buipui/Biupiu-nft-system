import {EngineBridgeRegistry,EngineRegistration,EngineHealthRecord} from "./engine-bridge";

export interface ProbeResult { engineId:EngineRegistration["engineId"]; passed:boolean; checks:string[]; failures:string[]; warnings:string[]; }
export interface AssetFingerprint { assetId:string; vertexCount:number; triangleCount:number; bounds:[number,number,number]; materialCount:number; sourceHash:string; }
export interface DriftReport { geometryDrift:number; topologyChanged:boolean; materialCountDelta:number; sourceHashChanged:boolean; passed:boolean; }

export function probeEngine(registry:EngineBridgeRegistry,engine:EngineRegistration,checks:string[],failures:string[]=[],warnings:string[]=[]):ProbeResult {
  registry.register(engine);
  const record:EngineHealthRecord={
    engineId:engine.engineId,
    checkedAt:new Date().toISOString(),
    state:failures.length?"BLOCKED":"READY",
    checks,failures,warnings
  };
  registry.setHealth(record);
  return {engineId:engine.engineId,passed:failures.length===0,checks,failures,warnings};
}

export function compareAssetFingerprints(a:AssetFingerprint,b:AssetFingerprint,tolerance=1e-6):DriftReport {
  const scale=Math.max(1,...a.bounds.map(Math.abs),...b.bounds.map(Math.abs));
  const geometryDrift=Math.max(...a.bounds.map((v,i)=>Math.abs(v-b.bounds[i])/scale));
  const topologyChanged=a.vertexCount!==b.vertexCount||a.triangleCount!==b.triangleCount;
  const materialCountDelta=b.materialCount-a.materialCount;
  const sourceHashChanged=a.sourceHash!==b.sourceHash;
  return {geometryDrift,topologyChanged,materialCountDelta,sourceHashChanged,passed:geometryDrift<=tolerance&&!topologyChanged};
}
