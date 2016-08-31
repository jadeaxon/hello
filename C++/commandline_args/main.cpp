// Simlpe demonstration of positional commandline argument handling.

#include <iostream>
using namespace std;

// Simply prints the commandline arguments to stdout.
// argc - argument count; the number of commandline arguments
// Note that this includes the name of the program (as invoked) as the 0th arg.
// So, argc is *always* >= 1.
//
// argv - argument "vector"; an array of arguments a C strings.
// argv[0] is the name of the program as invoked.
// In Windows, ./a.exe becomes ./a (extension is removed).
// Some people embed args into the program name.  For example, you might have the exact same 
// binary executable, but if you invoke it as foo_server vs. foo_client, it will launch as
// a server rather than a client.  That is, you may invoke a process by the role you want it to play.
int main(int argc, char* argv[]) {

	cout << "argc = " << argc << endl;
	for (int i = 0; i < argc; i++) {
		cout << "argv[" << i << "] = " << argv[i] << endl;

	} // next commandline argument


} // main(int, char* [])


// This code does not at all deal with the notion of commandline options.


