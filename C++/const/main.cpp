// Prefer constants over #defines.  They are typesafe.
// Also prefer enums if possible.  May write your own special enum class.

// Demonstrates C++ constants.
int main() {
	// Uncomment the lines beginning with /// to see the compiler errors.

	int i = 0;
	const int ci = 1;
	const int ci2 = 2;
	/// i = 0; // Can't do this; i is constant.

	// A variable pointer to a constant int.
	const int* vptr2ci = &ci;
	/// *ci = 3; // No.  The pointee is constant.
	vptr2ci = &ci2; // Yes.  The pointer is variable.


	const int* const cptr2ci = &ci;
	/// cptr2ci = &ci2; // No.  Both the pointer and the pointee are constant.

} // main()


