#include <iostream>

// Demonstates various literal values.  Generally, you want to avoid magic numbers in
// your code.
int main() {
	using namespace std;

	// Single quotes are used in C++ for character literals.
	// Double quotes are used for C string literals.
	char c1 = 'C'; // char literal
	char c2 = 10; // char literal (assigning in range int literal)

	short s = 255; // assign in range int literal to a short

	int chest = 42; // decimal integer literal
	int waist = 0x42; // hexadecimal integer literal
	int inseam = 042; // octal integer literal

	unsigned unsigned_int = 13u; // unsigned int literal
	unsigned long unsigned_long = 1234567890ul; // unsigned long int literal

	float f = 3.14f; // float literal
	double d = 3.14; // double literal
	double ds = 31.4e-1; // double literal; scientific notation (e-1 => *10^-1).
	long double dl = 3.14L; // long double literal


	long l = 1234657890L; // long literal
	long long ll = 1234567890LL; // long long literal (C++11)

	// C string literals.  Null terminated.
	const char* s1 = "A string.";
	char s2[256] = "A string you can safely modify.";

	// Wide character string literal.
	const wchar_t* ws1 = L"A wide character string.";

	cout << "Monsieur cuts a striking figure!\n";
	cout << "chest = " << chest << " (42 in decimal)\n";
	cout << "waist = " << waist << " (0x42 in hex)\n";
	cout << "inseam = " << inseam << " (042 in octal)\n";
	
	// An exercise from C++ Primer Plus.
	int i = 88;
	wchar_t u = L'\x58'; 
	
	cout << char(i) << endl;
	wcout << u << endl;

	return 0;
} // main()

