const int LED_PIN = 13; // Pin 13 is also attached to an on-board LED.
int interval = 500; // How long to leave LED on and off.

// Sets up LED pin to accept output.
void setup() {
  pinMode(LED_PIN, OUTPUT);
}

// Blinks the LED at an increasing rate.  Eventually resets back to slowest rate.
void loop() {
  digitalWrite(LED_PIN, HIGH);
  delay(interval);
  digitalWrite(LED_PIN, LOW);
  delay(interval);
  interval -= 10;
  if (interval < 20) {
    interval = 500;
  }
}

