import type { ProviderAdapter, ProviderJobInput, ProviderJobResult } from "./src/provider-adapter";

export interface BlenderExecutionRequest {
  jobId: string;
  sourceAssetIds: string[];
  workflow: string;
  output: string;
  parameters: Record<string, unknown>;
}

export interface BlenderExecutionResponse {
  providerJobId: string;
  state: ProviderJobResult["state"];
  outputAssetIds: string[];
  manifest?: import("./src/interchange").UniversalAssetManifest;
}

export type BlenderExecutor = (
  request: BlenderExecutionRequest
) => Promise<BlenderExecutionResponse>;

/**
 * Transport-agnostic Blender bridge. The host/worker supplies the executor;
 * this package does not launch Blender or carry provider credentials.
 */
export class BlenderAdapter implements ProviderAdapter {
  readonly id = "BLENDER" as const;
  readonly capabilities = [
    "PRODUCT_STILL",
    "DIGITAL_TWIN",
    "CINEMATIC_SHOWREEL",
    "RESEARCH_VISUALIZATION",
    "GLTF",
    "FBX",
    "OBJ",
    "USD"
  ];

  constructor(private readonly executor: BlenderExecutor) {}

  async submit(input: ProviderJobInput): Promise<ProviderJobResult> {
    if (!input.jobId) throw new Error("Blender adapter requires jobId.");
    if (!input.sourceAssetIds.length) {
      throw new Error("Blender adapter requires at least one source asset.");
    }
    const result = await this.executor({
      jobId: input.jobId,
      sourceAssetIds: input.sourceAssetIds,
      workflow: input.workflow,
      output: input.output,
      parameters: input.parameters
    });
    return result;
  }
}
