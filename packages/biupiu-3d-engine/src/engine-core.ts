export type Vec3={x:number;y:number;z:number};
export type EngineState="BOOTING"|"READY"|"RUNNING"|"PAUSED"|"FAULT";
export type EvidenceState="DOCUMENTED"|"RECONSTRUCTED"|"EXPERIMENTAL"|"HYPOTHESIS"|"SPECULATIVE";
export type LayerKind="TERRAIN"|"HYDROLOGY"|"WEATHER"|"SOIL"|"VEGETATION"|"WILDLIFE"|"INFRASTRUCTURE"|"VEHICLE"|"HMI"|"XR";
export interface TwinEntity{id:string;kind:string;evidence:EvidenceState;position:Vec3;velocity:Vec3;attributes:Record<string,number|string|boolean>;enabled:boolean}
export interface AssetBinding{assetId:string;sourcePackage:string;canonicalFormat:"USD"|"GLTF"|"GLB"|"NATIVE";twinId?:string;provenance:string[];licenceState:"CLEARED"|"PENDING"|"RESTRICTED"}
export interface WorldLayer{id:string;kind:LayerKind;enabled:boolean;quality:number;entityIds:string[]}
export interface EngineSnapshot{engineVersion:string;state:EngineState;tick:number;simTimeS:number;entities:Record<string,TwinEntity>;layers:WorldLayer[];faults:string[]}
export interface EnginePlugin{id:string;version:string;init(engine:BiupiuEngine):void;tick?(engine:BiupiuEngine,dtS:number):void;shutdown?(engine:BiupiuEngine):void}
const finite=(n:number,l:string)=>{if(!Number.isFinite(n))throw new Error(l+" must be finite");return n};
const clone=(v:Vec3):Vec3=>({x:v.x,y:v.y,z:v.z});
export class BiupiuEngine{
 readonly engineVersion="0.1.0"; private _state:EngineState="BOOTING"; private _tick=0; private _simTimeS=0;
 private entities=new Map<string,TwinEntity>(); private assets=new Map<string,AssetBinding>(); private layers=new Map<string,WorldLayer>(); private plugins=new Map<string,EnginePlugin>(); private faults:string[]=[];
 boot(){if(this._state==="FAULT")throw new Error("engine is faulted");this._state="READY"}
 start(){if(this._state!=="READY"&&this._state!=="PAUSED")throw new Error("engine must be READY or PAUSED");this._state="RUNNING"}
 pause(){if(this._state==="RUNNING")this._state="PAUSED"}
 registerLayer(l:WorldLayer){if(!l.id.trim())throw new Error("layer id required");if(this.layers.has(l.id))throw new Error("duplicate layer: "+l.id);this.layers.set(l.id,{...l,entityIds:[...l.entityIds]})}
 registerEntity(e:TwinEntity){if(!e.id.trim())throw new Error("entity id required");if(this.entities.has(e.id))throw new Error("duplicate entity: "+e.id);for(const n of [e.position.x,e.position.y,e.position.z,e.velocity.x,e.velocity.y,e.velocity.z])finite(n,"entity vector");this.entities.set(e.id,{...e,position:clone(e.position),velocity:clone(e.velocity),attributes:{...e.attributes}})}
 bindAsset(a:AssetBinding){if(!a.assetId.trim())throw new Error("assetId required");if(!a.provenance.length)throw new Error("asset provenance required");this.assets.set(a.assetId,{...a,provenance:[...a.provenance]})}
 use(p:EnginePlugin){if(this.plugins.has(p.id))throw new Error("duplicate plugin: "+p.id);this.plugins.set(p.id,p);p.init(this)}
 step(dtS:number){finite(dtS,"dtS");if(dtS<=0)throw new Error("dtS must be > 0");if(this._state!=="RUNNING")return;try{for(const e of this.entities.values()){e.position.x+=e.velocity.x*dtS;e.position.y+=e.velocity.y*dtS;e.position.z+=e.velocity.z*dtS}for(const p of this.plugins.values())p.tick?.(this,dtS);this._tick++;this._simTimeS+=dtS}catch(err){this.faults.push(err instanceof Error?err.message:String(err));this._state="FAULT";throw err}}
 snapshot():EngineSnapshot{const entities:Record<string,TwinEntity>={};for(const [id,e] of this.entities)entities[id]={...e,position:clone(e.position),velocity:clone(e.velocity),attributes:{...e.attributes}};return{engineVersion:this.engineVersion,state:this._state,tick:this._tick,simTimeS:this._simTimeS,entities,layers:[...this.layers.values()].map(x=>({...x,entityIds:[...x.entityIds]})),faults:[...this.faults]}}
 health(){return{state:this._state,tick:this._tick,entities:this.entities.size,assets:this.assets.size,layers:this.layers.size,plugins:this.plugins.size,faults:[...this.faults]}}
}
export function createBiupiuWorld(){const e=new BiupiuEngine();const kinds:LayerKind[]=["TERRAIN","HYDROLOGY","WEATHER","SOIL","VEGETATION","WILDLIFE","INFRASTRUCTURE","VEHICLE","HMI","XR"];for(const kind of kinds)e.registerLayer({id:kind.toLowerCase(),kind,enabled:true,quality:1,entityIds:[]});e.boot();return e}
export function runEngineSelfCheck(){const e=createBiupiuWorld();e.registerEntity({id:"selfcheck-ground",kind:"reference",evidence:"DOCUMENTED",position:{x:0,y:0,z:0},velocity:{x:1,y:0,z:0},attributes:{source:"biupiu"},enabled:true});e.start();e.step(1);const s=e.snapshot();const errors:string[]=[];if(s.state!=="RUNNING"||s.tick!==1||s.simTimeS!==1)errors.push("scheduler invariant failed");if(s.entities["selfcheck-ground"].position.x!==1)errors.push("transform integration failed");if(s.layers.length!==10)errors.push("world layer registration failed");return errors}
