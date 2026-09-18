export const BIUPIU_APP = "Biupiu Firefly Creative AI";
export const PACKAGE = "@biupiu/firefly";
export const SCOPE = "CREATIVE_AI" as const;

export type FireflyOperation =
  | "GENERATE_IMAGE"
  | "EXPAND_IMAGE"
  | "FILL_IMAGE"
  | "OBJECT_COMPOSITE"
  | "SIMILAR_IMAGES"
  | "UPSCALE"
  | "UPLOAD_ASSET";

export interface FireflyJobRequest {
  operation: FireflyOperation;
  prompt?: string;
  sourceAssetId?: string;
  referenceAssetId?: string;
  aspectRatio?: string;
  outputFormat?: "png" | "jpeg";
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
  "EXPAND_IMAGE",
  "FILL_IMAGE",
  "OBJECT_COMPOSITE",
  "SIMILAR_IMAGES",
  "UPSCALE",
  "UPLOAD_ASSET"
];

export const FIREFLY_PROVENANCE_RULES = {
  researchIdRequiredForResearchAssets: true,
  sourceAssetTracked: true,
  promptTracked: true,
  providerTracked: true,
  outputHashTracked: true,
  generatedAssetNeverOverwritesSource: true
} as const;
