export const RUNWAY_MEDIA_ROUTE = "RUNWAY_MEDIA";

export type RunwayMediaCapability =
  | "IMAGE_GENERATION"
  | "VIDEO_GENERATION"
  | "VIDEO_EDITING"
  | "VIDEO_UPSCALE"
  | "AUDIO_GENERATION";

export interface RunwayMediaRequest {
  capability: RunwayMediaCapability;
  prompt?: string;
  sourceAssetIds?: string[];
  model?: string;
  ratio?: string;
  durationSeconds?: number;
}
