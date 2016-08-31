#include <iostream>

using namespace std;


int main(int argc, char* argv[]) {
	char first[80];
	char last[80];
	char grade = 'A';
	unsigned short age = 0;

	cout << "What is your first name? ";
	cin.getline(first, 80);

	cout << "What is your last name? ";
	cin.getline(last, 80);

	cout << "What letter grade do you deserve? ";
	cin >> grade; cin.get();

	cout << "What is your age? ";
	cin >> age; cin.get();

	cout << endl;
	cout << "Name: " << last << ", " << first << endl;
	cout << "Grade: " << char(grade + 1) << endl;
	cout << "Age: " << age << endl;

} // main(...)





