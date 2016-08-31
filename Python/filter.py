#!/usr/bin/env python

import fileinput
import sys
import os


# TO DO: Create a Filter subclass.

# Strangely, if you check this later it will return false, so cache it up front.
stdinIsATerminal = os.isatty(0)
print stdinIsATerminal
print os.isatty(1)
print os.isatty(2)

# This is a basic pipe filter.  All it does is add line numbers to whatever data it filters.
#
# You can call it in these ways:
# ./hello_filter => interactive stdin
# command | ./hello_filter => filter noninteractive stdin piped in from another command
# ./hello_filter file1.ext ... fileN.ext => filter each file line by line
# ./hello_filter file.ext - => filter file.ext and then stdin interactively
# command | ./hello_filter file.ext => not sure what should happen, but the piped stdin is simply ignored
# command | ./hello_filter file.ext - => processes file.ext followed by the piped input


print sys.argv

# It works very much like Perl's 
# while (<>) {
#
# }
#
# If I call the script with no args or piped input, it requires me to hit ^D (EOF) twice instead of once for the 
# script to end.
#
# It does respect the '-' pseudofile arg to process stdin.
hasFileArgs = True
try:
	arg = sys.argv[1]
except:
	print "Exception."
	hasFileArgs = False

print "hasFileArgs: %s" % hasFileArgs
print "stdinIsATerminal: %s" % stdinIsATerminal

# If we are taking user input from the terminal, process each line one at a time like cat does.
# If we are processing files or attached to a pipe, use fileinput module to process the stream.
# The fileinput module does not handle terminal input correctly.
if (not hasFileArgs) and stdinIsATerminal:
	# This behaves as well as cat does in Cygwin relative to ^D.
	line_number = 0
	while True:
		line = sys.stdin.readline()

		controlD = False
		if not line.endswith("\n"): controlD = True	
		if not line: break

		line_number += 1
		line = line.rstrip()
		print "%d: %s" % (line_number, line)
		
		if controlD: break
	# next line
else:
	line_number = 0
	for line in fileinput.input():
		line_number += 1
		line = line.rstrip()
		print "%d: %s" % (line_number, line)
	# next line
# else



