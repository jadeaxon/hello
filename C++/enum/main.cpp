#include <iostream>

using namespace std;

// Enumerations are basically type-safer sets of related constants. 
// Alternative to using #defines or a bunch const ints.
// A shortcut to having your own class that really has constant instances defined.
// Enumeration => enumerated type => a type where all instances have been accounted for.

// The whole thing is an enumeration.
// Each value is an enumerator.
// First value is assigned 0 by default.  Others increment by 1 by default.
// Multiple enumerators may have the same value (these act as synonymns).
enum Color {red, orange, yellow, green, blue, violet, indigo, ultraviolet};

int main(int argc, char* argv[]) {
	Color color = red;
	Color color2 = blue;
	color2 = color;

	// color = 0; // No!  You can't assign an int to an enumerated type.

	cout << color << endl;


} // main(...)



