#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include <cmath>

/*
 Biupiu Native Intelligence Agent — deterministic event boundary.
 It does not autonomously publish, spend, deploy, actuate or promote evidence.
 Every inbound/outbound repository event must be represented by a LearningEvent.
*/
extern "C" {
struct BiupiuLearningEvent {
    uint64_t sequence;
    uint32_t direction;       // 0=inbound, 1=outbound
    uint32_t class_id;        // source/search/simulation/test/failure/update
    const char* source_id;
    const char* content_hash;
    const char* model_version;
    double confidence;
    uint32_t evidence_state;
};

int biupiu_learning_event_validate(const BiupiuLearningEvent* e) {
    if (!e || !e->source_id || !e->content_hash || !e->model_version) return -1;
    if (!*e->source_id || !*e->content_hash || !*e->model_version) return -2;
    if (!std::isfinite(e->confidence) || e->confidence < 0.0 || e->confidence > 1.0) return -3;
    return 0;
}
}
