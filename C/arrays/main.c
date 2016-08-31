// An array
// is (like) a constant pointer to a (sequence of) variable(s) of some type
// has a fixed length (is not dynamic like a STL vector or a Python array)
// should be initialized when it is created (can use special initializer syntax)
// can be initialized via a C string literal
// has an element type


#include <stdio.h> // For printf().

int main(void) {
	char cstring[] = "You can use a C string to init a char array.";
	int array[] = {0, 1, 2, 3}; // Array initializer syntax.
	int array2[] = {4, 5, 6}; 

	// An array is (like) a constant pointer to sequence of variables all of the same type.
	// The array points to the first address of that sequence.
	// You cannot change where it points.
	// array = array2; // FAIL
	// array = &array2; // FAIL

	// You can only assign to elements of arrays (because they are variables).
	// Array indexing is 0-based (using int values).
	//
	// sizeof(array) returns the size of the seq of array elements in bytes.
	// sizeof(array) does *NOT* return the array length (number of elements).
	int length = sizeof(array) / sizeof(int); // Divide total bytes by bytes per element type.
	printf("array length: %i\n", length);
	for (int i = 0; i < length; i++) { 
		printf("array[%i]: %i\n", i, array[i]);
	} // next array element
	printf("\n");

	// Note that we can set length to whatever here and the loop would have continued merrily
	// reading from addresses in memory that don't actually belong to the array.  That is, C does no
	// bounds checking on array access (like Java does).  It's up to you to do that.
	int bogusLength = 10;
	for (int i = 0; i < bogusLength; i++) {
		if (i < length) {
			printf("array[%i]: %i\n", i, array[i]);
		}
		else { // Out of bounds array access.
			printf("array[%i]: %i (out of bounds)\n", i, array[i]);
		}
	} // next array element
} // main()

