#define WATER_PIN  7 // D7 pin setup
#define SIGNAL_PIN A5 // Water sensor pin
#define LED 13  // Water sensor LED pin

int value = 0; // variable to store the sensor value

void setup() {
  pinMode(LED, OUTPUT); // declare LED as an output
  pinMode(WATER_PIN, OUTPUT);   // configure water sensor pin as an OUTPUT
  digitalWrite(WATER_PIN, LOW); // turn the sensor OFF
}

void loop() {
  digitalWrite(WATER_PIN, HIGH);  // turn water sensor ON
  value = analogRead(SIGNAL_PIN); // read the analog value from water sensor
  
  if (value > 200) {
    digitalWrite(LED, HIGH); // Turn the LED on
  }
  else {
    digitalWrite(LED, LOW); // Turn the LED off
  }
}
