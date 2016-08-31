#include <iostream>
#include <string>

using namespace std;


struct CandyBar {
	string brand;
	double weight;
	int calories;

};


int main(int argc, char* argv[]) {
	CandyBar snack = {"Mocha Munch", 2.3, 350};
	cout << snack.brand << endl;
	cout << snack.weight << endl;
	cout << snack.calories << endl;


} // main(...)





