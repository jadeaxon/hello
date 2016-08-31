

// Note that this would be '#include <stdlib.h>' in C.
// In C++, you take the C Standard Library headers and prefix them with 'c'.
#include <cstdlib> // Declare "system()"

#include <iostream>

// On some machines, the value returned by system is 256 * exit status (or perhaps some other
// such nonsense).  To get the right value, you need to use a macro defined in this header.
#include <sys/wait.h>

using namespace std;


int main() {
	system("echo 'Hello, world!'");

	int status = system("exit 1");
	cout << status << endl;
	status = WEXITSTATUS(status);
	cout << status << endl;

	// If you need to build up a more complex command, use a string, stringstream, a QString,
	// or sprintf on a C string.
	
	// Q. Can we start a background process with system?
	// A. Yes, indeed, we can.
	cout << "Should block." << endl;
	system("sleep 5");
	cout << "Should not block." << endl;
	system("sleep 5 &");
	cout << "This should appear immediately." << endl;


} // main()

