export type Vec3 = [number, number, number];
export interface Box { kind: "box"; size: Vec3; center: boolean; }
export interface Cylinder { kind: "cylinder"; radius: number; height: number; center: boolean; }
export interface Transform { translate?: Vec3; rotateDeg?: Vec3; scale?: Vec3; }
export interface ModelManifest {
  assetId: string; department: string; modelVersion: string;
  sourceFormat: "OPENSCAD" | "FREECAD" | "BLENDER" | "BUILD123D";
  units: "mm" | "m"; primitives: Array<Box | Cylinder>; transforms: Transform[];
  evidenceStatus: "CONCEPT" | "RECONSTRUCTED" | "EXPERIMENTAL" | "VALIDATED";
}
export function validateManifest(m: ModelManifest): string[] {
  const errors: string[] = [];
  if (!m.assetId.trim()) errors.push("assetId is required");
  if (!m.department.trim()) errors.push("department is required");
  if (!/^v\d+\.\d+$/.test(m.modelVersion)) errors.push("modelVersion must use vMAJOR.MINOR");
  if (m.primitives.length === 0) errors.push("at least one primitive is required");
  for (const [i,p] of m.primitives.entries()) {
    const dims = p.kind === "box" ? p.size : [p.radius, p.height];
    if (dims.some(v => !Number.isFinite(v) || v <= 0)) errors.push(`primitive ${i} contains invalid dimensions`);
  }
  return errors;
}
export function toOpenScad(m: ModelManifest): string {
  const errors = validateManifest(m);
  if (errors.length) throw new Error(errors.join("; "));
  const lines = [`// BIUPIU GENERATED MODEL — ${m.assetId} ${m.modelVersion}`, `// Department: ${m.department} | Evidence: ${m.evidenceStatus} | Units: ${m.units}`, "union() {"];
  for (const p of m.primitives) {
    if (p.kind === "box") lines.push(`  cube([${p.size[0]}, ${p.size[1]}, ${p.size[2]}], center=${p.center ? "true" : "false"});`);
    else lines.push(`  cylinder(r=${p.radius}, h=${p.height}, center=${p.center ? "true" : "false"}, $fn=96);`);
  }
  lines.push("}"); return lines.join("\n");
}
export function boundingRadius(m: ModelManifest): number {
  return Math.max(...m.primitives.map(p => p.kind === "box" ? Math.hypot(p.size[0], p.size[1], p.size[2]) / 2 : Math.hypot(p.radius, p.radius, p.height / 2)));
}