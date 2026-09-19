export const API_VERSION="1.0";
export const API_PREFIX="/v1";
export function apiHeaders(res){res.setHeader("X-Biupiu-API-Version",API_VERSION);res.setHeader("Cache-Control","no-store")}