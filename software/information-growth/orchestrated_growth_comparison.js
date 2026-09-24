const { scaleSynthetic, featureVector } = require("./information_growth_engine");

const LANES = Object.freeze({
  NATIVE_INDIVIDUAL: "native-individual-systems",
  QUANTUM_FEDERATION: "quantum-federation",
  NATIVE_MATH_GEOMETRY_ML: "native-computational-mathematics-geometry-ml",
  ALL_TOGETHER: "all-together-federated"
});

function runLane(lane, count, fanout = 2) {
  const base = scaleSynthetic(count, fanout).metrics;
  return { lane, archive_units:base.archive_units, graph_nodes:base.graph_nodes,
    graph_edges:base.graph_edges, graph_density:base.graph_density,
    metadata_density:base.metadata_density, growth_rate:base.growth_rate,
    feature_vector:featureVector(base), evidence_state:"MODELLED" };
}

function comparison(scales=[10,100,1000]) {
  return scales.flatMap(count => Object.values(LANES).map(lane => runLane(lane,count)));
}
module.exports={LANES,runLane,comparison};
