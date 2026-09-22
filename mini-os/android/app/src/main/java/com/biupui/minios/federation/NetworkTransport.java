package com.biupui.minios.federation;

import java.io.IOException;
import java.util.Map;

public interface NetworkTransport {
    NetworkResponse executeGet(String url, Map<String, String> headers) throws IOException;
    final class NetworkResponse {
        private final int statusCode;
        private final String body;
        public NetworkResponse(int statusCode, String body) { this.statusCode=statusCode; this.body=body; }
        public int statusCode(){ return statusCode; }
        public String body(){ return body; }
    }
}
