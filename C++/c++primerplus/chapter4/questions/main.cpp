#include <iostream>
#include <string>
#include <vector>
#include <array> // C++11

using namespace std;


// 8.
struct Fish {
	string type;
	int weight; // In ounces.
	float length; // In inches.

};


// 10.
enum Response {No, Yes, Maybe};


int main(int argc, char* argv[]) {
	// 1.
	char actors[30];
	short betsie[100];
	float chuck[13];
	long double dipsea[64];

	// 2.
	// No.
	
	// 3.
	int odds[] = {1, 3, 5, 7, 9};

	// 4.
	int even = odds[0] + odds[4];
	cout << even << endl;

	// 5.
	float ideas[] = {1.1f, 2.2f};
	cout << ideas[1] << endl; // Print 2nd element of array.

	// 6.
	char cstring[] = "cheeseburger";

	// 7.
	string stdstring("Waldorf Salad");


	// 9.
	Fish fish = {"trout", 3, 17.2f};
	cout << fish.type << endl;

	// 11.
	double ted = 7.77;
	double* ted_ptr = &ted;
	cout << *ted_ptr << endl;

	
	// 12.
	float treacle[] = {0.0f, 1.1f, 2.2f, 3.3f, 4.4f, 5.5f, 6.6f, 7.7f, 8.8f, 9.9f};
	float* p = &(treacle[0]);
	cout << "First: " << *p << endl;
	p += 9;
	cout << "Last: " << *p << endl;


	// 13.
	int size = 0;
	cout << "How large should the int array be? ";
	cin >> size; cin.get();
	int* int_array = new int[size];
	vector<int> int_vector(size);


	// 14. 
	// I say it is valid (though stupid) and just prints out the address of the string.
	cout << (int*) "Home of the jolly bytes" << endl;

	// 15.
	// Fish* f = new Fish {"carp", 4, 12.2f};
	Fish* f = new Fish();
	cout << "Type: " << "'" << f->type << "'" << endl;


	// 16. You would just get a single word assigned to the address variable rather than an entire
	// line.
	
	// 17.
	const int SIZE = 10;
	vector<string> vos(SIZE);
	array<string, SIZE> aos;


} // main(...)

