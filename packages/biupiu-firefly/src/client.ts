import { getFireflyAccessToken, getFireflyAuthConfig } from "./auth.js";

export interface FireflyApiConfig {
  baseUrl?: string;
  clientId?: string;
  fetchImpl?: typeof fetch;
}

export interface FireflyApiResponse {
  jobId?: string;
  statusUrl?: string;
  raw: unknown;
}

type JsonRecord = Record<string, unknown>;

const DEFAULT_BASE_URL = "https://firefly-api.adobe.io";

/**
 * Endpoint inventory aligned to Adobe's current Firefly API OpenAPI 3.0.0
 * specification (ffs-firefly-api/static/firefly-api.json).
 */
const ENDPOINTS = {
  GENERATE_IMAGE: "/v3/images/generate-async",
  GENERATE_IMAGE5: "/v4/images/generate-async",
  SIMILAR_IMAGES: "/v3/images/generate-similar-async",
  EXPAND_IMAGE: "/v3/images/expand-async",
  FILL_IMAGE: "/v3/images/fill-async",
  OBJECT_COMPOSITE: "/v3/images/generate-object-composite-async",
  PRECISE_COMPOSITE: "/v3/images/precise-composite",
  ADAPTIVE_COMPOSITE: "/v3/images/adaptive-composite",
  UPSCALE: "/v3/images/upscale",
  GENERATE_VIDEO: "/v3/videos/generate",
  UPLOAD_ASSET: "/v2/storage/image",
  JOB_STATUS: "/v3/status/",
  CANCEL_JOB: "/v3/cancel/"
} as const;

function extractJobId(payload: JsonRecord): string | undefined {
  if (typeof payload.jobId === "string") return payload.jobId;

  const links = payload.links;
  if (links && typeof links === "object") {
    const result = (links as JsonRecord).result;
    if (result && typeof result === "object") {
      const href = (result as JsonRecord).href;
      if (typeof href === "string") {
        const match = href.match(/\/status\/(.+)$/);
        return match?.[1] || href;
      }
    }
  }

  return undefined;
}

function extractStatusUrl(payload: JsonRecord): string | undefined {
  const links = payload.links;
  if (links && typeof links === "object") {
    const result = (links as JsonRecord).result;
    if (result && typeof result === "object") {
      const href = (result as JsonRecord).href;
      if (typeof href === "string") return href;
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
    this.baseUrl = (config.baseUrl || DEFAULT_BASE_URL).replace(/\/$/, "");
    this.clientId = config.clientId || auth?.clientId;
    this.fetchImpl = config.fetchImpl || fetch;
  }

  async health(): Promise<{
    configured: boolean;
    provider: "adobe-firefly";
    baseUrl: string;
  }> {
    return {
      configured: Boolean(getFireflyAuthConfig() && this.clientId),
      provider: "adobe-firefly",
      baseUrl: this.baseUrl
    };
  }

  async submit(
    operation: Exclude<keyof typeof ENDPOINTS, "JOB_STATUS" | "CANCEL_JOB" | "UPLOAD_ASSET">,
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

    const requiredModelVersions: Partial<Record<keyof typeof ENDPOINTS, string>> = {
      GENERATE_IMAGE5: "image5",
      GENERATE_VIDEO: "video1_standard",
      UPSCALE: "precise_upsampler_v1"
    };
    const requiredModel = requiredModelVersions[operation];
    const modelVersion = requiredModel || options.modelVersion;

    if (requiredModel && options.modelVersion && options.modelVersion !== requiredModel) {
      throw new Error(`Adobe Firefly requires x-model-version=${requiredModel} for ${operation}.`);
    }
    if (modelVersion) headers["x-model-version"] = modelVersion;

    const response = await this.fetchImpl(`${this.baseUrl}${path}`, {
      method: "POST",
      headers,
      body: JSON.stringify(payload)
    });

    const raw = await response.json().catch(() => ({}));
    if (!response.ok) {
      const body = raw as JsonRecord;
      const code =
        typeof body.error_code === "string" ? body.error_code : "firefly_api_error";
      const accessError = response.headers.get("x-access-error");
      throw new Error(
        `Firefly API ${response.status} ${code}${accessError ? ` (${accessError})` : ""}`
      );
    }

    const json = raw as JsonRecord;
    return {
      jobId: extractJobId(json),
      statusUrl: extractStatusUrl(json),
      raw
    };
  }

  async getJob(jobId: string): Promise<unknown> {
    const auth = await getFireflyAccessToken();
    if (!this.clientId) throw new Error("Firefly Client ID is not configured.");

    const target = jobId.startsWith("http")
      ? jobId
      : `${this.baseUrl}${ENDPOINTS.JOB_STATUS}${encodeURIComponent(jobId)}`;

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
      const code =
        typeof body.error_code === "string" ? body.error_code : "firefly_job_error";
      const accessError = response.headers.get("x-access-error");
      throw new Error(
        `Firefly job request ${response.status} ${code}${accessError ? ` (${accessError})` : ""}`
      );
    }

    return raw;
  }

  async cancelJob(jobId: string): Promise<unknown> {
    const auth = await getFireflyAccessToken();
    if (!this.clientId) throw new Error("Firefly Client ID is not configured.");

    const target = jobId.startsWith("http")
      ? jobId.replace("/status/", "/cancel/")
      : `${this.baseUrl}${ENDPOINTS.CANCEL_JOB}${encodeURIComponent(jobId)}`;

    const response = await this.fetchImpl(target, {
      method: "PUT",
      headers: {
        Authorization: `${auth.tokenType} ${auth.accessToken}`,
        "x-api-key": this.clientId,
        Accept: "application/json"
      }
    });

    const raw = await response.json().catch(() => ({}));
    if (!response.ok) {
      const body = raw as JsonRecord;
      const code =
        typeof body.error_code === "string" ? body.error_code : "firefly_cancel_error";
      throw new Error(`Firefly cancel ${response.status} ${code}`);
    }

    return raw;
  }

  async uploadImage(
    data: ArrayBuffer | Uint8Array | Blob,
    contentType: "image/jpeg" | "image/png" | "image/webp" | "image/tiff" | "image/jxl"
  ): Promise<unknown> {
    const auth = await getFireflyAccessToken();
    if (!this.clientId) throw new Error("Firefly Client ID is not configured.");

    const response = await this.fetchImpl(
      `${this.baseUrl}${ENDPOINTS.UPLOAD_ASSET}`,
      {
        method: "POST",
        headers: {
          Authorization: `${auth.tokenType} ${auth.accessToken}`,
          "x-api-key": this.clientId,
          "Content-Type": contentType,
          Accept: "application/json"
        },
        body: data
      }
    );

    const raw = await response.json().catch(() => ({}));
    if (!response.ok) {
      const body = raw as JsonRecord;
      const code =
        typeof body.error_code === "string" ? body.error_code : "firefly_upload_error";
      throw new Error(`Firefly upload ${response.status} ${code}`);
    }

    return raw;
  }
}

export const FIREFLY_API_ENDPOINTS = ENDPOINTS;
export const FIREFLY_API_BASE_URL = DEFAULT_BASE_URL;
