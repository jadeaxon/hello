// The point of this program is to let you switch a pin on and off so you can measure its voltage
// with a multimeter.

const int PIN = 3;

// Sets up output pin and serial comms.
void setup() {
	Serial.begin(9600);
	pinMode(PIN, OUTPUT);

}

// Switches a pin high or low depending on input from user via serial port.
void loop() {
	if ( Serial.available() ) {
		char c = Serial.read();
		if (c == '0') {
			Serial.println("Setting pin low.");
			digitalWrite(PIN, LOW);
		}
		else if (c == '1') {
			Serial.println("Setting pin high.");
			digitalWrite(PIN, HIGH);
		}
		else {
			Serial.println("ERROR: Invalid input.");
		}
	}
}


