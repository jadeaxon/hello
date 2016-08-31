// Simplest program in C.
// 
// The #include line is a preprocessor directive.
// It means to include the text of the given file here.
// The <> mean that the enlosed file should be searched for along an include path.
// If you use "" instead, it will search as a path relative to this file's directory.
// One way to add to the include path is via the -I option to the GNU C compiler (gcc).
//
// Often, the .h is left off (of the include).  Does it mean anything different that way?
//
// To build (compile) this program, you will need the GNU C compiler (or other ANSI C compiler).
// The simplest way to build it is
// gcc hello_word.c
// [Note that g++ is the GNU C++ compiler.]
//
// On a Windows machine (Cygwin), this will produce a.exe.  On a Linux machine, a.out.  You can then
// run that program from Bash using
// ./a.exe
// ./a.out
//
// Chances are, you want to call your program 'hello_world' instead of 'a.out'.  Do this:
// gcc hello_world.c -o hello_world
//
// Notice that C compiles to a binary executable specific to the type of machine it is compiled on.
// A C program compiled for one CPU architecture will not run on another.  You have to recompile for each
// different architecture.  This is known as porting a program.
// To see the type of binary file you have created, type
// file hello_world
//
// The executable binary created by the compiler should have its execute file permission set.  
// If it does not:
// chmod 755 hello_world
//
// Once you deploy your program, you won't want to have to type ./hello_world to invoke it (or its full path).
// To avoid that, you should copy the program to ~/bin (if only you intend to use it).  Or, /usr/local/bin (if you
// intend other people to use it).  Now, in your ~/.bashrc, add those directories to your PATH environment variable.
// export PATH="$PATH":/usr/local/bin:~/bin
//
// Now, next time you log in, you can just say this to run your program:
// hello_world
//
// With the right compiler, it is possible to compile source code into a binary format that targets (runs on)
// a different CPU architecture.  This is know as cross-compiling.
//
// Once your programs get more complicated and use multiple source files and third party libraries, you'll want to
// start automating the build process via GNU make.  Also, you'll want to use something like Subversion or Git for
// source code management (SCM).  If you get multiple projects going and have a team of developers, you'll want a
// continuous integration (CI) server like Jenkins.
//
// You may also want to use more modern build tools: Ant, Maven, Gradle.
//
// As your projects get huge, you'll want to look at code generation.

// #include <stdio>
#include <stdio.h>
// #include "stdio.h"

// A .h file is a header file.  A header file typically declares the interface of a library/module.
// The .c file assosciated with an .h file typically implements the declared interface.

// The special function 'main' is where execution begins in your program.
// A function has a return type (implicitly void), a name, a parameter list, and a body.
// The function body is enclosed by { }.  It consists of 0..* statements.
main() {
	// printf is a function from stdio, the C Standard Input/Output Library.
	// Statements are terminated by a semi-colon.
	// This statement is a function call.
	// To call a function, you say <function_name>(<argument>...).
	// The argument types must match the parameter types.
	// Think of a parameter as a name of a role and an argument as an actual thing/value filling that role.
	// Here, the argument is a C string literal.  C strings are null-terminated byte character arrays essentially.
	// Double quotes create C string literals.
	// Within a string literal, a backslash escaped character has special meaning.
	// \n means newline character, which is ASCII 10 decimal.
	//
	// What character encodings can you write ANSI C in?  Unicode?  ASCII?  Latin1?
	// In general, try to write all your code in UTF-8.
	// In Vim:
	// :set encoding=utf-8
	// :set fileencoding=utf-8
	printf("Hello, world!\n");

} // main()



