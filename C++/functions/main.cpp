#include <iostream>

// A function prototype.
// Generally, all your function prototypes (declarations) will be in a header file
// which you include (like iostream above).
// Without first declaring this function, you can't use it in main because the compiler
// doesn't know what arg types it expects and returns.  C++ is too type safe to allow that
// kind of looseness.  Python is a different story. . . .
//
// All functions must be declared before you use (call/invoke) them.
// They don't necessarily have to be defined yet though.
int stones2pounds(int);
int furlongs2yards(int);
int years2months(int);
float celsius2fahrenheit(float);
double lightYears2astronomicalUnits(double);
void threeBlindMice(); // In C this would mean unknown args.
void seeHowTheyRun(); // In C++, blank param list mean function takes zero args.

// A niladic procedure more than a function.

// Asks user for a weight in stone.  Converts it to pounds.
int main(int argc, char** argv) {
	// Not that we put the using statement here to avoid polluting the global namespace.
	// Each block scope forms its own little private anonymous namespace.
	using namespace std;
	int stone = 0;
	cout << "Enter the weight in stone: ";
	cin >> stone;
	cin.get(); // Eat the newline.
	int pounds = stones2pounds(stone); // A function call (aka, invocation).
	cout << stone << " stone = ";
	cout << pounds << " pounds." << endl;
	// 4 stone = 56 pounds.

	// Convert furlongs to yards.
	int furlongs = 0;
	cout << "Enter a distance in furlongs: ";
	cin >> furlongs;
	cin.get(); // Eat the newline.
	int yards = furlongs2yards(furlongs);
	// TO DO: A general pluralizer.  This is hard.  Python has one that sort of works.
	cout << furlongs << ((furlongs != 1) ? " furlongs" : " furlong") << " = ";
	cout << yards << " yards." << endl;

	// TO DO: Factor this "prompt for integer" code into its own function.
	int years = 0;
	cout << "How many years old are you? ";
	cin >> years;
	cin.get(); // Eat the newline.
	int months = years2months(years);
	cout << "You are " << months << " months old!" << endl;

	// Convert Celsius to Fahrenheit.
	float celsius = 0.0f;
	cout << "Please enter a Celsius value: ";
	cin >> celsius;
	cin.get();
	float fahrenheit = celsius2fahrenheit(celsius);
	// It appears that by default floats are displayed with no decimal places.	
	cout << celsius << " degrees Celsius is ";
	cout << fahrenheit << " degrees Fahrenheit.";
	cout << endl;

	double lightYears = 0.0;
	cout << "Enter light years: ";
	cin >> lightYears;
	cin.get();
	double aus = lightYears2astronomicalUnits(lightYears);
	cout << lightYears << " light years = ";
	cout << aus << " astronomical units.";
	cout << endl;

	// Spit out part of a nursery rhyme.
	cout << endl;
	threeBlindMice();
	threeBlindMice();
	seeHowTheyRun();
	seeHowTheyRun();
	
	return 0;
} // main(int, char**)


//=============================================================================
// Global Functions
//=============================================================================

// Definition of previously declared function.
// This function is defined in the global namespace.
// It is generally a bad idea to define anything but main in the global namespace.
// The primary reason the global namespace exists in C++ is for backwards compatibility
// with C.  In C *everything* is definied in the global namespace!
// Functions and objects in the standard library are defined in the std namespace.
// Converts stones to pounds.  A stone is 14 pounds.
int stones2pounds(int stones) {
	int pounds = 14 * stones;
	return pounds;
}


// Converts furlongs to yards.
// (One furlong is 220 yards.)
int furlongs2yards(int furlongs) {
	int yards = 220 * furlongs;
	return yards;
}


// Converts years to months.
int years2months(int years) {
	int months = 12 * years;
	return months;
}


// Converts Fahrenheit temperature to Celsius.
// Fahrenheit = 1.8 × degrees Celsius + 32.0
float celsius2fahrenheit(float c) {
	float f = (1.8f * c) + 32.0f;
	return f;
}

// Converts light years to astronomical units.
// 1 light year = 63,240 astronomical units
double lightYears2astronomicalUnits(double lightYears) {
	double astronomicalUnits = 63240 * lightYears;
	return astronomicalUnits;
}

// A function that returns no value is known as a procedure or subroutine
// in other languages (like Pascal or Basic).
void threeBlindMice() {
	using namespace std;
	cout << "Three blind mice." << endl;
}


// Again we are localizing our using statements to pollute as little namespace
// as possible.  Most code is sloppier than this.  Polluting namespace will probably
// only bite you on fairly large projects.
void seeHowTheyRun() {
	using namespace std;
	cout << "See how they run." << endl;
}

