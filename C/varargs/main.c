// Demonstrates the use of a vararg (variadic) function.

#include <stdarg.h> // For variadic functions.
#include <stdio.h> // printf().

// First arg args tells us how many more args to process.
int sum(int args, ...) {
	va_list ap; // The vararg list.  
	// Q. Why is the va_list called ap?
	// A. Probably means 'arg pointer'.
	//
	// Q. Does the first arg have to tell you how many more args there are?	
	// A. It has to know somehow.  Whether by explicit count, implicit count
	// (like in printf field specifiers) or a sentinel value.
	va_start(ap, args); // The variable list starts after the args argument.
	int sum = 0;
	for (int i = 0; i < args; i++) {
		int value = va_arg(ap, int);
		sum += value;
	}
	va_end(ap); // This is a macro.  Likely so is va_start().
	return sum;
}


int main() {
	int total = sum(4, 1, 2, 3, 4);
	printf("Total: %d\n", total);
	total = sum(5, 3, 3, 3, 3, 3);
	printf("Total: %d\n", total);

} // main()


