const int PIN = 13;

// Sets up output pin and serial comms.
void setup() {
	Serial.begin(9600);
  pinMode(PIN, OUTPUT);
}

// Dims the LED up and down like an emergency flasher.
void loop() {
  int pulse_width = random(0, 256);
  int duration = random(100, 301);
  int pause = random(10, 101);
  
  analogWrite(PIN, pulse_width);
  delay(duration);
  analogWrite(PIN, 0);
  delay(pause);
  
} // loop()






