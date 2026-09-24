const crypto = require("crypto");

const BEHAVIORS = Object.freeze(["DISTANCE","CONTAINMENT","INTERSECTION","ADJACENCY","SYMMETRY","TOPOLOGY","CURVATURE","TRANSFORM","SCALE","FLOW","COLLISION","NETWORK"]);

function finite(v,name){if(!Number.isFinite(v)) throw new Error(name+" must be finite");return v;}
function point2D(x,y){return{x:finite(x,"x"),y:finite(y,"y")};}
function distance(a,b){return Math.hypot(a.x-b.x,a.y-b.y);}
function orientation(a,b,c){return(b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);}
function polygonArea(poly){if(!Array.isArray(poly)||poly.length<3)throw new Error("polygon requires >= 3 points");let a=0;for(let i=0;i<poly.length;i++){const p=poly[i],q=poly[(i+1)%poly.length];a+=p.x*q.y-q.x*p.y;}return Math.abs(a)/2;}
function centroid(poly){let crossSum=0,cx=0,cy=0;for(let i=0;i<poly.length;i++){const p=poly[i],q=poly[(i+1)%poly.length],c=p.x*q.y-q.x*p.y;crossSum+=c;cx+=(p.x+q.x)*c;cy+=(p.y+q.y)*c;}if(crossSum===0)throw new Error("degenerate polygon");return{x:cx/(3*crossSum),y:cy/(3*crossSum)};}
function boundingBox(poly){return{minX:Math.min(...poly.map(p=>p.x)),maxX:Math.max(...poly.map(p=>p.x)),minY:Math.min(...poly.map(p=>p.y)),maxY:Math.max(...poly.map(p=>p.y))};}
function behaviorSignature({points=[],polygon=null,reference=null,tolerance=1e-9}={}){
 const pts=points.map(p=>point2D(p.x,p.y)),poly=polygon?polygon.map(p=>point2D(p.x,p.y)):null;
 const sig={behaviors:[...BEHAVIORS],coordinate_frame:"2D_CARTESIAN",units:"unspecified",tolerance,point_count:pts.length,polygon_vertex_count:poly?poly.length:0,pairwise_distance_sum:0,orientation_sum:0,area:poly?polygonArea(poly):0,centroid:poly?centroid(poly):null,bounding_box:poly?boundingBox(poly):null,reference_distance:null,invariants:{finite_coordinates:true,non_negative_area:true,translation_invariant_area:true,rotation_invariant_distance:true}};
 for(let i=0;i<pts.length;i++)for(let j=i+1;j<pts.length;j++)sig.pairwise_distance_sum+=distance(pts[i],pts[j]);
 for(let i=0;i+2<pts.length;i++)sig.orientation_sum+=orientation(pts[i],pts[i+1],pts[i+2]);
 if(reference)sig.reference_distance=distance(pts[reference.a],pts[reference.b]);
 return sig;
}
function transformPolygon(poly,{tx=0,ty=0,scale=1,rotation=0}={}){const c=Math.cos(rotation),s=Math.sin(rotation);return poly.map(p=>({x:scale*(p.x*c-p.y*s)+tx,y:scale*(p.x*s+p.y*c)+ty}));}
function behavioralTest(poly){
 const base=behaviorSignature({polygon:poly}),moved=behaviorSignature({polygon:transformPolygon(poly,{tx:17,ty:-9})});
 const p0=behaviorSignature({points:poly}),p1=behaviorSignature({points:transformPolygon(poly,{rotation:Math.PI/3})});
 const scaled=behaviorSignature({polygon:transformPolygon(poly,{scale:2})});
 return{area_translation_delta:Math.abs(base.area-moved.area),distance_rotation_delta:Math.abs(p0.pairwise_distance_sum-p1.pairwise_distance_sum),area_scale_ratio:scaled.area/base.area,invariant_pass:Math.abs(base.area-moved.area)<1e-8&&Math.abs(p0.pairwise_distance_sum-p1.pairwise_distance_sum)<1e-8};
}
function archiveGeometryBehavior(source,geometry={},metadata={}){
 const payload={source,geometry,metadata},id=metadata.id||crypto.createHash("sha256").update(JSON.stringify(payload)).digest("hex").slice(0,16);
 return{geometry_archive_id:id,source,behavior_signature:behaviorSignature(geometry),behavioral_tests:geometry.polygon?behavioralTest(geometry.polygon):null,geometry,metadata,evidence_state:metadata.evidence_state||"MODELLED",validation_state:metadata.validation_state||"PENDING"};
}
module.exports={BEHAVIORS,point2D,distance,orientation,polygonArea,centroid,boundingBox,behaviorSignature,transformPolygon,behavioralTest,archiveGeometryBehavior};
