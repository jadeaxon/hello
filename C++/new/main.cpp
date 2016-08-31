#include <iostream>

using namespace std;

// Function prototypes.
void dynamicallyAllocateInteger();



//=============================================================================
// Main
//=============================================================================

// Demonstrates dynamic allocation of memory using the new operator.
int main() {
	dynamicallyAllocateInteger();

} // main()



//=============================================================================
// Public Functions
//=============================================================================

// Dynamically allocates an integer on the heap and then deletes it from the heap.
void dynamicallyAllocateInteger() {
	// int_ptr is a point to an int value.
	// It points to the memory address of an unnamed value.
	// Normal variables are named values of a particular type at some static address.
	//
	// NULL is the special address 0 at which there is no value, no object.
	int* int_ptr = NULL;
	
	// Now, we create an int value on the heap.
	int_ptr = new int;
	
	// We use the dereferencing operator * to assign to the value.
	// Assigning to the pointer itself would be assigning an address to point to a different
	// value/object.
	*int_ptr = 23;

	// Use dereferencing to access the int value agaian.
	cout << "*int_ptr: " << *int_ptr << endl;

	// Free the dynamically allocated value on the heap.
	delete int_ptr;

	// Set pointer back to null so we don't accidentally access its value or free already freed
	// memory.  Doing either can lead to undefined behavior that may crash your program.
	int_ptr = NULL;

} // dynamicallyAllocateInteger()



