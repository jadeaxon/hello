#include <iostream>
#include <string>

using namespace std;



int main(int argc, char* argv[]) {
	const int SIZE = 3;
	double times[SIZE];

	// Input all the times.
	for (int i = 0; i < SIZE; i++) {
		cout << "t" << i << ": ";
		cin >> times[i]; cin.get();
	} // next time


	double sum = 0.0;
	for (int i = 0; i < SIZE; i++) {
		cout << times[i] << endl;
		sum += times[i];

	} // next time

	double average = sum / SIZE;
	cout << "Average: " << average << endl;


} // main(...)





