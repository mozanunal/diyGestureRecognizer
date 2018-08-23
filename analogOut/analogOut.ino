const int analogInPin0 = A0;
const int analogInPin1 = A1;
const int analogInPin2 = A2;


int sensorValue0 = 0;
int sensorValue1 = 0;
int sensorValue2 = 0;

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(115200);
}

void loop() {
  // read the analog in value:
  sensorValue0 = analogRead(analogInPin0);
  sensorValue1 = analogRead(analogInPin1);
  sensorValue2 = analogRead(analogInPin2);

  // print the results to the Serial Monitor:
  Serial.print(sensorValue0);
  Serial.print(" ");
  Serial.print(sensorValue1);
  Serial.print(" ");
  Serial.print(sensorValue2);
  Serial.println("");
  delay(2);
}
