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

type Destination = {
  id: string;
  label: string;
  position: Vector3;
  route: string;
};

const canvas = document.getElementById("renderCanvas") as HTMLCanvasElement;
const engine = new Engine(canvas, true);
const scene = new Scene(engine);

scene.clearColor = new Color3(0.025, 0.055, 0.045);

const camera = new ArcRotateCamera(
  "hub_camera",
  -Math.PI / 2,
  Math.PI / 3,
  34,
  new Vector3(0, 2, 0),
  scene,
);
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

function gate(id: string, label: string, x: number): Destination {
  const mat = material(id + "_material", new Color3(0.16, 0.24, 0.20));
  const left = MeshBuilder.CreateBox(id + "_left", { width: 1.8, height: 7, depth: 1.8 }, scene);
  left.position = new Vector3(x - 3.2, 3.5, 0);
  left.material = mat;
  const right = left.clone(id + "_right")!;
  right.position.x = x + 3.2;
  const top = MeshBuilder.CreateBox(id + "_top", { width: 8.2, height: 1.5, depth: 1.8 }, scene);
  top.position = new Vector3(x, 6.25, 0);
  top.material = mat;

  const destination = { id, label, position: new Vector3(x, 0, 0), route: id === "farming_gate" ? "farming_world" : "metal_making_world" };
  return destination;
}

const destinations = [
  gate("farming_gate", "FARMING WORLD", -11),
  gate("metallurgy_gate", "METAL MAKING WORLD", 11),
];

const plaza = MeshBuilder.CreateCylinder("orientation_plaza", { diameter: 14, height: 0.6 }, scene);
plaza.position.y = 0.3;
plaza.material = material("plaza_material", new Color3(0.12, 0.17, 0.14));

const hubMarker = MeshBuilder.CreateCylinder("hub_marker", { diameter: 3, height: 0.5 }, scene);
hubMarker.position.y = 0.8;
hubMarker.material = material("hub_marker_material", new Color3(0.75, 0.56, 0.16));

engine.runRenderLoop(() => scene.render());
window.addEventListener("resize", () => engine.resize());

console.info("Biupiu Main Hub prototype ready", { destinations });
