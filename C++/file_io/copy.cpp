#include <string>
#include <fstream> // file stream

using namespace std;


// Copies one file to another, a line at a time.
int main() {
	// Input file stream.
	ifstream in("copy.cpp"); // Open for reading.
	
	// Output file stream.
	ofstream out("copy_of_copy.cpp"); // Open for writing.
	
	string s;
	// getline() will return false if EOF, so works in loop.
	while( getline(in, s) ) { // Discards newline char.
		out << s << "\n"; // So, we must write it back.
	}
} // main()

