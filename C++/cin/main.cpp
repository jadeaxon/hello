// C++ Standard Library
#include <iostream>
#include <string>

// C Standard Library
#include <climits> // For INT_MAX

using namespace std;

// Function prototypes.
void askForTime();
void displayTime(int hours, int minutes);
void askAboutDessert(); // Demonstrates cin.getline(...).


//=============================================================================
// Main
//=============================================================================

// Demonstrates basic use of cin and cout.  Just goes to show the kind of pitfalls
// you can run into in even the simplest of programs.  NOTHING is simple!
int main(int argc, char** argv) {
	askAboutDessert();

	// We could use this here so it only applies to this function vs. whole file.
	// using namespace std;
	
	// Statement declare/define variable of type int named carrots with literal int value 0. 
	int carrots = 0; 

	// endl is a stream manipulator.  It flushes stream whereas \n does not.
	cout << "How many carrots do you have?" << endl;

	// C++ input.  In C, you'd use scanf() and other junk like that.
	// Reads a whole line from stdin.
	// TO DO: How do you respond to individual keystrokes?
	//
	// Wow, for this, it won't accept a single newline!
	// You have to enter a non-blank line!
	// The way the extraction operator works, it *must* read some whitespace-delimited token.
	// cin >> carrots;
	//
	// Not that any non int value you type in is interpreted as value 0.
	// No validation exception is thrown.
	cin >> carrots;

	// The cin >> carrots *only* reads the number from stdin.
	// There is a trailing newline still there that we need to clear.
	// If we don't, then it will be instantly gobbled by the cin.get() below.
	// In that case, there will be no pause before exiting!
	cin.clear(); // Clear an error state.
	cin.ignore(INT_MAX, '\n'); // Ignore all newlines still in stream.
	
	cout << "Here are two more.  ";
	carrots = carrots + 2;

	// You can chain << to concatenate output.
	// << is extensible in that you can overload it in your own classes.
	cout << "Now you have " << carrots << " carrots." << endl;

	askForTime();

	// This is useful if running in a Windows console which would automatically exit
	// at end of program otherwise.
	cout << "Press <Enter> to exit." << endl;
	// cin.flush(); // No such method.
	
	// Huh, this does not cause pause in Debian 7.
	// FIXED: See above.
	// The other solution would have been to simply put two cin.get()s here.
	cin.get(); 

	// return 0; // Implicit (but only in main(...))
} // end main(int, char**)


//=============================================================================
// Global Functions
//=============================================================================

// Asks user to input time and then displays it.
void askForTime() {
	using namespace std;
	
	int hours = 0;
	cout << "Hours? ";
	cin >> hours; // Get one token.
	cin.get(); // Eat newline.
	
	int minutes = 0;
	cout << "Minutes? ";
	cin >> minutes;
	cin.get();

	displayTime(hours, minutes);

} // askForTime()


// Displays times in H:MM form.
void displayTime(int hours, int minutes) {
	cout << hours << ":"; 
	if (minutes < 10) {
		cout << "0"; // Zero pad minutes.
	}
	cout << minutes; 
	cout << endl;
} // displayTime()


// Demonstates cin.getline(...).  This allows you to read a line at a time rather than token
// by token.
void askAboutDessert() {
	using namespace std;
	const int SIZE = 80;
	char name[SIZE];
	char dessert[SIZE];

	cout << "Enter your name:\n";
	// Is the second size arg optional?
	cin.getline(name, SIZE); // reads through newline and consumes it
	
	cout << "Enter your favorite dessert:\n";
	cin.getline(dessert, SIZE);
	// You can also use getline(stream, string) global function.

	// Note that if you try using >> into a char array, cin will give you the first
	// *token* (whitespace separated), not the entire line.
	// cin >> name;
	
	// Does getline(...) and >> work with std::string?  Yes, it does.  Sort of.
	string line;
	string trash;
	cout << "Type a line: ";
	cin >> line;
	getline(cin, trash); // Throw away rest of line.  Yes, this works.
	// Works even if line contained only one word.
	cout << "cin >>: " << line << endl;
	
	cout << "Type a line: ";
	// FAIL: cin.getline(line); // There is no istream.getline(std::string)
	// But, we do have getline(istream, std::string) from <string>.
	
	// So, this is probably the best way to read a line at a time.
	getline(cin, line);
	cout << "getline(istream, string): " << line << endl;
	cout << endl;

	cout << "I have some delicious " << dessert;
	cout << " for you, " << name << ".\n";
} // askAboutDessert()


