"""Governed native adapter catalog built from internal contracts plus external harvest.

The registry describes interoperability surfaces without copying third-party
implementation code. External adapters remain candidate/reference until normal
promotion evidence gates pass.
"""
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class AdapterSpec:
    adapter_id:str
    family:str
    protocol:str
    role:str
    capabilities:Tuple[str,...]
    source_url:str
    licence_note:str
    status:str="CANDIDATE"
    executable_promotion_allowed:bool=False

USABLE_ADAPTERS=(
    AdapterSpec("mqtt-5","iot","MQTT 5","device/event transport",("pubsub","telemetry","commands","retained-state"),"https://mqtt.org/","standard/protocol; implementation-specific licence"),
    AdapterSpec("eclipse-ditto","digital-twin","HTTP/MQTT/Kafka/AMQP","digital-twin connectivity",("desired-reported-state","twin-events","payload-mapping","access-control"),"https://eclipse.dev/ditto/","Eclipse project; verify component licence before dependency promotion"),
    AdapterSpec("opcua-pubsub","industrial","OPC UA PubSub","industrial data/telemetry",("information-model","pubsub","industrial-telemetry","machine-capability"),"https://opcfoundation.org/","specification/SDK dependent; verify implementation licence"),
    AdapterSpec("ros2-dds","robotics","ROS 2 / DDS","robotics federation",("topics","services","actions","robot-state","simulation-bridge"),"https://www.ros.org/","ROS 2 ecosystem; verify selected DDS/runtime component licences"),
    AdapterSpec("openusd","world","OpenUSD","scene/digital-world interchange",("scene-graph","assets","simulation-scenes","cross-tool-interchange"),"https://openusd.org/","Open-source project; verify component licence/version"),
    AdapterSpec("fmi-fmu","simulation","FMI","model-exchange/co-simulation",("model-exchange","co-simulation","tool-interchange","parameterisation"),"https://fmi-standard.org/","standard; FMU implementation licences vary"),
    AdapterSpec("flower","federated-ml","Flower","federated learning",("federated-training","federated-analytics","simulation","strategy-plug-ins"),"https://flower.ai/","open-source framework; verify release/dependency licences"),
    AdapterSpec("nvflare","federated-ml","NVIDIA FLARE","federated learning",("privacy-preserving-fl","workflow","multi-party-training","simulation"),"https://developer.nvidia.com/flare","open-source SDK; verify release/dependency licences"),
    AdapterSpec("opentelemetry","observability","OpenTelemetry","trace/metric/log correlation",("trace-context","correlation","telemetry","semantic-events"),"https://opentelemetry.io/","open-source project; verify selected SDK/exporter licences"),
    AdapterSpec("a2a","agent-federation","A2A","agent-to-agent interoperability",("agent-discovery","task-routing","cross-agent-communication"),"https://a2a-protocol.org/","open standard/project; verify implementation licence"),
    AdapterSpec("opensharing","ai-assets","OpenSharing","AI asset/data exchange",("model-sharing","agent-skills","data-exchange","cross-platform-assets"),"https://www.linuxfoundation.org/projects/opensharing","open project; verify implementation/dependency licences"),
    AdapterSpec("autosar-capi","automotive","AUTOSAR Adaptive CAPI","automotive middleware reference",("communication","execution-management","logging","diagnostics"),"https://www.autosar.org/capi","partner/source-access conditions apply; reference/candidate only"),
)

def adapter_ids()->Tuple[str,...]:
    return tuple(sorted(a.adapter_id for a in USABLE_ADAPTERS))

def adapters_for_family(family:str)->Tuple[AdapterSpec,...]:
    key=str(family).strip().lower()
    return tuple(a for a in USABLE_ADAPTERS if a.family==key)

def promotion_safe(adapter:AdapterSpec,*,provenance:bool,licence:bool,security:bool,build:bool,regression:bool,runtime:bool,human_approved:bool)->bool:
    """Fail closed: registry presence/evidence cannot override adapter policy."""
    return bool(adapter.executable_promotion_allowed and adapter.status=="VERIFIED_WORKING" and all((provenance,licence,security,build,regression,runtime,human_approved)))
