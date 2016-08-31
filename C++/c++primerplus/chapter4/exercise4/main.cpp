#include <iostream>
#include <string>

using namespace std;


int main(int argc, char* argv[]) {
	string first;
	string last;
	string sep(", ");
	string result;

	cout << "What is your first name? ";
	getline(cin, first);

	cout << "What is your last name? ";
	getline(cin, last);


	result = last + sep + first;

	cout << endl;
	cout << "Name: " << result << endl;

} // main(...)





