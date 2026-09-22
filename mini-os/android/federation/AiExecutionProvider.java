package com.biupiu.minios.federation;

/**
 * Architecture-neutral execution-provider contract.
 * Providers advertise capability; selection never implies runtime verification.
 */
public interface AiExecutionProvider {
    String id();
    AiMultimediaUiFederationRegistry.State state();
    boolean supports(String workload);
}
