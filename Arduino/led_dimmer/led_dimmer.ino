const int PIN = 13;

// Sets up output pin and serial comms.
void setup() {
	Serial.begin(9600);
  pinMode(PIN, OUTPUT);
  Serial.println("Enter voltage between 0.0 and 5.0:");
}

// Dims the LED up and down like an emergency flasher.
void loop() {
  static float volts = 0.0;
  static float delta = 0.01;
  
  int pwmValue = (volts * 255.0) / 5.0;
  analogWrite(PIN, pwmValue);
  delay(3);
  if (volts >= 5.0) {
    delta = -0.01;   
  }
  else if (volts <= 0.0) {
    delta = 0.01;
  }
  volts += delta;
} // loop()


// Switches pulse width depending on input via serial port.
void loop2() {
	if ( Serial.available() ) {
		float volts = Serial.parseFloat();
		// PWM is pulse width modulation.  Basically, instead of leaving a signal on, you rapidly turn it on and then off like 500 times per second.
    // The fraction of the amount of time it is on each cycle is the pulse width (duty cycle).
    // The pin is capable of 255 different pulse widths.
		int pwmValue = (volts * 255.0) / 5.0;
    Serial.println(pwmValue);

    // Certain pins can output PWM signal instead of just low or high.
    // This allows you to reduce the average power out on the pin thus acting like a dimmer.
    // Looks like you must use analogWrite() to use an otherwise digital pin's PWM capability.
		analogWrite(PIN, pwmValue);
		
	} // serial input available
} // loop()




