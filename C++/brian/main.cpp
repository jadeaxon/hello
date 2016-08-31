#include <iostream>
#include <fstream>
#include <string>

#include <fstream> // For ofstream.  Added by Jeff.
#include <cstdlib> // For system(...).  Added by Jeff.

using namespace std;

//purpose: prints string to declared file
//parameters: sentence , file by constant reference
//returns: none
void print(string, const string&);

//purpose: print string to console
//parameters: sentence
//returns:none
void print(string);

//purpose: removes vowels from sentence
//parameters: s
//returns: string s without vowels
string devowel(string);

// Why not capitalize the prompt?
// Didn't compile because missing two includes and botched constructor call.
// Why not put space around operators?
// Why the hell did he use a goto?
// Why use unnecessary system calls to make it non-portable?
// Not bracing all if/then/else uses.
// Why not use something less ugly than that 8 || while condition?
// How do you spell the contraction "don't"?
// Should the first word of a sentence be capitalized?
// When writing English, do you put a space after a comma?


int main () {
	string sentence="";
	char ans ='c';
	string file="";

	// prompt for input
	cout << "please enter a sentence" << endl;
	getline(cin,sentence);
	
	// if invalid input return to here	
	again:
	cout << "would you like to print to file(f) or console(c)?: "; // I had to add the space after the colon.
	cin >> ans;

	// change ans to lowercase
	tolower(ans);

	if (ans == 'c') {
		print(sentence);
	}
	else if (ans == 'f') {
		// prompt for file
		cout << "please enter a file name (dont add an extension. files will be made .txt): ";
		cin >> file;
		// add .txt extension
		file += ".txt";
		print(sentence, file);
	}
	else {
		// The use of system calls here assumes we are running on Windows/DOS.  Not portable.
		cout << "invalid input, try again";
		// system("PAUSE");
		// system("CLS");
		// try ans again
		goto again;
	}

	// system ("PAUSE");
	return 0;
}


void print(string s, const string& f) {
	// declare ofstream
	ofstream out(f.c_str()); // Fixed by Jeff.  There is no ofstream constructor that takes a std::string.
	// call devowel and print to file
	out << devowel(s);
}


void print(string s) {
	// call devowel and print to console
	cout<< devowel(s) << endl;
}


string devowel(string s) {
	// go through string 
	for (int i=0; i<s.size(); i++) {
		// search for vowels
		while(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U') {
			// erase current index
			s.erase(s.begin() + i);
		}
	}
	
	return s;
}


