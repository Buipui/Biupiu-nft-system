package com.biupiu.minios.federation;

import java.io.IOException;
import java.util.Map;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public final class OkHttpNetworkTransport implements NetworkTransport, ExternalTransportAdapter {
    private final OkHttpClient client;
    public OkHttpNetworkTransport(OkHttpClient client){ if(client==null) throw new IllegalArgumentException("client == null"); this.client=client; }
    public static OkHttpNetworkTransport createDefault(){ return new OkHttpNetworkTransport(new OkHttpClient.Builder().build()); }
    @Override public NetworkResponse executeGet(String url, Map<String,String> headers) throws IOException {
        if(url==null || url.trim().isEmpty()) throw new IllegalArgumentException("url is required");
        Request.Builder b=new Request.Builder().url(url);
        if(headers!=null) for(Map.Entry<String,String> h:headers.entrySet()) if(h.getKey()!=null && h.getValue()!=null) b.header(h.getKey(),h.getValue());
        try(Response r=client.newCall(b.get().build()).execute()){ return new NetworkResponse(r.code(), r.body()==null?"":r.body().string()); }
    }
    @Override public String id(){ return "network.okhttp"; }
    @Override public boolean isAvailable(){ return true; }
    @Override public String diagnosticState(){ return "IMPLEMENTED; centralized OkHttp transport boundary"; }
}
