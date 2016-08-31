#include <iostream>
#include <string>

using namespace std;


// A struct is really just a class whose default membership access is public.
// In C, a struct is restricted to just data members and you have to use the
// struct keyword instead of just the type name when declaring variables.
// Basically, they are better in C++.
// The only time you would use them is to emphasize that you really just want a
// clump of pure data.
struct Pizza {
	string name;
	double weight;
	double diameter;

};


int main(int argc, char* argv[]) {
	// Pizza pizza;
	// Swithed from using . member accessor on stack allocated struct var to
	// using -> on heap allocated struct object.
	Pizza* pizza = new Pizza();


	cout << "Diameter: ";
	cin >> pizza->diameter; cin.get();

	cout << "Name: ";
	getline(cin, pizza->name);

	cout << "Weight: ";
	cin >> pizza->weight; cin.get();

	cout << endl;
	cout << pizza->name << endl;
	cout << pizza->weight << endl;
	cout << pizza->diameter << endl;


} // main(...)





