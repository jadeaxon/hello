#include <stdio.h>

// EOF is defined in <stdio.h>.

// Copies stdin to stdout.
main() {
	printf("EOF = %d\n", EOF);

	int c = 0;
	// I see the characters line-by-line, when user hits enter.
	// This does not see them immediately as each key is pressed.
	// Pressing ^D causes an EOF on stdin.
	while (1) {
		c = getchar();
		int result = (c != EOF);
		printf("result = %d\n", result);
		if (result == 0) {
			break;
		}
		putchar(c);
	} // next character

} // main()

