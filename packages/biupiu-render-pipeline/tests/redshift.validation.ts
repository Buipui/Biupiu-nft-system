import {
  REDSHIFT_OSL_VALIDATION_SET,
  validateRedshiftEnvironment
} from "../src/redshift";

const blocked = validateRedshiftEnvironment({
  host: "UNKNOWN",
  hostVersion: null,
  redshiftVersion: null,
  device: {
    kind: "UNKNOWN",
    name: null,
    vramGb: null,
    driver: null
  },
  detected: false
});

if (blocked.status !== "BLOCKED") {
  throw new Error("RED-03 expected an unconnected environment to fail closed as BLOCKED.");
}

if (!REDSHIFT_OSL_VALIDATION_SET.includes("SpaceTransform.osl")) {
  throw new Error("Redshift OSL validation set is incomplete.");
}

const ready = validateRedshiftEnvironment({
  host: "CINEMA_4D",
  hostVersion: "TEST",
  redshiftVersion: "TEST",
  device: {
    kind: "NVIDIA",
    name: "TEST GPU",
    vramGb: 16,
    driver: "TEST"
  },
  detected: true
});

if (ready.status !== "PASS") {
  throw new Error("RED-03 expected a fully detected environment to pass the environment contract.");
}
