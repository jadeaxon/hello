#include <iostream>
#include <vector>

using namespace std;


// Demostrates use of vectors.
int main() {
	// Does list initializer syntax work with a vector?  No.  Not in C++98 at least.
	// FAIL: vector<int> v = {1, 2, 4, 8};
	vector<int> v;
	v.push_back(16); // Why can't they just call it 'append' like normal people?
	v.push_back(32);
	v.push_back(64);
	v.push_back(128);
	
	// The auto keyword can figure this type out for you.
	// But will this work in our L7/L10 code?
	vector<int>::iterator i;

	// Should I be using ++i here for some reason?
	// 'auto' does not appear to work here.  Is it C++11?
	for (i = v.begin(); i != v.end(); i++) {
		// An iterator is really a smart pointer, so you have to deref it with *.
	    cout << *i << endl;
	} // next element

	// Is there a 'for i in L' syntax?  I know Qt has one.
	// But does it work with normal C++ crap?

} // main()









