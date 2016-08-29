// A pointer
// is a variable whose value is a memory address
// can be dereferenced with the * operator
// interprets the pointed-to value (the pointee/referant) as being of a certain data type
// can be passed to a function enabling the function to mutate the pointee

#include <stdio.h> // For printf().

void mutate(int*); // Function prototype.  Because we refer to it before it's defined.

// Demonstrates some basic usage of pointers.
int main() {
	int pointee = 42;
	int* pointer = &pointee; // The & (address) unary operator yields the memory address of a variable.

	printf("I am pointing to the int at address %p.\n", pointer);
	mutate(pointer);
	mutate(&pointee); // Just pass the address directly rather than using an intermediary pointer var.
	// WARNING: If the function stores pointers to stack variables, it may try to use them later
	// when that stack variable no longer exists.  Thus, it is safer to pass pointers to values on
	// the heap since they tend to have greater duration than stack values.
	printf("That int now has value %i.\n", pointee);
}


// Increments the given int by 1.
// C functions pass args by value.  But, a pointer passed by value still points to the same thing.
// void mutate(const int* intToChange) { // No, this makes the pointee const.
void mutate(int* const intToChange) {
	// We declare the pointer arg const because we don't want the function changing where the
	// pointer points to!  Using const here does not prevent us from changing the pointee's value,
	// as you can see.

	// intToChange = NULL; // Illegal since pointer arg is const.

	// Dereferencing works in assignment and expression evaluation.
	*intToChange = *intToChange + 1;
}

