const int PIN = 3;
const int ON_PIN = 13;

void setup() {
	pinMode(PIN, INPUT);
  
  // If you run a jumper wire from this pin to the input pin, 1 will start appearing in the serial output.
  pinMode(ON_PIN, OUTPUT);
  digitalWrite(ON_PIN, HIGH);
	
	Serial.begin(9600);
}

// Polls a digital input pin every second.
void loop() {
	// Anything below 2.5V is considered off (0).
	// Anything 2.5V and above is considered on (1).
	int value = digitalRead(PIN);
	Serial.println(value);
	delay(1000);
}

