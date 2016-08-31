#include <stdio.h>


// Ha, there is no println in C.  I'm too used to Java.
void println(char*);


main() {
	int value = 1;

	// The switch query value can be any integer type including char.
	switch(value) {
		case 0:
			println("The value is zero.");
			break;
			// If you don't use a break, execution will "fall through" to the next case.
			// That case will also be exectuted.
		case 1:
			println("The value is one.");
			break;
		case 2:
			println("The value is two.");
			break;

		// The default case is executed if no other cases trigger.
		// You can also fall through to the default case.  Even if another case did trigger.
		default:
			println("I don't know about that value.");


	} // switch

} // main()



void println(char* string) {
	printf("%s\n", string);

} // println(char*)

