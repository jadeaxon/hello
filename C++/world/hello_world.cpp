// To compile this program:
// g++ -o hello_world hello_world.cpp
// g++ is the GNU C++ compiler whereas gcc is the GNU C compiler.

// Include the input/output stream standard library.
// The <> tells the preprocessor to search the include path for this file.
// With "", the preprocessor would search the directory this file is contained in.
#include <iostream>

// In old-style includes, you'd say
// #include <iostream.h>
// This turns out to be equivalent to
// #include <iostream>
// using namespace iostream;
// Generally, you should not do this and use the new form with no .h.

// Makes it so things defined in std namespace are accessible in just this file 
// without fully qualifying them.
using namespace std;

// iostream defines a cout object that is bound to stdout.
// It does not get imported into the current namespace automaticaliy (?).


// Execution starts in the main() function.
// There must be only one.
// It must return int.  This is the exit status back to the OS/shell.
// The braces delineate the body of a function definiton.
// int is the return type.
// 'main' is the name of this function.
// It's parameter list () is empty.  It takes no args.
//
// Usually, the signature for main includes commandline args:
// int main(int argc, char** argv) {
int main() {
	// cout is an object in the std namespace.
	// The std namespace is used by the C++ Standard Library.
	// Without the 'using' statement above, you'd have to say std.cout and std.endl below.
	// cout => console out
	// cout is connected to stdout by default.
	// << is the stream insertion operator. 
	// So, you are inserting a string literal onto the stream cout.
	// The operator returns the stream it just acted on, so you can chain it.
	// So, we insert the string and endl (a newline) into the cout stream.
	// The result is that "Hello, world!" gets printed to the console.
	// Assuming stdout is not redirected by the shell.
	// All statements in C++ end in a semicolon.
	cout << "Hello, world!" << endl;

	// The main function (and only the main function) implicitly returns 0.
	// This becomes the exit status returned to the shell that called this program.
	// Most shells interpret a 0 exit status to mean the program ran successfully.
	// All other exit status values indicate an error.

	// It is useful to comment closing braces so you instantly know what opening brace
	// it matches.
}  // main()



