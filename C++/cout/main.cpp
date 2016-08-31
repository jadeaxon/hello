// C++ Standard Library
#include <iostream>
#include <bitset>
#include <string>
#include <sstream> // A string stream.

// C Standard Library
#include <climits> // For CHAR_BIT, number of bits in a byte.

// POSIX
#include <unistd.h> // For usleep(microseconds).

std::string commify(const std::string& input, char separator, int period);


// Demonstrates standard library cout stream.
// std::cout is a output stream tied to stdout.
int main(int argc, char** argv) {
	using namespace std;

	int n = 42;
	const int BITS_PER_INT = CHAR_BIT * sizeof(int);
	bitset<BITS_PER_INT> bits(n);

	cout << "Jeff Anderson" << endl;
	cout << "1546 Westlane Ct." << endl;
	cout << "Provo, UT 84601" << endl;
	cout << "(385) 201-3698" << endl;

	// Display a number in decimal, hexidecimal, and octal forms.
	cout << endl;
	cout << dec << n << endl;
	cout << hex << n << endl;
	cout << oct << n << endl;
	// cout << bin << n << endl; // Nope, there is no 'bin' stream manipulator!
	// DONE: How do we 'commify' a bit set display so space between every octet?
	stringstream ss;
	ss << bits;
	string prettyBits = commify(ss.str(), ' ', 8);
	cout << prettyBits << endl; // Turn number into a bit set instead.
	cout << dec; // Switch cout back to its default: dec.
	cout << endl;

	// Output individual characters.
	char c = 'C';
	cout << c;
	cout.put(c);
	cout << endl; 

	// Outputting a wide character (probably 16-bit Unicode).
	// Must use wcout, not cout.  Normal cout only handles char-based streams.
	// Notice the L"" wide string literal.
	wcout << L"This is a wide character (wchar_t) string literal." << endl; 

	// Here's how we display decimal points on floats.
	double d = 1.234;
	cout.setf(std::ios::fixed); // How do we set this back to truncating?
    cout.precision(2);
    cout << d << endl;


	// TO DO: Put this in its own thread and you have the CLI equivalent of
	// Apple's spinning lollipop and the Windows hourglass.
	// ASCII animation.
	while (true) {
		int t = 100 * 1000; // microseconds
		// Note that \b doesn't actually erase character from screen.
		// It's only when you write a new one that it disappears.
		// So, you can use this trick to ___ underline an input field.
		cout.put('-'); usleep(t); cout.flush(); cout.put('\b'); 
		cout.put('\\'); usleep(t); cout.flush(); cout.put('\b');
		cout.put('|'); usleep(t); cout.flush(); cout.put('\b');
		cout.put('/'); usleep(t); cout.flush(); cout.put('\b');
	} // next animation sequence

	return 0;
} // main(int, char**)


// Commifies a string from right to left.  That is, inserts a separator every nth
// character, like how you'd add commas to a large number.
// 1000000 => 1,000,000
// PRE: period >= 1 (throw IllegalArgumentException).
// TO DO: Factor into digEcor StringUtil class.
// TO DO: Set defaults to ',' and 3.
// TO DO: Add unit tests.
// input - the string to "commify"
// separator - the separator character to use (defaults to a comma)
// period - how often to insert separator (defaults to after every 3rd character)
// direction - whether to start from left or right (not implemented)
std::string commify(const std::string& input, char separator, int period) {
	using namespace std;
	// string commified;
	// string commified(); // You can't init stack variables this way.  Stupid C++!
	// However, if there was an arg to constructor, you'd be okay.
	string commified("");
	int count = 1;
	for (int i = input.size() - 1; i >= 0; i--) {
		char c = input.at(i);
		// commified.append(c); // No append method for std::string!
		commified.push_back(c);

		// Every nth character, insert separator.
		if ( (count % period) == 0 ) {
			commified.push_back(separator);	
		}
		count++;
	} // next character

	return commified;

} // commify(string, char)


