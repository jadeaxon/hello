#include <stdio.h>

// Make a typedef for a struct.  This is as close as you get to a class in C.
typedef struct fish {
	const char* name;
	const char* species;
	int teeth;
	int age;
} Fish;

void Fish__describe(Fish* fish);


// Uses a struct.
int main(int argc, char* argv[]) {
	Fish fish1;
	fish1.name = "Deep Moses";
	fish1.species = "catfish";
	fish1.teeth = 1;
	fish1.age = 100;

	Fish fish2;
	fish2.name = "Golden Boy";
	fish2.species = "carp";
	fish2.teeth = 2;
	fish2.age = 1;

	// Initializer syntax.
	Fish fish3 = {"Nemo", "ocellaris", 4, 2};

	Fish__describe(&fish1);
	Fish__describe(&fish2);
	Fish__describe(&fish3);


} // main(...)


// Describes a fish.  You could make a bunch of functions like this that work on Fish structs.
void Fish__describe(Fish* fish) {
	if (fish->teeth == 1) {
		printf("This %d year old %s, %s, has %d tooth.\n", fish->age, fish->species, fish->name, fish->teeth);
	}
	else {
		printf("This %d year old %s, %s, has %d teeth.\n", fish->age, fish->species, fish->name, fish->teeth);
	}
}



