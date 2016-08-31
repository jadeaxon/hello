#include <cassert>

// Because 'assert' is a macro, it is in the global namespace, not the std:: namespace.
// This is another reason macros and defines are dangerous.
// using std::assert;

// If NDEBUG is set, it means "no debugging".  This disables the assert macro.
#undef NDEBUG

// The assertion mechanism comes from C.  It is a macro.
// An assertion should never have side effects since may not be present at all in production code.

// Do not use assertions for arg validation.  Throw an IllegalArgumentException or NullPointerException.
// Or whatever the C++ versions of those are.

// When an assertion fails, abort() is called.

// See what happens if we fail an assertion.
int main(int argc, char* argv[]) {
	assert(true);
	// assert(false);
	assert(false && "Custom error message."); // Since a string evals to true.

}


