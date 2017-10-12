#!/usr/bin/env python3

# Import argv for command-line args.
from sys import argv

# Unpack the command-line args.
script, filename = argv

# Open the file.
print(f"Opening '{filename}'.")
f = open(filename, 'r')

contents = f.read() # Slurp.
print(contents)


# Close the file.
print("And finally, we close it.")
f.close()


