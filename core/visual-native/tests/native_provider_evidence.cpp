#include "../include/biupiu_visual_provider_validation.h"
#include <fstream>
#include <iomanip>
#include <string>

static const char* result_for(const biupiu_visual_provider_validation& v) {
  if (!v.linked) return "SKIPPED";
  if (!v.runtime_probe || !v.deterministic_pass || !v.repeat_pass) return "FAIL";
  return "PASS";
}

int main(int argc, char** argv) {
  const char* path = argc > 1 ? argv[1] : "provider-evidence.json";
  const char* providers[] = {"OpenUSD", "OpenTimelineIO", "OpenSubdiv", "MaterialX", "OpenColorIO", "OpenImageIO", "OpenEXR"};
  const char input[] = "VIS-NATIVE-18";
  std::ofstream out(path, std::ios::trunc);
  if (!out) return 2;
  out << "{\n  \"schema\": \"biupiu.visual.provider-evidence.v1\",\n  \"gate\": \"VIS-NATIVE-18\",\n  \"providers\": [\n";
  for (unsigned i = 0; i < sizeof(providers)/sizeof(providers[0]); ++i) {
    biupiu_visual_provider_validation v{};
    if (biupiu_visual_provider_validate(providers[i], input, sizeof(input)-1, input, sizeof(input)-1, &v) != 0) return 3;
    if (i) out << ",\n";
    out << "    {\"provider\":\"" << v.provider << "\",\"version\":\"" << v.version
        << "\",\"discovered\":" << static_cast<unsigned>(v.discovered)
        << ",\"linked\":" << static_cast<unsigned>(v.linked)
        << ",\"runtime_probe\":" << static_cast<unsigned>(v.runtime_probe)
        << ",\"deterministic_pass\":" << static_cast<unsigned>(v.deterministic_pass)
        << ",\"repeat_pass\":" << static_cast<unsigned>(v.repeat_pass)
        << ",\"state\":" << static_cast<unsigned>(v.state)
        << ",\"input_hash\":\"0x" << std::hex << v.input_hash
        << "\",\"output_hash\":\"0x" << v.output_hash
        << "\",\"repeat_hash\":\"0x" << v.repeat_hash << std::dec
        << "\",\"result\":\"" << result_for(v) << "\"}";
  }
  out << "\n  ]\n}\n";
  return out.good() ? 0 : 4;
}
