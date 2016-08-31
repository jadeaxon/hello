#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;


// Reads an entire file line-by-line into a single string object.
// Then slurps the same file into a vector and adds line numbers.
int main() {
	// Slurp file contents into a string.
	ifstream in("slurp.cpp");
	string s;
	string line;
	while( getline(in, line) ) {
		s += line + "\n";
	} // next line
	
	cout << s;
	in.close();


	// Slurp file contents into a vector so we can individually access each line.
	// Vectors are a template type, thus the <> notation.
	vector<string> v;
	ifstream in2("slurp.cpp"); // Can I reopen an ifstream object?
	
	while( getline(in2, line) ) {
		// Add the line to the end of the vector.
		// That is push it on the back (end) of the vector.
		v.push_back(line); 
	} // next line

	// Add line numbers:
	for(int i = 0; i < v.size(); i++) {
		cout << (i + 1) << ": " << v[i] << endl;
	} // next line
	in2.close(); // This would automatically happen when the stream is destroyed.

} // main()


