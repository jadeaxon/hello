/*

Note that gcc is the GNU C Compiler whereas g++ is the GNU C++ Compiler.
Therefore, you must compile this with g++, not gcc.

.cpp is the filename extension for C++ files.

To build and run (do this from bash/mintty/Cygwin):

$ indicates a bash shell prompt.  It is not part of the command to type.

$ cd <directory containing this file>
$ g++ hello_world -o hello_world
[$ chmod 755 hello_world.exe]
$ ./hello_world.exe
Hello, world!

By default, g++ will write the executable to a.exe.  The -o option overrides this.  It automatically appends the .exe
extension.  Not sure how to override that behaviour.

Must use ./hello_world.exe unless . is in your path.  Even then, better to use ./ so you know you are actually executing
the executable you just built.

If your PATHEXT environment variable contains .EXE, you can run the file via ./hello_world (no .exe needed).

g++ appears to give execute permission to the executable it builts by default.  Do chmod just in case.

PATH environment variable should contain /usr/bin.  The /usr/bin directory should contain g++.

Note that I installed *all* Cygwin packages.

$ which g++
$ file hello_world.exe
/usr/bin

$ uname -a
CYGWIN_NT-6.0 Bitrealm 1.7.9(0.237/5/3) 2011-03-29 10:10 i686 Cygwin

hello_world.exe: PE32 executable (console) Intel 80386, for MS Windows

*/


// Lines beginning with # are preprocessor/compiler directives.  They are not actual parts of the program.  They specify
// how the program should be compiled.  So, they are compile time code statements vs. runtime code.
//
// Includes the stream IO standard library.
// When you use <includefile>, g++ searches various directories in a specific order for a file named includefile.h. 
#include <iostream>

// This makes it so you can say 'cout' instead of 'std::cout'.
// All elements of the C++ standard library are defined in namespace std.
using namespace std;

// All C++ programs start execution in a function called main that returns an int value.
int main() {
    // Write the string literal to stream cout which is linked to stdout.
    cout << "Hello, world!";

    // The return value is the process exit status.  An exit status of zero means normal termination.
    // Any other exit status indicates that an error of some sort occurred.
    return 0;

} // main(...)



