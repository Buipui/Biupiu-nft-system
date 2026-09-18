import type { RenderJob, RenderProvider } from "../src/index";

const providers: RenderProvider[] = ["BLENDER","UNREAL_ENGINE_5","REDSHIFT","VRAY","OCTANE","LUMION","KEYSHOT"];
const job: RenderJob = { sourceAssetIds:["BIUPIU-RENDER-TEST-001"], provider:"REDSHIFT", output:"STILL", provenanceRequired:true };
if (providers.length !== 7) throw new Error("RED-04 provider matrix is incomplete.");
if (!providers.includes(job.provider)) throw new Error("RED-04 job provider is outside the interoperability matrix.");
if (!job.provenanceRequired || job.sourceAssetIds.length !== 1) throw new Error("RED-04 requires source identity and provenance.");
