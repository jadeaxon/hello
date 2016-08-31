#include <stdio.h>

// Function prototype.  Declare function interface so that you can use it before it is defined.
int foo(int, int);


main() {
	printf("Result = %d\n", foo(1, 3));

}



int foo(int arg1, int arg2) {
	int result = arg1 + arg2;
	return result;

}


