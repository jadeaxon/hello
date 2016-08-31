#include <stdio.h>

// This is in the digEcor digelib StringUtil namespace.


// Deletes all occurences of given character from a C string.
// Mutates the string arg.
void deleteAll(char* s, char charToDelete) {
    char* ip = s; // Where to insert next good character.
    char* cp = s; // Pointer to current character to examine.

    while (*cp != '\0') {
        // Is this a good character that we want to keep?
        if (*cp != charToDelete) {
            *ip = *cp;
            ip++;
        }
        else { // Not a character we want to keep.
            // Do nothing.
        }
        cp++;

    } // next character


    // All good characters are now to the left of ip.  So, null terminate the string.
    *ip = '\0';

} // deleteAll(char*, char)



// Deletes the character 'i' from various strings.
int main(int argc, char* argv[]) {
	char s[][80] = {
		"fizziness",
		"igloo",
		"bantii",
		"iinterupt",
		"iandi",
		"unmodufyed"
	};

	// Get size of array.
	int size = sizeof(s) / sizeof(s[0]);

	for (int i = 0; i < size; i++) {
		printf("%s => ", s[i]);

		deleteAll(s[i], 'i');

		printf("'%s'\n", s[i]);
	} // next string

} // main(...)


