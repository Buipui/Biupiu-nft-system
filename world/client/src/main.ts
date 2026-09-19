import {
  ArcRotateCamera,
  Color3,
  Engine,
  HemisphericLight,
  MeshBuilder,
  Scene,
  StandardMaterial,
  Vector3,
} from "@babylonjs/core";
import { DESTINATION_ROUTES, type DestinationId } from "./routeManifest";
import { requestDestination } from "./destinationLoader";

const canvas = document.getElementById("renderCanvas") as HTMLCanvasElement;
const engine = new Engine(canvas, true);
const scene = new Scene(engine);
scene.clearColor = new Color3(0.025, 0.055, 0.045);

const camera = new ArcRotateCamera("hub_camera", -Math.PI / 2, Math.PI / 3, 34, new Vector3(0, 2, 0), scene);
camera.attachControl(canvas, true);
camera.wheelPrecision = 70;
camera.lowerRadiusLimit = 12;
camera.upperRadiusLimit = 70;

new HemisphericLight("hub_light", new Vector3(0, 1, 0), scene).intensity = 1.0;

const ground = MeshBuilder.CreateGround("welcome_plaza", { width: 60, height: 60 }, scene);
const groundMaterial = new StandardMaterial("ground_material", scene);
groundMaterial.diffuseColor = new Color3(0.07, 0.11, 0.09);
ground.material = groundMaterial;

function material(name: string, color: Color3): StandardMaterial {
  const m = new StandardMaterial(name, scene);
  m.diffuseColor = color;
  return m;
}

function gate(routeId: DestinationId, x: number): void {
  const route = DESTINATION_ROUTES.find((item) => item.id === routeId)!;
  const mat = material(route.gate + "_material", new Color3(0.16, 0.24, 0.20));
  const left = MeshBuilder.CreateBox(route.gate + "_left", { width: 1.8, height: 7, depth: 1.8 }, scene);
  left.position = new Vector3(x - 3.2, 3.5, 0);
  left.material = mat;
  const right = left.clone(route.gate + "_right")!;
  right.position.x = x + 3.2;
  const top = MeshBuilder.CreateBox(route.gate + "_top", { width: 8.2, height: 1.5, depth: 1.8 }, scene);
  top.position = new Vector3(x, 6.25, 0);
  top.material = mat;
  top.metadata = { routeId: route.id, route: route.id, departmentScope: route.departmentScope };
}

gate("farming_world", -11);
gate("metal_making_world", 11);

const plaza = MeshBuilder.CreateCylinder("orientation_plaza", { diameter: 14, height: 0.6 }, scene);
plaza.position.y = 0.3;
plaza.material = material("plaza_material", new Color3(0.12, 0.17, 0.14));

const hubMarker = MeshBuilder.CreateCylinder("hub_marker", { diameter: 3, height: 0.5 }, scene);
hubMarker.position.y = 0.8;
hubMarker.material = material("hub_marker_material", new Color3(0.75, 0.56, 0.16));

function routePreview(id: DestinationId): void {
  const result = requestDestination(id, ["subscriber"]);
  console.info("Main Hub route intent", result);
}

routePreview("farming_world");
routePreview("metal_making_world");

engine.runRenderLoop(() => scene.render());
window.addEventListener("resize", () => engine.resize());

console.info("Biupiu Main Hub route-integrated prototype ready", {
  routes: DESTINATION_ROUTES.map((r) => r.id),
});
