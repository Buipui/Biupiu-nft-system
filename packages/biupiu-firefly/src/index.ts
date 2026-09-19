export const BIUPIU_APP = "Biupiu Firefly Creative AI";
export const PACKAGE = "@biupiu/firefly";
export const SCOPE = "CREATIVE_AI" as const;

export type FireflyOperation =
  | "GENERATE_IMAGE"
  | "GENERATE_IMAGE5"
  | "EXPAND_IMAGE"
  | "FILL_IMAGE"
  | "OBJECT_COMPOSITE"
  | "PRECISE_COMPOSITE"
  | "ADAPTIVE_COMPOSITE"
  | "SIMILAR_IMAGES"
  | "UPSCALE"
  | "GENERATE_VIDEO"
  | "UPLOAD_ASSET";

export interface FireflyJobRequest {
  operation: FireflyOperation;
  prompt?: string;
  sourceAssetId?: string;
  referenceAssetId?: string;
  aspectRatio?: string;
  outputFormat?: "png" | "jpeg";
  modelVersion?: "image3" | "image3_custom" | "image4_standard" | "image4_ultra" | "image4_custom" | "image5";
  projectId: string;
  researchId?: string;
  assetId?: string;
}

export interface FireflyJobResult {
  provider: "adobe-firefly";
  operation: FireflyOperation;
  status: "QUEUED" | "RUNNING" | "SUCCEEDED" | "FAILED";
  jobId?: string;
  outputAssetId?: string;
  outputUri?: string;
  errorCode?: string;
  errorMessage?: string;
  provenanceRequired: true;
}

export interface FireflyAdapter {
  health(): Promise<{ configured: boolean; provider: "adobe-firefly" }>;
  submit(request: FireflyJobRequest): Promise<FireflyJobResult>;
  getJob(jobId: string): Promise<FireflyJobResult>;
}

export const FIREFLY_CAPABILITIES: readonly FireflyOperation[] = [
  "GENERATE_IMAGE",
  "GENERATE_IMAGE5",
  "EXPAND_IMAGE",
  "FILL_IMAGE",
  "OBJECT_COMPOSITE",
  "PRECISE_COMPOSITE",
  "ADAPTIVE_COMPOSITE",
  "SIMILAR_IMAGES",
  "UPSCALE",
  "GENERATE_VIDEO",
  "UPLOAD_ASSET"
];

export const FIREFLY_ACCESS_ERRORS = [
  "quota_exhausted",
  "user_non_entitled",
  "user_profile_denied",
  "invalid_ims_scope"
] as const;

export const FIREFLY_PROVENANCE_RULES = {
  researchIdRequiredForResearchAssets: true,
  sourceAssetTracked: true,
  promptTracked: true,
  providerTracked: true,
  outputHashTracked: true,
  generatedAssetNeverOverwritesSource: true
} as const;
