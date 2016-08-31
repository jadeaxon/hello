#include <stdio.h>

main() {
	int c = 0;

	/*
	int tabs = 0;
	int spaces = 0;
	int newlines = 0;
	*/

	// Array to hold count for each (extended) ASCII character.
	int ascii[256];
	int i = 0;
	for (i = 0; i < 256; i++) {
		ascii[i] = 0;
	}


	while ( (c = getchar()) != EOF ) {
		/*
		if ( c == '\t' ) {
			tabs++;
		}
		else if ( c == ' ' ) {
			spaces++;
		}
		else if ( c == '\n' ) {
			newlines++;
		}
		*/

		ascii[c]++;

	} // next character


	/*
	printf("tabs = %d\n", tabs);
	printf("spaces = %d\n", spaces);
	printf("newlines = %d\n", newlines);
	*/

	// Report counts for each character.
	for (i = 0; i < 256; i++) {
		
		if (isprint(i)) {
			if (i == 32) {
				printf("%d\tSpace\t%d\n", i, i);
			}
			else { // A non-space printable character.
				printf("%d\t%c\t%d\n", i, i, ascii[i]);
			}
		}
		else { // Unprintable character.
			char symbol[10];
			char* s = NULL;
			switch (i) {
				case  0: s = "NUL"; break; // null character
				case  1: s = "SOH"; break; // start of text
				case  2: s = "STX"; break; // start of heading
				case  3: s = "ETX"; break; // end of text
				case  4: s = "EOT"; break; // end of transmission
				case  5: s = "ENQ"; break; // enquiry
				case  6: s = "ACK"; break; // acknowledge
				case  7: s = "BEL"; break; // audible bell
				case  8: s = "BS" ; break; // backspace, \b
				case  9: s = "TAB"; break; // horizontal tab, \t
				case 10: s = "LF" ; break; // NL line feed (newline), \n
				case 11: s = "VT" ; break; // vertical tab, \t
				case 12: s = "FF" ; break; // NP form feed (new page)
				case 13: s = "CR" ; break; // carriage return
				case 14: s = "SO" ; break; // shift out
				case 15: s = "SI" ; break; // shift in
				case 16: s = "DLE"; break; // data link escape
				case 17: s = "DC1"; break; // device control 1
				case 18: s = "DC2"; break; // device control 2
				case 19: s = "DC3"; break; // device control 3
				case 20: s = "DC4"; break; // device control 4
				case 21: s = "NAK"; break; // negative acknowledgement
				case 22: s = "SYN"; break; // synchronous idle
				case 23: s = "ETB"; break; // end of transmission block
				case 24: s = "CAN"; break; // cancel
				case 25: s = "EM" ; break; // end of medium
				case 26: s = "SUB"; break; // substitute
				case 27: s = "ESC"; break; // escape
				case 28: s = "FS" ; break; // file separator
				case 29: s = "GS" ; break; // group separator
				case 30: s = "RS" ; break; // record separator

				case 31: s = "US" ; break; // unit separator
				
				// The space character is a printable character.
				// case 32: s = "Space"; break; // space character

				case 127: s = "DEL"; break; // delete character


				default:
					sprintf(symbol, "\\x%02x", i);
			}

			if (s != NULL) {
				sprintf(symbol, "%s", s);
			}

			printf("%d\t%s\t%d\n", i, symbol, ascii[i]);

		}

	} // next character


} // main()
