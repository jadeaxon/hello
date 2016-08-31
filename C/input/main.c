#include <stdio.h> // For printf() and scanf().

// Demonstrates basic command line input.
int main(void) {
	char name[40];
	// Prompt for input.  No trailing newline.
	printf("Enter your name: ");
	
	// 39 so there is 1 char left for trailing null char.
	// Reads a formatted input string from stdin into 1 or more variables.
	// Note that space delimits the format fields, so typing 'Jeff Anderson' will get you just
	// 'Jeff'.	
	scanf("%39s", name);

	printf("Hello, %s!\n", name);

} // main()


