const assert = require("assert");
const {DIMENSIONS,archiveUnit,snapshot,scaleSynthetic,featureVector} =
  require("../software/information-growth/information_growth_engine");

describe("Biupiu multidimensional information growth engine", function () {
  it("exposes the canonical dimensions", function () {
    assert.equal(DIMENSIONS.length,12);
    assert.ok(DIMENSIONS.includes("quantum"));
    assert.ok(DIMENSIONS.includes("digital_twin"));
  });
  it("creates governed archive units", function () {
    const u=archiveUnit({id:"a"},{knowledge:{topic:"x"}});
    assert.equal(u.archive_unit_id,"a");
    assert.equal(u.evidence_state,"DISCOVERED");
    assert.equal(u.validation_state,"PENDING");
  });
  it("scales monotonically at 10, 100 and 1000 units", function () {
    const m=[10,100,1000].map(n=>scaleSynthetic(n).metrics);
    assert.deepEqual(m.map(x=>x.archive_units),[10,100,1000]);
    assert.deepEqual(m.map(x=>x.graph_nodes),[10,100,1000]);
    assert.ok(m[2].graph_edges>m[1].graph_edges);
  });
  it("measures graph and metadata density", function () {
    const m=scaleSynthetic(50).metrics;
    assert.ok(m.metadata_density>0);
    assert.ok(m.graph_density>=0);
  });
  it("keeps a fixed-width ML feature vector", function () {
    const v=featureVector(scaleSynthetic(25).metrics);
    assert.equal(v.length,8);
    assert.ok(v.every(Number.isFinite));
  });
  it("computes incremental growth", function () {
    const previous=scaleSynthetic(100).metrics;
    const current=snapshot(scaleSynthetic(150).units,previous);
    assert.equal(current.growth_rate,0.5);
  });
  it("rejects negative scale", function () {
    assert.throws(()=>scaleSynthetic(-1),/non-negative/);
  });
  it("does not treat metadata as validation", function () {
    assert.equal(archiveUnit({id:"x"},{knowledge:{claim:"x"}}).validation_state,"PENDING");
  });
});
