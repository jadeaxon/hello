#include <iostream>

using namespace std;

void printArray(const char*, int* const, unsigned int);


// Prints any kind of array.
// Could you even do function prototypes for a template function?
// Wow, this actually works!
template<typename Type, int Size>
void print(const char* name, Type const(& array)[Size]) {
	using namespace std;
	for(int i = 0; i < Size; i++) {
		cout << name << "[" << i << "] = " << array[i] << endl;
		// cout << array[Size] << endl;
	} // next element
} // print(...)


// Demostrates use of arrays.
int main() {
	// A C style array does not know its own length at runtime.
	// You need to keep track of this yourself.
	const int ARRAY_LENGTH = 10;
	
	// {} list initializer syntax
	// The [] comes after the array name.  I don't like this.  Should be int[] values.
	// An array is a const pointer to variable data pointing to the first element of
	// a fixed number of statically allocated values of a single type.
	//
	// You can only use an initializer list when defining an array.
	// You can not use it for later assignments at runtime.
	int values[ARRAY_LENGTH] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

	// Calculate the length of any array like this.
	int length = sizeof(values) / sizeof(int);

	// If you partially init an array, remaining values are set to 0.
	// If you don't init an array, all its values are random garbage.
	int uninitialized[7]; // Random garbage.
	int zeros[13] = {0}; // Initialized to all zeros.

	// Iterate over an array with a for loop.
	for (int i = 0; i < ARRAY_LENGTH; i++) {
		// Access elements of array by index with [] array subscript operator.
		// Array indexes are 0-based.
		cout << "values[" << i << "] = " << values[i] << endl;
	} // next element
	cout << endl;

	printArray("values", values, ARRAY_LENGTH);
	print("values", values);
	print("zeros", zeros);
	cout << "length == " << length << endl;


	// Note that an array really is just a pointer.
	// This won't work because &values is a pointer to a size 10 int array. 
	// int* iptr = &values; 
	// This will work because values is a int* const.
	int* const iptr = values; // You could also assign to a non-const int*.
	// const int* const iptr would be a constant pointer to constant integers.
	// Whereas int* const is a constant pointer to variable integers.
	int thirdValue = *(iptr + 2); // Same as values[2].
	cout << "thirdValue == " << thirdValue << endl;

} // main()


// Prints out the values of an int array.
// Seems like we need generic programming to handle all cases.
// Could do with a bunch of overloads.
void printArray(const char* name, int* const array, unsigned int length) {
	for (unsigned int i = 0; i < length; i++) {
		cout << name << "[" << i << "] = " << array[i] << endl;
	} // next element

} // printArray(...)



