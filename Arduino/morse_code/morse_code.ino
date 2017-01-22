const int LED_PIN = 13; // Pin 13 is also attached to an on-board LED.

char* letters[] = { 
	".-", "-...", "-.-.", "-..", ".", "..-.", "--.", // A-G
	"....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", // H-P
	"--.-", ".-.", "...", // Q-S
	"-", "..-", "...-", // T-V
	".--", "-..-", "-.--", "--.." // W-Z
};

char* numbers[] = { 
	"-----", ".----", "..---", "...--", "....-", 
	".....", "-....", "--...", "---..", "----."
};

int dot = 100;
int intraDotDash = dot;
int dash = 3 * dot;
int intraLetter = dash;
int intraWord = dot * 7;

// Sets up LED pin to accept output.
void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}


// Blinks out characters read from serial input as Morse code on the LED.
void loop() {
  char ch; 
  char* seq = 0;
  if (Serial.available() > 0) { 
  	ch = Serial.read(); 
  	if (ch >= 'a' && ch <= 'z') {
  		seq = letters[ch - 'a']; 
  	} 
  	else if (ch >= 'A' && ch <= 'Z') { 
  		seq = letters[ch - 'A'];
  	}
  	else if ( (ch >= '0') && (ch <= '9') ) { 
  		seq = numbers[ch - '0']; 
  	} 
  	else if (ch == ' ') {
  		delay(intraWord - intraLetter);  
  	} 
  } // if serial input
   
  if (seq) {
    Serial.println(seq);
	  flashSequence(seq);
  }
} // loop()


// Flashes a sequence of Morse code symbols on the LED.
void flashSequence(char* s) {
	char c = 0;
	while (c = *s) {
		if (c == '.') {
      flash(dot);
		}
		else if (c == '-') {
			flash(dash);
		}
		else {
			Serial.println("ERROR: Illegal Morse code symbol detected.");
		}
   s++;
	}
	delay(intraLetter);
} // flashSequence(...)


// Flashes LED on then off for some duration of milliseconds.
void flash(int duration) {
  digitalWrite(LED_PIN, HIGH);
  delay(duration);
  digitalWrite(LED_PIN, LOW);
  delay(intraDotDash);
}



