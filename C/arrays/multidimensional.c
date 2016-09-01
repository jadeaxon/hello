#include <stdio.h>

// Demonstrates the use of multidimensional arrays.
int main(void) {
	// Compiler determines you have 5 strings, so you don't have to declare the first dimension.	
	char tracks[][80] = {
		"I left my heart in Harvard Med School",
		"Newark, Newark - a wonderful town",
		"Dancing with a Dork",
		"From here to maternity",
		"The girl from Iwo Jima",
	};

	int length = sizeof(tracks) / (sizeof(char) * 80);
	printf("Length: %i\n", length);

	for (int i = 0; i < length; i++) {
		printf("Title: %s\n", tracks[i]);
	}

} // main()


