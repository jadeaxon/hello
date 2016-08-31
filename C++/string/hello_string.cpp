// The C++ string class.  You should use this instead of C strings whenever possible.

#include <string>
#include <iostream>

using namespace std;


int main() {
	// Remember that in C++, you can have stack objects.
	// So, these are not null object refs as they would be in Java.
	// You have to explicitly make a pointer in C++.
	string s1, s2; // Empty strings
	string s3 = "Hello, world!"; // Initialized.
	string s4(" I am"); // Also initialized.
	s2 = "today"; // Assigning to a string.
	s1 = s3 + " " + s4; // Combining strings.
	s1 += " 8 "; // Appending to a string.
	cout << s1 + s2 + "!" << endl;

} // main()
