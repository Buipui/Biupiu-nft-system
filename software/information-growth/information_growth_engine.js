const crypto = require("crypto");

const DIMENSIONS = Object.freeze([
  "identity","knowledge","mathematics","physics","quantum","computation",
  "digital_twin","federation","evidence","temporal","security_trust","blockchain"
]);

function assertFiniteNonNegative(value, name) {
  if (!Number.isFinite(value) || value < 0) throw new Error(name + " must be finite and non-negative");
}

function archiveUnit(source, metadata = {}) {
  if (!source || typeof source !== "object") throw new Error("source object required");
  const id = String(source.id || crypto.createHash("sha256").update(JSON.stringify(source)).digest("hex").slice(0,16));
  const dimensions = Object.fromEntries(DIMENSIONS.map(d => [d, metadata[d] ?? null]));
  const geometry_behavior = geometryBehaviorEnvelope(metadata.geometry_behavior || {});
  return { archive_unit_id:id, source:{...source}, dimensions, geometry_behavior,
    provenance:metadata.provenance || {}, evidence_state:metadata.evidence_state || "DISCOVERED",
    validation_state:metadata.validation_state || "PENDING" };
}

function graphMetrics(units) {
  const nodes = units.length;
  const edges = units.reduce((n,u) => n + (Array.isArray(u.source.relationships) ? u.source.relationships.length : 0), 0);
  return {nodes, edges, graph_density:nodes ? edges/nodes : 0};
}

function snapshot(units, previous = null) {
  const archive_units = units.length;
  const graph = graphMetrics(units);
  const metadata_fields = units.reduce((n,u) => n + Object.values(u.dimensions).filter(v => v !== null).length, 0);
  return {
    source_objects:archive_units, metadata_records:archive_units, archive_units,
    graph_nodes:graph.nodes, graph_edges:graph.edges, graph_density:graph.graph_density,
    metadata_density:archive_units ? metadata_fields/archive_units : 0,
    growth_rate:previous && previous.archive_units ? (archive_units-previous.archive_units)/previous.archive_units : 0
  };
}

function scaleSynthetic(count, relationshipFanout = 2) {
  assertFiniteNonNegative(count, "count");
  assertFiniteNonNegative(relationshipFanout, "relationshipFanout");
  const units = [];
  for (let i=0;i<count;i++) {
    const relationships=[];
    for (let j=1;j<=relationshipFanout;j++) if (i+j<count) relationships.push("unit-"+(i+j));
    units.push(archiveUnit({id:"unit-"+i,relationships},{
      knowledge:{index:i}, mathematics:{index:i%7}, computation:{index:i%5}
    }));
  }
  return {units,metrics:snapshot(units)};
}

function featureVector(metrics) {
  return [metrics.source_objects,metrics.metadata_records,metrics.graph_nodes,metrics.graph_edges,
    metrics.archive_units,metrics.graph_density,metrics.metadata_density,metrics.growth_rate];
}



const SEARCH_HARD_ELEMENTS = Object.freeze(["intent","coordinate_frame","units","relations","invariants","tolerance","transformations","behavioral_tests","provenance","evidence_state"]);
function geometryBehaviorEnvelope(input={}) {
  const applicable = input.applicability || "NONE";
  return {applicability:applicable, ...Object.fromEntries(SEARCH_HARD_ELEMENTS.map(k=>[k,input[k] ?? null]))};
}
module.exports = {DIMENSIONS,SEARCH_HARD_ELEMENTS,geometryBehaviorEnvelope,archiveUnit,graphMetrics,snapshot,scaleSynthetic,featureVector};
