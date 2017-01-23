// Demonstrates the use of a vararg (variadic) function.

#include <stdarg.h> // For variadic functions.
#include <stdio.h> // printf().

int sum(int args, ...) {
	va_list ap; // The vararg list.  
	// Q. Why is the va_list called ap?
	// Q. Does the first arg have to tell you how many more args there are?	
	va_start(ap, args); // The variable list starts after the args argument.
	int sum = 0;
	for (int i = 0; i < args; i++) {
		int value = va_arg(ap, int);
		sum += value;
	}
	return sum;
}


int main() {
	int total = sum(4, 1, 2, 3, 4);
	printf("Total: %d\n", total);

} // main()


