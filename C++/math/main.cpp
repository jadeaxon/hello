#include <iostream>
#include <cmath>


// Test standard library math functions.
int main(int argc, char** argv) {
	using namespace std;

	// Basic math operators.  We'll do a 9x9 arithmetic "table".
	for (int a = 1; a <= 9; a++) {
		for (int b = 1; b <= 9; b++) {
			cout << a << " + " << b << " = " << a + b << endl;
			cout << a << " - " << b << " = " << a - b << endl;
			cout << a << " * " << b << " = " << a * b << endl;
			cout << a << " / " << b << " = " << a / b << endl;
			cout << a << " % " << b << " = " << a % b << endl; // Modulo (integer division remainder).
		} // next b
	} // next a


	// double sqrt(double)
	double value = 5.0;
	double result = sqrt(value);
	cout << "The square root of " << value << " is " << result << "." << endl;

	// double pow(double, double)
	// Note that 2.0 is a double literal while 2.0f is a float literal.
	result = pow(2.0, 3.0); // 2^3 = 8
	cout << "2^3 == " << result << "." << endl;

	return 0;

} // end main(int, char**)

