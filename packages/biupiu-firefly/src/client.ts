import { getFireflyAccessToken, getFireflyAuthConfig } from "./auth.js";

export interface FireflyApiConfig {
  baseUrl?: string;
  clientId?: string;
  fetchImpl?: typeof fetch;
}

export interface FireflyApiResponse {
  jobId?: string;
  statusUrl?: string;
  resultUrl?: string;
  raw: unknown;
}

type JsonRecord = Record<string, unknown>;

const DEFAULT_BASE_URL = "https://firefly-api.adobe.io";

const ENDPOINTS = {
  GENERATE_IMAGE: "/v3/images/generate-async",
  GENERATE_IMAGE5: "/v4/images/generate-async",
  EXPAND_IMAGE: "/v3/images/expand-async",
  FILL_IMAGE: "/v3/images/fill-async",
  OBJECT_COMPOSITE: "/v3/images/generate-object-composite-async",
  SIMILAR_IMAGES: "/v3/images/generate-similar-async",
  UPSCALE: "/v3/images/upscale",
  UPLOAD_ASSET: "/v2/storage/image",
  GENERATE_VIDEO: "/v3/videos/generate"
} as const;

function extractJobId(payload: JsonRecord): string | undefined {
  if (typeof payload.jobId === "string") return payload.jobId;
  const links = payload.links;
  if (links && typeof links === "object") {
    const result = (links as JsonRecord).result;
    if (result && typeof result === "object" && typeof (result as JsonRecord).href === "string") {
      const href = (result as JsonRecord).href as string;
      const match = href.match(/\/status\/(.+)$/);
      return match?.[1] || href;
    }
  }
  return undefined;
}

function extractStatusUrl(payload: JsonRecord): string | undefined {
  const links = payload.links;
  if (links && typeof links === "object") {
    const result = (links as JsonRecord).result;
    if (result && typeof result === "object" && typeof (result as JsonRecord).href === "string") {
      return (result as JsonRecord).href as string;
    }
  }
  return undefined;
}

export class FireflyApiClient {
  private readonly baseUrl: string;
  private readonly clientId?: string;
  private readonly fetchImpl: typeof fetch;

  constructor(config: FireflyApiConfig = {}) {
    const auth = getFireflyAuthConfig();
    this.baseUrl = (config.baseUrl || "https://firefly-api.adobe.io").replace(/\/$/, "");
    this.clientId = config.clientId || auth?.clientId;
    this.fetchImpl = config.fetchImpl || fetch;
  }

  async health(): Promise<{ configured: boolean; provider: "adobe-firefly"; baseUrl: string }> {
    return {
      configured: Boolean(getFireflyAuthConfig() && this.clientId),
      provider: "adobe-firefly",
      baseUrl: this.baseUrl
    };
  }

  async submit(
    operation: keyof typeof ENDPOINTS,
    payload: JsonRecord,
    options: { modelVersion?: string } = {}
  ): Promise<FireflyApiResponse> {
    const auth = await getFireflyAccessToken();
    if (!this.clientId) throw new Error("Firefly Client ID is not configured.");

    const path = ENDPOINTS[operation];
    const headers: Record<string, string> = {
      Authorization: `${auth.tokenType} ${auth.accessToken}`,
      "x-api-key": this.clientId,
      "Content-Type": "application/json",
      Accept: "application/json"
    };

    if (options.modelVersion) headers["x-model-version"] = options.modelVersion;

    const response = await this.fetchImpl(`${this.baseUrl}${path}`, {
      method: "POST",
      headers,
      body: JSON.stringify(payload)
    });

    const raw = await response.json().catch(() => ({}));
    if (!response.ok) {
      const body = raw as JsonRecord;
      const code = typeof body.error_code === "string" ? body.error_code : "firefly_api_error";
      const accessError = response.headers.get("x-access-error");
      throw new Error(
        `Firefly API ${response.status} ${code}${accessError ? ` (${accessError})` : ""}`
      );
    }

    const json = raw as JsonRecord;
    return {
      jobId: extractJobId(json),
      statusUrl: extractStatusUrl(json),
      resultUrl: extractStatusUrl(json),
      raw
    };
  }

  async getJob(jobId: string): Promise<unknown> {
    const auth = await getFireflyAccessToken();
    if (!this.clientId) throw new Error("Firefly Client ID is not configured.");

    const target = jobId.startsWith("http")
      ? jobId
      : `${this.baseUrl}/v3/status/${encodeURIComponent(jobId)}`;

    const response = await this.fetchImpl(target, {
      method: "GET",
      headers: {
        Authorization: `${auth.tokenType} ${auth.accessToken}`,
        "x-api-key": this.clientId,
        Accept: "application/json"
      }
    });

    const raw = await response.json().catch(() => ({}));
    if (!response.ok) {
      const body = raw as JsonRecord;
      const code = typeof body.error_code === "string" ? body.error_code : "firefly_job_error";
      throw new Error(`Firefly job request ${response.status} ${code}`);
    }

    return raw;
  }

  async uploadImage(
    data: ArrayBuffer | Uint8Array | Blob,
    contentType: "image/jpeg" | "image/png" | "image/webp" | "image/tiff" | "image/jxl"
  ): Promise<unknown> {
    const auth = await getFireflyAccessToken();
    if (!this.clientId) throw new Error("Firefly Client ID is not configured.");

    const response = await this.fetchImpl(`${this.baseUrl}${ENDPOINTS.UPLOAD_ASSET}`, {
      method: "POST",
      headers: {
        Authorization: `${auth.tokenType} ${auth.accessToken}`,
        "x-api-key": this.clientId,
        "Content-Type": contentType,
        Accept: "application/json"
      },
      body: data
    });

    const raw = await response.json().catch(() => ({}));
    if (!response.ok) {
      const body = raw as JsonRecord;
      const code = typeof body.error_code === "string" ? body.error_code : "firefly_upload_error";
      throw new Error(`Firefly upload ${response.status} ${code}`);
    }

    return raw;
  }
}

export const FIREFLY_API_ENDPOINTS = ENDPOINTS;
