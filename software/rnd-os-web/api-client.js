// Biupiu R&D OS API client adapter.
// Configure window.BIUPIU_API_BASE before production use.
const BIUPIU_API_BASE = globalThis.BIUPIU_API_BASE || "/v1";
export async function apiRequest(path, options={}) {
  const response=await fetch(BIUPIU_API_BASE+path,{...options,headers:{"content-type":"application/json",...(options.headers||{})}});
  const data=await response.json().catch(()=>({}));
  if(!response.ok) throw new Error(data.error||"API request failed");
  return data;
}
export const rndApi={
  health:()=>apiRequest("/../health"),
  research:()=>apiRequest("/research"),
  createResearch:x=>apiRequest("/research",{method:"POST",body:JSON.stringify(x)}),
  experiments:()=>apiRequest("/experiments"),
  createExperiment:x=>apiRequest("/experiments",{method:"POST",body:JSON.stringify(x)}),
  assets:()=>apiRequest("/assets"),
  createAsset:x=>apiRequest("/assets",{method:"POST",body:JSON.stringify(x)}),
  advanceGate:(id,status)=>apiRequest("/assets/"+encodeURIComponent(id)+"/gate",{method:"POST",body:JSON.stringify({status})}),
  audit:()=>apiRequest("/audit")
};