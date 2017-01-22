// Inits the serial port.  The Arduino IDE serial monitor default speed is 9600.
void setup() {
  Serial.begin(9600);
  Serial.println("Serial port initialized.");
  
}

// Reports status on the serial port.
void loop() {
  Serial.println("Reporting status on serial port.");
  delay(1000);
}

