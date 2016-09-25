#include <stdio.h>
#include <string.h>

const int BUFFER_SIZE = 1024;

// Gets rid of single trailing newline, if any.
void chomp(char* s) {
	size_t last = strlen(s) - 1;
	if (s[last] == '\n') s[last] = '\0';
}

// A filter reads a line at a time from stdin and transforms/filters each line or summarizes all the
// lines.  It might rearrange the order of the lines as well.  Errors are written to stderr.
// Relies on redirection and pipes to be used with files and output from other programs.  The Unix
// small tool philosophy is that you make a bunch of focused, small commands (like filters), and
// pipe them together to do a bigger job.  The Perl philosophy is to do everything those little
// tools did directly in one language.  So, it's a wheel of reincarnation thing.
//
// Here we have a filter that does nothing.  Just writes each line it reads from stdin to stdout.
// This mimics the behavior of 'cat' when you run it with no args.
int main(int arc, char** argv) {
	char line[BUFFER_SIZE]; // Line buffer.  Needs to be big enough for largest possible line.
	char* result;

	while (1) { 
		result = fgets(line, BUFFER_SIZE, stdin);  // This includes the newline.
		if (result == NULL) break; // EOF (perhaps error).
		// How to we detect a read error in fgets()?
		chomp(line);
		puts(line); // This adds a newline.
	} // next line

} // main()


