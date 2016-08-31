#include <stdio.h> // For printf() and scanf().

// Demonstrates basic command line input.
int main(void) {
	char name[40] = "Nameless Wanderer";
	int age = 0;
	// Prompt for input.  No trailing newline.
	printf("Enter your name: ");
	
	// 39 so there is 1 char left for trailing null char.
	// Reads a formatted input string from stdin into 1 or more variables.
	// Note that space delimits the format fields, so typing 'Jeff Anderson' will get you just
	// 'Jeff'.
	//
	// WARNING: scanf does not do bounds checking.  If you use a formatter that reads in more
	// characters than your array can hold, you'll likely get a seg fault.
	// If user just enters too many chars, these will still be in the buffer when the next scanf is
	// called.  So, you probably need to flush this between scanf calls.
	scanf("%39s", name);

	printf("Enter your name (fgets): ");
	// This doesn't work if called after scanf.
	// fgets includes the newline in what is read.  Maybe scanf pushes the newline back and fgets
	// instantly reads it.  Again, probably need to flush stdin before reading it.	
	fgets(name, sizeof(name), stdin); 

	printf("How old are you? ");
	scanf("%i", &age); // scanf wants a pointer, address, or array

	printf("Hello, %s (age %i)!\n", name, age);

} // main()


