#include <stdio.h>

// Prints out all commandline args (including program name).
main(int argc, char* argv[]) {
	int i = 0;
	for (i = 0; i < argc; i++) {
		printf("argv[%d] = %s\n", i, argv[i]);
	} // next commandline arg
	return 0;
} // main(...)

