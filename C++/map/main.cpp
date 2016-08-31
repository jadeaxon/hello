// C++ Standard Library
#include <iostream>
#include <map>
#include <vector>
#include <stdexcept> // For out_of_range.

using namespace std;



// Demostrates use of vectors.
int main() {
	map<int, int> m;

	// You can use [] operator assign a value to a key.
	m[0] = 0;
	m[1] = 10;
	m[2] = 20;

	// map.insert(pair) inserts the pair *if* the key does not already exist.
	// Otherwise, it does nothing.
	m.insert(make_pair(3, 30));
	m.insert(make_pair(2, 15)); // Nothing should happen here.

	// What happens if we access by a key that DNE?
	// It appears that a new map entry is created with the value initialized to a default.	
	int x = m[10];
	cout << "x: " << x << endl;

	// In C++11, you can use map.at(key).  It throws an out_of_range exception if key DNE.
	// That means that the g++ I am running in Cygwin is C++11 compliant.	
	try {	
		x = m.at(11);
	} 
	catch (out_of_range& e) {
		cout << "You attempted at access a map entry that DNE." << endl;
	}

	// To delete a map entry, use map.erase(key).
	m.erase(0);

	// We can iterate over a map like so.
	map<int, int>::iterator i;
	vector<int> keys;
	vector<int> values;
	for (i = m.begin(); i != m.end(); i++) {
		// A map entry is a pair<int, int>.
		keys.push_back(i->first);
		values.push_back(i->second);
		cout << i->first << " => " << i->second << endl;
	} // next map entry

	
	// Check if map is empty and report its size.
	// Note that you can use 'not' instead of '!'.
	if (not m.empty()) {
		cout << "map.size(): " << m.size() << endl;
	}

	// Let's clear all the elements.
	// Like all STL containers, removing an element does not cause it to be deleted.
	// You have to manage memory yourself.
	m.clear();
	if (m.empty()) {
		cout << "The map is empty after calling map.clear()." << endl;
	}



} // main()









