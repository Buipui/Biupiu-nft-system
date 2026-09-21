#include "../include/biupiu_visual_native.h"
#include <atomic>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <mutex>
#include <string>
#include <unordered_map>

namespace {
struct Job { std::atomic<uint32_t> state{0}; };
std::mutex jobs_mutex;
std::unordered_map<biupiu_visual_job, Job*> jobs;
std::atomic<uint64_t> next_job{1};

biupiu_visual_status make_job(biupiu_visual_job* out) {
  if (!out) return BIUPIU_VISUAL_INVALID_ARGUMENT;
  auto id=next_job.fetch_add(1);
  auto *j=new Job();
  { std::lock_guard<std::mutex> lock(jobs_mutex); jobs[id]=j; }
  *out=id; return BIUPIU_VISUAL_OK;
}
}

extern "C" biupiu_visual_status biupiu_visual_get_capabilities(biupiu_visual_capabilities* out) {
  if (!out) return BIUPIU_VISUAL_INVALID_ARGUMENT;
  *out={};
  out->api_version=BIUPIU_VISUAL_API_V1;
  out->max_texture_size=16384;
  out->max_msaa_samples=8;
  out->compute=1;
  out->hdr=1;
  return BIUPIU_VISUAL_OK;
}

extern "C" biupiu_visual_status biupiu_visual_render_submit(const biupiu_render_request* r, biupiu_visual_job* out) {
  if (!r || !out || r->width==0 || r->height==0 || r->frame_end<r->frame_start || r->frame_rate<=0) return BIUPIU_VISUAL_INVALID_ARGUMENT;
  return make_job(out);
}
extern "C" biupiu_visual_status biupiu_visual_animation_submit(const biupiu_animation_request* r, biupiu_visual_job* out) {
  if (!r || !out || r->frame_end<r->frame_start || r->frame_rate<=0) return BIUPIU_VISUAL_INVALID_ARGUMENT;
  return make_job(out);
}
extern "C" biupiu_visual_status biupiu_visual_video_submit(const biupiu_video_request* r, biupiu_visual_job* out) {
  if (!r || !out || r->width==0 || r->height==0 || r->frame_end<r->frame_start || r->frame_rate<=0) return BIUPIU_VISUAL_INVALID_ARGUMENT;
  return make_job(out);
}
extern "C" biupiu_visual_status biupiu_visual_job_status(biupiu_visual_job id, uint32_t* out) {
  if (!out) return BIUPIU_VISUAL_INVALID_ARGUMENT;
  std::lock_guard<std::mutex> lock(jobs_mutex);
  auto it=jobs.find(id); if(it==jobs.end()) return BIUPIU_VISUAL_INVALID_ARGUMENT;
  *out=it->second->state.load(); return BIUPIU_VISUAL_OK;
}
extern "C" biupiu_visual_status biupiu_visual_job_cancel(biupiu_visual_job id) {
  std::lock_guard<std::mutex> lock(jobs_mutex);
  auto it=jobs.find(id); if(it==jobs.end()) return BIUPIU_VISUAL_INVALID_ARGUMENT;
  it->second->state.store(3); return BIUPIU_VISUAL_OK;
}
extern "C" biupiu_visual_status biupiu_visual_release(biupiu_visual_handle id) {
  std::lock_guard<std::mutex> lock(jobs_mutex);
  auto it=jobs.find(id); if(it==jobs.end()) return BIUPIU_VISUAL_INVALID_ARGUMENT;
  delete it->second; jobs.erase(it); return BIUPIU_VISUAL_OK;
}
