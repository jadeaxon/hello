#include <stdio.h>
#include <unistd.h> // For getopt().
#include <stdbool.h> // For bool.

// getopt() parses a single commandline option each time it is called.
// The string you pass it specifies which short options to look for.
// A : following an opt => the opt has an arg.  It gets stored in global optarg.
// getopt() does understand -- by itself.
int main(int argc, char* argv[]) {
	bool opt_a = false;
	bool opt_b = false;
	bool opt_c = false;
	char* c_arg; // The argument for option c.
	bool opt_d = false;

	char opt = '\0';
	while ( (opt = getopt(argc, argv, "abc:d")) != EOF ) {
		switch (opt) {
			case 'a':
				opt_a = true;
				break;
			case 'b':
				opt_b = true;
				break;
			case 'c':
				opt_c = true;
				c_arg = optarg;
				break;
			case 'd':
				opt_d = true;
				break;
			default:
				// Note that getopt() prints its own error message and opt is not set.
				fprintf(stderr, "ERROR: Unknown option %c.\n", opt);
				return 1;

		} // switch
	} // next option

	// optind holds the current index into the raw commandline args.
	// Advance to remaining raw commandline args.
	argc -= optind;
	argv += optind;

	printf("opt_a: %s\n", opt_a ? "true" : "false");
	printf("opt_b: %s\n", opt_b ? "true" : "false");
	printf("opt_c: %s\n", opt_c ? "true" : "false");
	printf("c_arg: %s\n", c_arg);	
	printf("opt_d: %s\n", opt_d ? "true" : "false");

	// Print any raw commandline args that remain after option processing.
	// argv[0] is now the first of remaining args (not this program's name).
	for(int i = 0; i < argc; i++) {
		printf("argv[%d]: %s\n", i, argv[i]);
	} // next arg

} // main()


