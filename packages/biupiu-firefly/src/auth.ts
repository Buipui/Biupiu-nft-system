export interface FireflyAuthConfig {
  clientId: string;
  clientSecret: string;
  tokenUrl?: string;
  scope?: string;
}

export interface FireflyAccessToken {
  accessToken: string;
  expiresAt: number;
  tokenType: string;
}

const DEFAULT_TOKEN_URL = "https://ims-na1.adobelogin.com/ims/token/v3";
const DEFAULT_SCOPE =
  "openid,AdobeID,session,additional_info,read_organizations,firefly_api,ff_apis";

export function getFireflyAuthConfig(
  env: Record<string, string | undefined> = (() => { const runtime = globalThis as typeof globalThis & { process?: { env?: Record<string, string | undefined> } }; return runtime.process?.env || {}; })()
): FireflyAuthConfig | null {
  const clientId = env.FIREFLY_SERVICES_CLIENT_ID;
  const clientSecret = env.FIREFLY_SERVICES_CLIENT_SECRET;
  if (!clientId || !clientSecret) return null;

  return {
    clientId,
    clientSecret,
    tokenUrl: env.FIREFLY_SERVICES_TOKEN_URL || DEFAULT_TOKEN_URL,
    scope: env.FIREFLY_SERVICES_SCOPE || DEFAULT_SCOPE
  };
}

let cachedToken: FireflyAccessToken | null = null;

export async function getFireflyAccessToken(
  config = getFireflyAuthConfig()
): Promise<FireflyAccessToken> {
  if (!config) {
    throw new Error("Firefly server credentials are not configured.");
  }

  const now = Date.now();
  if (cachedToken && cachedToken.expiresAt - now > 60_000) {
    return cachedToken;
  }

  const body = new URLSearchParams({
    grant_type: "client_credentials",
    client_id: config.clientId,
    client_secret: config.clientSecret,
    scope: config.scope || DEFAULT_SCOPE
  });

  const response = await fetch(config.tokenUrl || DEFAULT_TOKEN_URL, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body
  });

  if (!response.ok) {
    throw new Error(`Adobe IMS token request failed with HTTP ${response.status}.`);
  }

  const payload = (await response.json()) as {
    access_token?: string;
    token_type?: string;
    expires_in?: number;
  };

  if (!payload.access_token || !payload.expires_in) {
    throw new Error("Adobe IMS returned an incomplete access-token response.");
  }

  cachedToken = {
    accessToken: payload.access_token,
    tokenType: payload.token_type || "bearer",
    expiresAt: now + payload.expires_in * 1000
  };

  return cachedToken;
}

export function clearFireflyTokenCache(): void {
  cachedToken = null;
}
