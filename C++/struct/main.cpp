#include <iostream>

// A structure declaration.
// A structure is really just a class whose members are all public by default.
// Generally, a struct will have only data members and no methods.
// But, you certainly can add methods to a C++ struct.
// In new code, you should never make a struct.  Use a class instead.
// A structure is used to combine/compose related values of different types.
// It provides some cohesion, but weak encapsulation.
struct StoreItem {
	char name[80];
	float weight;
	double price;
};


// Demonstrates use of structures.
int main() {
	using namespace std;
	
	// In C, you'd have to say
	// struct StoreItem coke;
	// You can initialize a struct much like you can an array.
	StoreItem coke = {
		"Coke", // name value
		1.88, // weight value
		29.99 // price value
	}; 
	
	StoreItem pepsi = {
		"Pepsi",
		3.12,
		32.99
	}; 

	cout << "This store has " << coke.name << " and " << pepsi.name << "." << endl;


	// You can do a shallow memberwise copy with the assignment operator.
	StoreItem unknown;
	unknown = pepsi;
	cout << "Unknown is now " << unknown.name << "." << endl;
	cout << endl;

	// You can have an array of structures.
	// Notice how you can initialize them.
	StoreItem items[] = {
		{"Lo Mein", .5, 1.39},
		{"Egg Roll", .25, .75},
		{"Kung Pow Chicken", 1.5, 3.29}
	};


	int size = sizeof(items) / sizeof(StoreItem);
	for (int i = 0; i < size; i++) {
		cout << "name: " << items[i].name << endl;
		cout << "weight: " << items[i].weight << endl;
		cout << "price: " << items[i].price << endl;
		cout << endl;
	} // next item


	// TO DO: Structures also have a special syntax that lets you use
	// them as bit vector.
	// You may want to use std::bitset for this.
	// If you don't care about space, vector<bool> is fine too.
	// Or, you can just bit twiddle on an unsigned int.

} // main()
