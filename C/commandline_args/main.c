#include <stdio.h> // For printf().

// Prints out all commandline args (including program name, the 0th).
//
// Multiword positional args need to be single or double quoted in the shell command.
// E.g., command "this is a single arg"
//
// The raw positional args can be further processed as options.
// Short options (-o) start with a dash.  Long options (--option) start with two dashes.
// An option might have an arg (-o file.ext).
//
// A -- positional arg ends options processing.  All subsequent args are positional args.
// This allows you to pass args that begin with dashes (args that look like options).
//
// Shells like Bash and zsh provide tab completion of arguments.  Args can also be specified via
// history, variable, or command expansion.
//
// xargs can be used to turn the stdout of one command into the args of multiple invocations of
// another command.
//
// Custom default options/args to a command are typically stored in the <COMMAND>_OPTS and
// <COMMAND>_ARGS env vars.  It is up to the command itself to implement this convention.
int main(int argc, char* argv[]) {
	int i = 0;
	for (i = 0; i < argc; i++) {
		printf("argv[%d] = %s\n", i, argv[i]);
	} // next commandline arg
	return 0;
} // main(...)

