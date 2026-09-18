import type { RenderJob } from "@biupiu/render-pipeline";
export interface ShowcaseRenderRequest extends RenderJob { title:string; sourceModelVersion:string; reviewState:"DRAFT"|"REVIEW"|"APPROVED"; }