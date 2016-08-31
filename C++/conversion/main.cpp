#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

// Function prototypes.
// These are exercises from the book C++ Primer Plus.
void european();
void milesPerGallon();
void population();
void convertInches();
void calculateBMI();
void latitude();
void seconds();


//=============================================================================
// Main
//=============================================================================

// Demonstrates automatic type conversion and type casting.
int main() {
	// Narrowing conversion.
	// But no error.  No warnting.  C++ silently truncates!
	int i1 = 3.9 + 4.2; 
	int i2 = (int) 3.9 + (int) 4.2;
	int i3 = int(3.9) + int(4.2); // Same thing; different cast syntax.

	// cout << setprecision(1); // i is an int, duh.	
	cout << i1 << endl; // 8
	cout << i2 << endl; // 7
	cout << i3 << endl; // 7
	cout << endl;

	european();
	milesPerGallon();
	population();
	seconds();
	latitude();
	calculateBMI();
	convertInches();

} // main()


//=============================================================================
// Functions
//=============================================================================

// Asks user for height in inches.  Convert to feet and inches.  Outputs result.
// Exercise from C++ Primer Plus.
void convertInches() {
	const int INCHES_PER_FOOT = 12;

	int inches = 0;
	int feet = 0;
	int pounds = 0;

	// Won't this just erase the underscores?  No, this actually works.
	cout << "Inches: __\b\b";
	cin >> inches; cin.get(); // Eat newline.
	feet = inches / INCHES_PER_FOOT;
	inches = inches % INCHES_PER_FOOT;

	cout << feet << " ft. " << inches << " in." << endl;
	cout << endl;

} // convertInches()


// Asks user for input.  Calculates body mass index.
void calculateBMI() {
	const int INCHES_PER_FOOT = 12;
	const double METERS_PER_INCH = 0.0254;
	const double POUNDS_PER_KILOGRAM = 2.2;
	
	int inches = 0;
	int feet = 0;
	int pounds = 0;
	
	// Now, calculate the user's BMI.
	cout << "Feet: _\b";
	cin >> feet; cin.get();
	cout << "Inches: __\b\b";
	cin >> inches; cin.get();
	inches = (feet * INCHES_PER_FOOT) + inches;
	cout << "Pounds: ___\b\b\b";
	cin >> pounds; cin.get();

	double meters = inches * METERS_PER_INCH;
	double kilograms = pounds * POUNDS_PER_KILOGRAM;

	// Beware: ^ is the bitwise xor operator.
	double bmi = kilograms / pow(meters, 2); // We could just say meters * meters.
	cout << setprecision(2);
	cout << "BMI = " << bmi << endl;
} // calculateBMI()



// 3. Write a program that asks the user to enter a latitude in degrees, minutes, and sec-
// onds and that then displays the latitude in decimal format.There are 60 seconds of
// arc to a minute and 60 minutes of arc to a degree; represent these values with sym-
// bolic constants.You should use a separate variable for each input value.A sample
// run should look like this:
// Enter a latitude in degrees, minutes, and seconds:
// First, enter the degrees: 37
// Next, enter the minutes of arc: 51
// Finally, enter the seconds of arc: 19
// 37 degrees, 51 minutes, 19 seconds = 37.8553 degrees
void latitude() {
	int degrees = 0;
	int minutes = 0;
	int seconds = 0;

	const int MINUTES_PER_DEGREE = 60;
	const int SECONDS_PER_MINUTE = 60;
	const int SECONDS_PER_DEGREE = SECONDS_PER_MINUTE * MINUTES_PER_DEGREE;

	cout << "37 degrees, 51 minutes, 19 seconds = 37.8553 degrees" << endl;
	cout << "Degrees: ";
	cin >> degrees; cin.get();
	cout << "Minutes: ";
	cin >> minutes; cin.get();
	cout << "Seconds: ";
	cin >> seconds; cin.get();

	double result = 
		(double) degrees + 
		(double) minutes / (double) MINUTES_PER_DEGREE +
		(double) seconds / (double) SECONDS_PER_DEGREE
	;

	cout << setprecision(6); // This is total digits, not just decimal places.
	cout << result << endl;
 
} // latitude()


// Write a program that asks the user to enter the number of seconds as an integer
// value (use type long, or, if available, long long) and that then displays the equiva-
// lent time in days, hours, minutes, and seconds.  Use symbolic constants to represent
// the number of hours in the day, the number of minutes in an hour, and the number
// of seconds in a minute.  The output should look like this:
// Enter the number of seconds: 31600000
// 31600000 seconds = 365 days, 17 hours, 46 minutes, 40 seconds
void seconds() {
	long long seconds = 0;
	cout << "Seconds: ";
	cin >> seconds; cin.get();

	const int SECONDS_PER_MINUTE = 60;
	const int MINUTES_PER_HOUR = 60;
	const int HOURS_PER_DAY = 24;
	const int DAYS_PER_YEAR = 365;

	const int SECONDS_PER_YEAR = 
		DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE;

	const int SECONDS_PER_DAY = 
		HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE;

	const int SECONDS_PER_HOUR = MINUTES_PER_HOUR * SECONDS_PER_MINUTE;

	// If you just defined a bunch of unit conversion rules, they could chain themselves
	// together.

	// Interesting trickle down remainder modulo chain.
	long long years  = seconds / SECONDS_PER_YEAR;
	seconds = seconds % SECONDS_PER_YEAR;
	int days = seconds / SECONDS_PER_DAY;
	seconds = seconds % SECONDS_PER_DAY;
	int hours = seconds / SECONDS_PER_HOUR;
	seconds = seconds % SECONDS_PER_HOUR;
	int minutes = seconds / SECONDS_PER_MINUTE;
	seconds = seconds % SECONDS_PER_MINUTE;

	cout << "years = " << years << endl;
	cout << "days = " << days << endl;
	cout << "hours = " << hours << endl;
	cout << "minutes = " << minutes << endl;
	cout << "seconds = " << seconds << endl;
	cout << endl;

} // seconds()


// Write a program that requests the user to enter the current world population and
// the current population of the U.S. (or of some other nation of your choice). Store
// the information in variables of type long long. Have the program display the per-
// cent that the U.S. (or other nation’s) population is of the world’s population.The
// output should look something like this:
// Enter the world's population: 6898758899
// Enter the population of the US: 310783781
// The population of the US is 4.50492% of the world population.
void population() {
	long long worldPopulation = 0;
	long long usPopulation = 0;

	cout << "World population: ";
	cin >> worldPopulation; cin.get();
	cout << "US population: ";
	cin >> usPopulation; cin.get();

	long double percent = (long double) usPopulation / (long double) worldPopulation;
	percent *= 100;

	cout << setprecision(6);
	cout << "The population of the US is " << percent << "% of the world population.";
	cout << endl;

} // population()


// Write a program that asks how many miles you have driven and how many gallons
// of gasoline you have used and then reports the miles per gallon your car has gotten.
// Or, if you prefer, the program can request distance in kilometers and petrol in liters
// and then report the result European style, in liters per 100 kilometers.
void milesPerGallon() {
	int gallons = 0;
	int miles = 0;

	cout << "Miles: ";
	cin >> miles; cin.get();
	cout << "Gallons: "; 
	cin >> gallons; cin.get();

	double milesPerGallon = (double) miles / (double) gallons;
	cout << setprecision(4);
	cout << "Miles per gallon: " << milesPerGallon << endl;
	cout << endl;

} // milesPerGallon()


// Write a program that asks you to enter an automobile gasoline consumption figure
// in the European style (liters per 100 kilometers) and converts to the U.S. style of
// miles per gallon. Note that in addition to using different units of measurement, the
// U.S. approach (distance / fuel) is the inverse of the European approach (fuel / dis-
// tance). Note that 100 kilometers is 62.14 miles, and 1 gallon is 3.875 liters.Thus, 19
// mpg is about 12.4 l/100 km, and 27 mpg is about 8.7 l/100 km.
void european() {
	int liters = 0;
	int kilometers = 0;

	const float LITERS_PER_GALLON = 3.85f;
	const float KILOMETERS_PER_MILE = 100.0f / 62.14f;

	cout << "Liters: ";
	cin >> liters; cin.get();
	cout << "Kilometers: ";
	cin >> kilometers; cin.get();

	float gallons = liters / LITERS_PER_GALLON;
	float miles = kilometers / KILOMETERS_PER_MILE;
	float milesPerGallon = miles / gallons;

	cout << "Miles per gallon: " << milesPerGallon;
	cout << endl; cout << endl;

} // european()


