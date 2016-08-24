// Writes a C string (a null-terminate char array) to stdout.

// To use a library, the C compiler (gcc) must know about the interface to the library.
// This interface is defined in the .h header file.
// By default, header files are found in /usr/include/.
// If you need to include headers from some other dir, use -I<include dir> option of gcc.
// The shared/dynamic libs corresponding to the headers are generally found under /usr/lib/.
// The standard C library is implicitly dynamically linked by gcc.
//
// Using strace (system call trace) you can see exactly what dynamic libs are loaded at runtime:
// strace ./hello |& grep lib
// This shows that only libc.so.6 is loaded.  That means multiple headers can refer to same library.
// The reason is it would be unwieldy to pollute your namespace with all the libc functions.
#include <stdio.h> // For puts().
#include <stdlib.h> // For exit().

// To compile: gcc -o hello main.c
// To run: ./hello

// Write a string to stdout using puts() from stdio lib.  It means "put string".
// The entry point to a C program is main().  
// It can take no args.  It must return an int as exit code.
// A zero is returned for success.  A nonzero value is returned for failure.
// Some programs like grep return 1 for a non-error failure (no match found).
int main() {
	puts("Hello, C!"); // Put given string on stdout.
	exit(0); // This would happen implicitly.
} // main()

