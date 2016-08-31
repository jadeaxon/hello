#include <iostream>
#include <string>

using namespace std;


struct CandyBar {
	string name;
	double weight;
	int calories;

};


int main(int argc, char* argv[]) {
	CandyBar* snacks = new CandyBar[3];
	CandyBar* snack_ptr = &(snacks[0]);
	snack_ptr->name = "Chocha Cunch";
	snack_ptr->weight = 2.3;
	snack_ptr->calories = 650;

	CandyBar snack = {"Mocha Munch", 3.2, 560};
	cout << snack.name << endl;
	cout << snack.weight << endl;
	cout << snack.calories << endl;

	cout << snack_ptr->name << endl;
	cout << snack_ptr->weight << endl;
	cout << snack_ptr->calories << endl;



} // main(...)





