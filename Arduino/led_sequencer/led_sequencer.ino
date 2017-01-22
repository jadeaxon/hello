const int LED_PIN = 13; // Pin 13 is also attached to an on-board LED.

// How long to leave LED on and off.  This sequence emits SOS in Morse code.
// If you put exactly even durations, the SOS does not feel human.
int intervals[] = {
	200, 100, 200, 100, 300, 1000, 
	500, 100, 500, 100, 600, 600, 
	200, 100, 200, 100, 300, 2000
}; 
int elements = 0;


// Sets up LED pin to accept output.
void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  elements = sizeof(intervals) / sizeof(int);
  Serial.println(elements);
  Serial.println("====");
  delay(3000);
}


// Blinks out the on/off interval sequence in the intervals array repeatedly. 
// Thus this acts as a basic LED sequencer.
void loop() {
  for (int i = 0; i < elements; i++) {
  	int interval = intervals[i];
    Serial.println(interval);
  	if ((i % 2) == 0) {
  		digitalWrite(LED_PIN, HIGH);
  		delay(interval);
  	}
  	else { // Off interval.
  		digitalWrite(LED_PIN, LOW);
  		delay(interval);
  	}
  } // next interval
  
} // loop()


