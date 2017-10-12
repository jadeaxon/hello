#!/usr/bin/env python3

# This script copies a file to a new location.

# Use argv to get command-line args.
from sys import argv
# Import a symbol from a submodule.
from os.path import exists

# Unpack the command-line args.
script, from_file, to_file = argv

# We could do these two on one line, how?
# Use, you can chain method calls.  But for clarity and debug, not best idea.
# indata = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()

# Copy contents of from_file to to_file.
out_file = open(to_file, "w")
out_file.write(indata)

# Clean up.
out_file.close()
in_file.close()

