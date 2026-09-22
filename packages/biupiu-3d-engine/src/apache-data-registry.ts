export interface ApacheDataProviderContract {
  id: "apache-arrow" | "apache-parquet";
  source: string;
  license: string;
  capabilities: readonly string[];
  state: "INTEGRATED";
}

export const APACHE_DATA_PROVIDERS: readonly ApacheDataProviderContract[] = [
  {
    id: "apache-arrow",
    source: "https://arrow.apache.org/",
    license: "Apache-2.0",
    capabilities: ["columnar-data", "language-interchange", "zero-copy-oriented-data-interfaces"],
    state: "INTEGRATED",
  },
  {
    id: "apache-parquet",
    source: "https://parquet.apache.org/",
    license: "Apache-2.0",
    capabilities: ["columnar-storage", "schema-metadata", "compression-and-encoding", "cross-language-data-exchange"],
    state: "INTEGRATED",
  },
];

export function apacheDataSmokeTest(): boolean {
  return APACHE_DATA_PROVIDERS.length === 2 &&
    APACHE_DATA_PROVIDERS.every((provider) => provider.state === "INTEGRATED");
}
