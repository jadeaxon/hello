#include <iostream>

using namespace std;


// Demonstrates the use of many kinds of primitives.
int main() {
	char c;
	unsigned char cu;
	int i;
	unsigned int iu;
	short int is;
	short iis; // Same as short int
	unsigned short int isu;
	unsigned short iisu;
	long int il;
	long iil; // Same as long int
	unsigned long int ilu;
	unsigned long iilu;
	float f;
	double d;
	long double ld;

	short s = 80;
	unsigned int ui = 42110;
	
	// This shouldn't work unless int is 64 bit.
	// Only a warning is given!  It overflows clocking to a negative number!	
	int i2 = 3000000000; 


	// The number of bytes used to store each primitive data type is machine-dependent.
	cout
		<< "\n char= " << sizeof(c)
		<< "\n unsigned char = " << sizeof(cu)
		<< "\n int = " << sizeof(i)
		<< "\n unsigned int = " << sizeof(iu)
		<< "\n short = " << sizeof(is)
		<< "\n unsigned short = " << sizeof(isu)
		<< "\n long = " << sizeof(il)
		<< "\n unsigned long = " << sizeof(ilu)
		<< "\n float = " << sizeof(f)
		<< "\n double = " << sizeof(d)
		<< "\n long double = " << sizeof(ld)
		<< endl
	; // cout

	cout << i2 << endl;

} // main()
