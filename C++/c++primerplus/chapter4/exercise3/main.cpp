#include <iostream>
#include <cstring>

using namespace std;


int main(int argc, char* argv[]) {
	char first[80];
	char last[80];
	char sep[] = ", ";
	char result[164];

	

	cout << "What is your first name? ";
	cin.getline(first, 80);

	cout << "What is your last name? ";
	cin.getline(last, 80);

	strcpy(result, last);
	strcat(result, sep);
	strcat(result, first);

	cout << endl;
	cout << "Name: " << result << endl;

} // main(...)





