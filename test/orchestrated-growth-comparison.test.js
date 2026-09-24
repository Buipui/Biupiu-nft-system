const assert=require("assert");
const {LANES,comparison}=require("../software/information-growth/orchestrated_growth_comparison");

describe("Digital Orchestra growth comparison",function(){
  it("contains four governed comparison lanes",function(){
    assert.deepEqual(Object.keys(LANES).sort(),["ALL_TOGETHER","NATIVE_INDIVIDUAL","NATIVE_MATH_GEOMETRY_ML","QUANTUM_FEDERATION"].sort());
  });
  it("produces comparable vectors at every scale",function(){
    const rows=comparison([10,100,1000]);
    assert.equal(rows.length,12);
    assert.ok(rows.every(r=>r.feature_vector.length===8));
    assert.ok(rows.every(r=>r.evidence_state==="MODELLED"));
  });
  it("does not claim quantum execution or advantage",function(){
    const q=comparison([100]).find(r=>r.lane===LANES.QUANTUM_FEDERATION);
    assert.equal(q.evidence_state,"MODELLED");
  });
  it("keeps the combined lane comparable without invented gains",function(){
    const c=comparison([100]).find(r=>r.lane===LANES.ALL_TOGETHER);
    assert.equal(c.graph_nodes,100);
    assert.equal(c.graph_edges,198);
  });
});
