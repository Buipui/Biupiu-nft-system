// Biupiu SF-01 Arduino sensor controller prototype
// Sends one JSON telemetry line per interval over USB serial.

const int SOIL_PIN = A0;
const int LIGHT_PIN = A1;
const unsigned long SAMPLE_MS = 60000UL;

float soilPctFromRaw(int raw) {
  // MUST be replaced with calibrated dry/wet endpoints for the actual soil/sensor.
  const int dry = 800;
  const int wet = 350;
  float pct = 100.0f * (dry - raw) / float(dry - wet);
  if (pct < 0) pct = 0;
  if (pct > 100) pct = 100;
  return pct;
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  int soilRaw = analogRead(SOIL_PIN);
  int lightRaw = analogRead(LIGHT_PIN);
  float soilPct = soilPctFromRaw(soilRaw);

  Serial.print("{\"soil_raw\":"); Serial.print(soilRaw);
  Serial.print(",\"soil_moisture_pct\":"); Serial.print(soilPct, 1);
  Serial.print(",\"light_raw\":"); Serial.print(lightRaw);
  Serial.println("}");

  delay(SAMPLE_MS);
}
